# Contributors Guide

Interested in sharing how you use Python in atmospheric science research or education? 
Have code from your research that you believe others will
find useful? Have a few minutes to tackle an issue? In this guide we will get you setup and
integrated into contributing to the Unidata Python Training Site!

## Introduction
First off, thank you for considering contributing to this training site. It is an open-source
project meant to be a resource for the community, useful for beginners to expert users of Python.
We welcome all contributions to enhance the resources available for the community.

Following these guidelines helps to communicate that you respect the time of the
developers managing and developing this open source project. In return, they
should reciprocate that respect in addressing your issue, assessing changes, and
helping you finalize your pull requests.

So, please take a few minutes to read through this guide and get setup for success with your
Python Training contributions. We're glad you're here!

## What Can I Do?
* Tackle any [issues](https://github.com/Unidata/python-training/issues) you wish! We have a special
  label for issues that beginners might want to try. Also have a look at if the issue is already 
  assigned to someone - this helps us make sure that work is not duplicated if the issue is already 
  being worked on by Unidata Staff.

* Contribute code you already have. It does not need to be perfect! We will help you clean
  things up, test it, etc.

* Make a tutorial or example of how to do something.

* Improve documentation that you find incomplete or troublesome.

* File a new issue if you run into problems!

## Ground Rules
The goal is to maintain a diverse community that's pleasant for everyone. Please
be considerate and respectful of others by following our
[code of conduct](https://github.com/Unidata/.github/blob/master/CODE_OF_CONDUCT.md).

Other items:

* Each pull request should consist of a logical collection of changes. You can
  include multiple bug fixes in a single pull request, but they should be related.
  For unrelated changes, please submit multiple pull requests.
* Do not commit changes to files that are irrelevant to your feature or bug fix
  (eg: .gitignore).
* Be willing to accept criticism and work on improving your code; we don't want
  to break other users' code, so care must be taken not to introduce bugs.
* Be aware that the pull request review process is not immediate, and is
  generally proportional to the size of the pull request.

## Reporting a bug
The easiest way to get involved is to report issues you encounter when using MetPy or by
requesting something you think is missing.

* Head over to the [issues](https://github.com/Unidata/MetPy/issues) page.
* Search to see if your issue already exists or has even been solved previously.
* If you indeed have a new issue or request, click the "New Issue" button.
* Fill in as much of the issue template as is relevant. Please be as specific as possible.
  Include the version of the code you were using, as well as what operating system you
  are running. If possible, include complete, minimal example code that reproduces the problem.

## Setting up your development environment
We recommend using the [conda](https://conda.io/docs/) package manager for your Python
environments. Our recommended setup for contributing is:

* Install [miniconda](https://docs.conda.io/en/latest/miniconda.html) on your system.
* Install git on your system if it is not already there (install XCode command line tools on
  a Mac or git bash on Windows)
* Login to your GitHub account and make a fork of the
  [MetPy repository](https://github.com/unidata/metpy/) by clicking the "Fork" button.
* Clone your fork of the MetPy repository (in terminal on Mac/Linux or git shell/
  GUI on Windows) in the location you'd like to keep it. We are partial to creating a
  ``git_repos`` directory in our home folder.
  ``git clone https://github.com/your-user-name/metpy.git``
* Navigate to that folder in the terminal or in Anaconda Prompt if you're on Windows.
  ``cd metpy``
* Connect your repository to the upstream (main project).
  ``git remote add unidata https://github.com/unidata/metpy.git``
* Create the development environment by running ``conda env create``. This will install
  all of the packages in the ``environment.yml`` file.
* Activate our new development environment ``source activate devel`` on Mac/Linux or
  ``activate devel`` on Windows.
* Make an editable install of MetPy by running ``pip install -e .``

Now you're all set! You have an environment called ``devel`` that you can work in. You'll need
to make sure to activate that environment next time you want to use it after closing the
terminal or your system. If you want to get back to the root environment, just run
``source deactivate`` (just ``deactivate`` on Windows).

## Pull Requests

The changes to the MetPy source (and documentation) should be made via GitHub pull requests
against ``master``, even for those with administration rights. While it's tempting to
make changes directly to ``master`` and push them up, it is better to make a pull request so
that others can give feedback. If nothing else, this gives a chance for the automated tests to
run on the PR. This can eliminate "brown paper bag" moments with buggy commits on the master
branch.

During the Pull Request process, before the final merge, it's a good idea to rebase the branch
and squash together smaller commits. It's not necessary to flatten the entire branch, but it
can be nice to eliminate small fixes and get the merge down to logically arranged commits. This
can also be used to hide sins from history--this is the only chance, since once it hits
``master``, it's there forever!

**Working on your first Pull Request?** You can learn how from this *free* video series
[How to Contribute to an Open Source Project on GitHub](https://egghead.io/courses/how-to-contribute-to-an-open-source-project-on-github), Aaron Meurer's [tutorial on the git workflow](https://www.asmeurer.com/git-workflow/), or the guide [“How to Contribute to Open Source"](https://opensource.guide/how-to-contribute/).

Commit the changes you made. Chris Beams has written a [guide](https://chris.beams.io/posts/git-commit/) on how to write good commit messages.

Push to your fork and [submit a pull request]( https://github.com/Unidata/python-training/compare/).
For the Pull Request to be accepted, you need to agree to the
Unidata Python Contributor License Agreement (CLA). This will be handled automatically
upon submission of a Pull Request. See [here](/CLA.md) for more
explanation and rationale behind the Python Training Site's CLA.

## Source Code
The Python Training Site's source code is located in the `pages/` directory in the root of the repository. Within
`pages/` are the main top-level subpackages of the training site:
- `python`: Introduction to Python, how to download from Anaconda, version control, and introductory notebooks
- `gallery`: Example gallery of atmospheric science workflows, as Jupyter notebooks
- `workshop`: The Unidata Python workshop materials 

## Documentation
Now that you've made your awesome contribution, it's time to tell the world how to use it.
Make sure that notebooks have appropriate markdown sections telling users what each block of
code does, or provide comments within the code to clarify specific calls. Generally, more
explanation is better!

You can build the documentation locally to see how your changes will look. 
* Within the repository and with your conda environment activated, type ``nikola build``.
This will build the pages and check to make sure links work.
* Enter ``nikola serve -b`` to see your changes in a browser!

## What happens after the pull request
You've make your changes, documented them, added some tests, and submitted a pull request.
What now?

### Automated Testing
First, our army of never sleeping robots will begin a series of automated checks.
The test suite, documentation, and more will be checked on various versions of Python
with current and legacy packages. Travis CI will run testing on Linux and Mac.
If you see a red mark by a service, something failed and clicking the "Details" link 
will give you more information. We're happy to help if you are stuck.

The robots can be difficult to satisfy, but they are there to help everyone write better code.
In some cases, there will be exceptions to their suggestions, but these are rare. If you make
changes to your code and push again, the tests will automatically run again.

### Code Review
At this point you're waiting on us. You should expect to hear at least a comment within a
couple of days. We may suggest some changes or improvements or alternatives.

Some things that will increase the chance that your pull request is accepted quickly:

* Write effective documentation.
* Write a [good commit message](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).

### Merging
Once we're all happy with the pull request, it's time for it to get merged in. Only the
maintainers can merge pull requests and you should never merge a pull request you have commits
on as it circumvents the code review. If this is your first or second pull request, we'll
likely help by rebasing and cleaning up the commit history for you. As your development skills
increase, we'll help you learn how to do this.


## More Questions?
If you're stuck somewhere or are interested in being a part of the community in
other ways, feel free to contact us:
* [Unidata's Python support address](mailto:support-python@unidata.ucar.edu)
* [python-users](https://www.unidata.ucar.edu/support/#mailinglists) mailing list

## Futher Reading
There are a ton of great resources out there on contributing to open source and on the
importance of writing tested and maintainable software.
* [GitHub's Contributing to Open Source Guide](https://guides.github.com/activities/contributing-to-open-source/)
* [Zen of Scientific Software Maintenance](https://jrleeman.github.io/ScientificSoftwareMaintenance/)