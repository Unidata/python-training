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

############
Contributing
############

Have an example of how you use Python for atmospheric science research or education? Share it with
the community by contributing it to our gallery. Confused about something you read here? Add more
documentation where you find it lacking! Check out our `contributor's guide <contributing>`_
for information on how to help build this site!

#########################
Installation Instructions
#########################

Installation consists of getting Conda (what you'll use to manage your Python installation and packages),
getting the workshop materials, then creating a copy of the environment we've created that contains the
useful packages you'll need to follow along with the materials and do much of your domain specific work.
If you're unfamiliar with conda, plan on dedicating about 30 minutes to this process. If you are attending
and in-person workshop we ask that you complete the installation steps before arriving at the workshop or
arrive slightly early for help so we may begin on time. You are also welcome to contact our Python team
at any time with issues you encounter!

****************
Installing Conda
****************

Conda is a great way to manage multiple environments (think sandboxes to work in, but more on that later).
It also makes managing all of the Python packages you'll be using much easier than handling it all yourself.

Windows
=======
* Download the Miniconda installer for Python 3.X `here <http://conda.pydata.org/miniconda.html>`_.
  **Windows 32-bit machines are NOT supported by most packages and cannot be used.**
* After downloading the installer, open it and click through the graphical install utility.
  Accept all of the default installation settings.
* You should now have a program called “Anaconda Prompt” installed. Open it
  (this will be your Python command prompt).

Mac/Linux
=========
* After downloading the bash installer, open a command prompt (terminal program on the Mac).
* Change the directory at the terminal to wherever the installer was downloaded. On most systems,
  this will default to the downloads directory in your user account. If that’s the case, :code:`cd ~/Downloads`
  will get you there, or replace the path with wherever you saved the file.
* Run the installer script by typing :code:`bash Miniconda3-latest-MacOSX-x86_64.sh`.
  Note: Your file name may be different depending upon your operating system! replace Miniconda3-latest-MacOSX-x86_64.sh
  with whatever the name of the file you downloaded was.
* Accept the defaults.
* After the installer has completed completely close and restart your terminal program (this sources the newly modified path).
* If bash isn't your default shell, switch to it by running the command :code:`bash`.
* Verify that your install is working by running :code:`conda --version`.
  You should see a response like conda 4.8.0 or similar (though yours may be a slightly different version number).

*********************
Setup the Environment
*********************

Environments are great ways to isolate your sandbox to work in of a given Python version, packages, etc. You'll
learn more about them later, but we'll need to create one that contains all of the useful packages used in these
materials. If you can't wait to learn more about environments, checkout this
`MetPy Monday video <https://www.youtube.com/watch?v=15DNH25UCi0>`_ on them.

* Open a terminal window (Anaconda Prompt if you're on Windows).
* Download the environment.yml file that tells your system what should be in the environment. Remember where you
  download this file! Most systems go in ~/Downloads by default which is fine. Right click and select "save" on
  `this link <https://raw.githubusercontent.com/Unidata/python-workshop/master/environment.yml>`_ to download the file.
* In the terminal, navigate to wherever this file saved, probably :code:`cd ~/Downloads` will get you there.
* Run the command :code:`conda env create` and wait for the installation to finish.
* Run the command :code:`conda activate training` to activate the unidata environment and verify that everything is ready.
* For an in-depth tutorial on conda and environments, check out this
  `Carpentry-style tutorial <https://kaust-vislab.github.io/introduction-to-conda-for-data-scientists/>`_.

*************************
Download Course Materials
*************************

There are two ways you can get the course materials: with git and as a ZIP file. If you're familiar with git or plan
on contributing to the content, then follow the git based instructions. Otherwise the ZIP file method is fine.

ZIP Download
============
* Head over to the GitHub page for the materials `here <https://github.com/unidata/python-training>`_.
* Click the green "Clone or download" button in the upper right section of the screen.
* Click "Download ZIP"
* Using an unzip utility (right click on the file in Windows), extract the contents and put them wherever you'd like
  your workshop materials to be.

Using git
=========
* Open a terminal/Anaconda prompt.
* cd into where you'd like the course materials to download.
* If you don't have git installed already you can do so with :code:`conda install git`.
* Clone the repository with :code:`git clone https://github.com/Unidata/python-training`.

*********************
Starting up Notebooks
*********************

It's a good idea to go ahead and try to start up the Jupyter Lab server to make sure your installation and materials download
was successful.

* Open a terminal/Anaconda Prompt.
* Activate the training environment we created with :code:`conda activate training`
* Change directory to the location you've placed your training materials :code:`cd ~/Desktop/python-training` or similar.
* Start jupyter lab by running the command :code:`jupyter lab`
* A browser should open and you're in jupyter lab!
* Explore some if you'd like, then close the browser.
* In the terminal/Anaconda Prompt hit :code:`ctrl + c` a few times until the prompt is back.
* Close your terminal/Anaconda Prompt.
