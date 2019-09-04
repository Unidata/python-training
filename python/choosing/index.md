---
title: Where to Get Python 
---

While it's possible to install Python directly from [python.org](https://wiki.python.org/moin/BeginnersGuide/Download),
we recommend using [Conda](http://conda.pydata.org/docs/index.html) instead.
Conda is a package management system, from ContinuumIO, created specifically to
assist working with Python packages in a cross-platform fashion. Its real
strength comes in handling Python packages which require compiled code--such
packages are especially prevalent in the scientific Python ecosystem.

Conda also has the concept of an environment, which is an independent,
self-contained install of Python and packages. These environments make it easy
to install different versions of Python side-by-side; this is especially useful
when trying to test libraries on a variety of different Python versions. Other
applications of environments:
* Keeping a static install of Python with a known working set of packages for a
  particular project (e.g. journal article or thesis)
* A disposable environment for testing a new library without polluting the rest
  of the Python install; this environment can easily be discarded when no
  longer needed
* Quick set up of a known set of libraries and programs for workshops and tutorials

## Anaconda vs. Miniconda
There are two options for getting Conda:
[Anaconda](https://www.anaconda.com/distribution/) and
[miniconda](https://conda.io/en/latest/miniconda.html). Anaconda is a full
distribution of Python, and comes with over 150 packages in the download;
consequently, this download is over 3GB. Anaconda is good if you want to have
many packages downloaded and available in one shot; this is especially useful
if you know you'll be working offline for awhile. Miniconda contains only
Python and other libraries needed to run Conda itself; other packages will be
downloaded and installed as requested. For more information, see
[here](https://conda.io/en/latest/miniconda.html).

## Python 2 vs. 3
In 2008, the core Python development team released Python 3.0; the goal of that
release was to clean up a variety of issues with Python 2.x without worrying
about complete backwards compatibility. At this point in time, Python 3.x
represents the actively developed version of Python, with the 2.x series now
"legacy", only seeing bug fixes. For scientific use, all major packages support
Python 3. For information about what's new in Python 3, there are a variety of
resources:

- [Official Python Docs](https://docs.python.org/3/whatsnew/)
- Lexy Munroe's Detailed [Why should I use Python 3?](https://eev.ee/blog/2016/07/31/python-faq-why-should-i-use-python-3/)
- [Nick Coghlan's (core Python developer) Python Notes](http://python-notes.curiousefficiency.org/en/latest/python3/index.html)
- [Brett Cannon's (another core developer) Blog](http://www.snarky.ca/why-python-3-exists)

Our recommendation is to use Python 3 installed through Miniconda. All of the
subsequent materials here will assume the use of Python 3; however, the use
of features available **only** in Python 3 will be minimal (*if any*).
