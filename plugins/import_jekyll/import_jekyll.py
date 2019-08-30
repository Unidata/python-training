# -*- coding: utf-8 -*-

# Copyright © 2014, 2015 Miguel Ángel García

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from __future__ import unicode_literals, print_function

import os
import re
import datetime
import codecs

import yaml
import dateutil

from nikola.plugin_categories import Command, PageCompiler
from nikola import utils
from nikola.plugins.basic_import import ImportMixin
from nikola.plugins.command.init import SAMPLE_CONF, prepare_config

LOGGER = utils.get_logger('import_jekyll', utils.STDERR_HANDLER)


class JekyllImportError(Exception):
    def __init__(self, arg, *args, **kwargs):
        self._arg = arg
        super(JekyllImportError, self).__init__(*args, **kwargs)


class JekyllConfigurationNotFound(JekyllImportError):
    def __str__(self):
        return 'Jekyll configuration file was not found at %s' % self._arg


class CommandImportJekyll(Command, ImportMixin):
    """Import a Jekyll or Octopress blog."""

    name = "import_jekyll"
    needs_config = False
    doc_usage = "[options] jekyll_site"
    doc_purpose = "import a Jekyll or Octopress site"
    cmd_options = ImportMixin.cmd_options

    _jekyll_config = None
    _jekyll_path = None
    _url_slug_mapping_file = None

    def _execute(self, options, args):
        """Import a Jekyll/Octopress site."""
        # Configuration
        self.import_into_existing_site = False

        # Parse args
        self._jekyll_path = args[0] if args else '.'
        self.output_folder = options['output_folder']

        # Execute
        try:
            self._read_config()
            self._write_site()
            self._import_posts()
        except JekyllImportError as e:
            LOGGER.error('ERROR: %s' % e)

    def _read_config(self):
        path = os.path.join(self._jekyll_path, '_config.yml')
        if not os.path.exists(path):
            raise JekyllConfigurationNotFound(path)

        LOGGER.debug('Loading Jekyll configuration file %s', path)
        with open(path) as fd:
            self._jekyll_config = yaml.load(fd.read())

    def _write_site(self):
        context = SAMPLE_CONF.copy()

        context['DEFAULT_LANG'] = 'en'
        context['BLOG_TITLE'] = self._jekyll_config.get('title', 'EXAMPLE')

        context['BLOG_DESCRIPTION'] = self._jekyll_config.get('description') or ''
        context['SITE_URL'] = self._jekyll_config.get('url', 'EXAMPLE')
        context['BLOG_EMAIL'] = self._jekyll_config.get('email') or ''
        context['BLOG_AUTHOR'] = self._jekyll_config.get('author') or ''

        context['POSTS'] = """(
            ("posts/*.md", "blog", "post.tmpl"),
            ("posts/*.rst", "blog", "post.tmpl"),
            ("posts/*.txt", "blog", "post.tmpl"),
            ("posts/*.html", "blog", "post.tmpl"),
            )"""

        if 'disqus_short_name' in self._jekyll_config:
            context['COMMENT_SYSTEM'] = 'disqus'
            context['COMMENT_SYSTEM_ID'] = self._jekyll_config[
                'disqus_short_name']

        if self._jekyll_config.get('', False):
            context['PRETTY_URLS'] = True
            context['INDEXES_PRETTY_PAGE_URL'] = True

        conf_template = self.generate_base_site()
        conf_out_path = self.get_configuration_output_path()

        conf_template_render = conf_template.render(**prepare_config(context))
        self.write_configuration(conf_out_path, conf_template_render)

    def _import_posts(self):
        rel_path = self._jekyll_config.get('source', '')
        posts_path = os.path.join(self._jekyll_path, rel_path, '_posts')
        importer = JekyllPostImport()

        for dirpath, dirnames, filenames in os.walk(posts_path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                if not filepath.lower().endswith(
                        ('.md', '.markdown', '.html', 'rst', '.textile')):
                    LOGGER.warning('Unknown format for file %s. Ignoring it!'
                                   % filepath)
                    continue
                LOGGER.info('Importing post %s' % filepath)
                output_relfile, nikola_post = importer.import_file(filepath)
                output_file = os.path.join(self.output_folder, 'posts',
                                           output_relfile)
                utils.makedirs(os.path.dirname(output_file))
                with codecs.open(output_file, 'w', encoding='utf-8') as fd:
                    fd.write(nikola_post)
                LOGGER.info('Writing post %s' % output_file)


class JekyllPostImport(object):
    def import_file(self, path):
        def new_filename(filename):
            _, ext = os.path.splitext(filename)
            return '{0}{1}'.format(slugify_file(filename), ext)

        jmetadata, jcontent = self._split_metadata(path)
        metadata = self._import_metadata(path, jmetadata)
        doc = self._import_content(path, jcontent)

        filename = os.path.basename(path)
        date = metadata['date']
        output_file = os.path.join(str(date.year), str(date.month),
                                   str(date.day), new_filename(filename))

        content = self._serialize(metadata, doc, is_html(path))
        return output_file, content

    def _serialize(self, metadata, doc, is_html):
        header = utils.write_metadata(metadata)

        pattern = '<!--\n{0}\n-->\n\n{1}' if is_html else '{0}\n\n{1}'
        return pattern.format(header.strip(), doc)

    def _split_metadata(self, path):
        with codecs.open(path, encoding='utf-8') as fd:
            post_content = fd.read()
        metadata = next(yaml.load_all(post_content))

        composer_iter = yaml.compose_all(post_content)
        composer = next(composer_iter)
        last_line = composer.end_mark.line + 1
        content = '\n'.join(post_content.splitlines()[last_line:])

        return metadata, content

    def _import_metadata(self, path, jmetadata):
        def extract_date():
            raw_date = jmetadata.get('date')
            if isinstance(raw_date, datetime.date):
                return raw_date
            if isinstance(raw_date, str):
                return dateutil.parser.parse(raw_date)

            # date not in metadata or unreadable. Trying from filename.
            raw_date = re.findall(r'\d+\-\d+\-\d+', path)
            if raw_date:
                return dateutil.parser.parse(raw_date[-1])
            LOGGER.warning('Unknown date "%s". Using today.', raw_date)
            return datetime.date.today()

        def extract_title():
            if 'title' in jmetadata:
                return jmetadata['title']
            regex = (
                r'(?:\d+-\d+-\d+-)'
                r'(?P<name>.+?)'
                r'(?:\.\w+)?$'
            )
            m = re.match(regex, path)
            if m is None:
                return None
                name = m.group('name')
            return name

        tags = [x for x in jmetadata.get('tags') or [] if x]
        categories = [x for x in jmetadata.get('categories') or [] if x]

        metadata = PageCompiler.default_metadata.copy()
        metadata['title'] = extract_title()
        metadata['slug'] = slugify_file(path)
        metadata['date'] = extract_date()
        if 'description' in jmetadata:
            metadata['description'] = jmetadata['description']
        metadata['tags'] = ','.join(tags + categories)
        if categories:
            metadata['category'] = categories[0]
        return metadata

    def _import_content(self, path, content):
        def replace_teaser_mark(content):
            REGEX_TEASER_MD = r'<!--\s*more\s*-->'
            REGEX_TEASER = r'..\s+more'
            if is_html(path):
                regex = REGEX_TEASER_MD
                repl = '<!-- TEASER_END -->'
            else:
                regex = REGEX_TEASER
                repl = '.. TEASER_END'
            return re.sub(
                regex,
                repl,
                content,
                count=1,
            )

        def replace_code(content):
            def code_surround(lang, code):
                return '.. code::%s\n%s' % (
                    ' %s' % lang if lang else '',
                    '\n'.join(('    ' + s if s.strip() else '')
                              for s in code.splitlines())
                )

            def code_repl(matchobj):
                lang = matchobj.group('lang')
                code = matchobj.group('code')
                return code_surround(lang, code)
            REGEX_CODE = (
                r'\{%\s*highlight\s*(?P<lang>\w+)?'
                r'(?P<props>\s*(?:linenos|linenos=\w+|hl_lines|hl_lines=\S+))*\s*%\}'
                r'(?P<code>.*?)'
                r'\{%\s*endhighlight\s*%\}'
            )
            return re.sub(REGEX_CODE, code_repl, content,
                          flags=re.MULTILINE | re.DOTALL)

        def replace_links(content):
            def link_repl(matchobj):
                url = matchobj.group('url')
                slug = slugify_file(url)
                return 'link://slug/{0}'.format(slug)
            REGEX_LINK = (
                r'{%' r'\s*'
                r'post_url' r'\s*'
                r'(?P<url>.*?)' r'\s*'
                r'%}'
            )
            return re.sub(REGEX_LINK, link_repl, content)

        for repl in (replace_code, replace_links, replace_teaser_mark):
            content = repl(content)
        return content


def slugify_file(filename):
    name, _ = os.path.splitext(os.path.basename(filename))
    m = re.match('\d+\-\d+\-\d+\-(?P<name>.*)', name)
    if m:
        name = m.group('name')

    if not isinstance(name, utils.unicode_str):
        name = name.decode('unicode-escape')
    return utils.slugify(name)


def is_html(path):
    return path.lower().endswith(('.md', '.markdown', '.html'))


def is_textile(path):
    return path.lower().endswith(('.textile', ))
