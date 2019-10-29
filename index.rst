.. title: The Unidata Python Training Site
.. slug: index
.. date: 2019-07-26 14:38:34 UTC-06:00
.. tags: atmospheric science python meteorology training examples gallery
.. category: 
.. link: 
.. description: A one-stop shop for Python in atmospheric science and meteorology
.. type: text

Welcome to Unidata's Python Training Site for atmospheric science and meteorology. This site is meant
to be a one-stop website for learning how to use Python for earth-science education and research
for any experience level. New Python users may find the :doc:`Introduction to Python <intro-to-python>`
section a good place to start. Check out the :doc:`Example Gallery <gallery-home>` for detailed meteorology-specific
examples, or learn advanced usage of the scientific Python ecosystem for atmospheric science with our
:doc:`workshop materials <workshop-intro>`. If you have questions, please contact the Unidata Python team
at our `support email`_.

.. _`support email`: support-python@unidata.ucar.edu

.. class:: jumbotron-fluid

   .. admonition:: Introduction to Python

    New to Python? Learn the basics of this powerful programming language and see how
    you can use it for atmospheric science education and research.

    .. raw:: html

       <a href="/python/intro-to-python" class="btn btn-primary btn-lg">Start learning!</a>


.. class:: jumbotron-fluid

   .. admonition:: Example Gallery

    Looking for examples of how to use MetPy, Siphon, Xarray, Pandas, or other useful Python packages
    with your meteorological data? Check out our example gallery for ideas on how to analyze
    and visualize your data!

    .. raw:: html

       <a href="/gallery/gallery-home" class="btn btn-primary btn-lg">Check out the gallery</a>

.. class:: jumbotron-fluid

   .. admonition:: Python Workshop Material

    Would you like to work through advanced examples of the scientific Python ecosystem,
    along with detailed visualizations of meteorological data? Work through our workshop
    notebooks at your own pace, or come back to the material after attending on of our
    in-person workshops.

    .. raw:: html

       <a href="/workshop/workshop-intro" class="btn btn-primary btn-lg">Start the workshop</a>

Contributing
------------

Have an example of how you use Python for atmospheric science research or education? Share it with
the community by contributing it to our gallery. Confused about something you read here? Add more
documentation where you find it lacking! Check out our `contributor's guide <contributing>`_
for information on how to help build this site!

Installation Instructions
-------------------------

To set up the Python environment used in the notebooks contained in this repository, follow
these instructions:

1. `Install Miniconda (Python 3.7) from Continuum Analytics <http://conda.pydata.org/miniconda.html>`_.
`Determine if your OS 32 or 64 bit <http://www.akaipro.com/kb/article/1616#os_32_or_64_bit>`_.

2. Once Miniconda is installed, from the command line (e.g., OS X terminal,
cmd.exe), run these instructions to clone the repository and create the environment:

.. code-block::

    git clone https://github.com/Unidata/python-training

    cd python-gallery

    conda env create -f environment.yml

From a Unix command line (e.g., OS X terminal)
If your default shell is NOT bash, first type `bash`.
To activate or switch to a conda environment, you can `conda activate
<environment>`. For example,

.. code-block::

    conda activate training

To switch and/or deactivate environments:

.. code-block::

    conda deactivate
    conda activate <environment>

From a Windows command line (e.g., cmd.exe)

To activate or switch to a conda environment, you can `activate
<environment>`. For example,

.. code-block::

    activate training

To switch and/or deactivate environments:

.. code-block::

    deactivate
    activate <environment>
