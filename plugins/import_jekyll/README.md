## Nikola Jekyll/Octopress importer

This plugin will do a quick import of your Jekyll or Octopress site.

To install it:

    $ nikola plugin -i import_jekyll


To use it:

    $ nikola import_jekyll your_jekyll_root_path


## How does it work?

It will translate your post metadata to the Nikola format, creating the `slug` and `date` if not present or cannot be taken from the file name. Teaser marks will be translated too.

It will try to create a directory structure similar to the one used in Jenkins.

In addition, `post_url` and `highlight` directives will be translated to Nikola format.
