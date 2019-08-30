.. title: Installation Guide for the Unidata Example Gallery
.. slug: installation
.. date: 2019-07-29 14:37:54 UTC-06:00
.. tags: python example meteorology atmospheric science unidata installation
.. category:
.. link:
.. description:

This gallery provides a great set of examples and starting points for your
projects. We have an environment file to make running these examples easier.
To get started, you can setup your environment following these steps:

Video-Based Instructions
------------------------

Mac/Linux
~~~~~~~~~
.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/lmAulLlXNOc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Windows
~~~~~~~
.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/5DFDXKzqkrU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Installing Conda
----------------
Head over to `conda.io/miniconda.html <https://conda.io/miniconda.html>`_ and
download the miniconda installer for your operating system. You'll want the
Python 3.X version. **Windows 32-bit machines are NOT supported by most
packages and cannot be used.**

Windows
~~~~~~~
* After downloading the installer, open it and click through the graphical
  install utility. Accept all of the default installation settings.
* You should now have a program called "Anaconda Prompt" installed. Open it
  (this will be your Python command prompt).

Mac/Linux
~~~~~~~~~
* After downloading the bash installer, open a command prompt (terminal program
  on the Mac).
* Change the directory at the terminal to wherever the installer was downloaded.
  On most systems, this will default to the downloads directory in your user
  account. If that's the case, `cd ~/Downloads` will get you there, or replace
  the path with wherever you saved the file.
* Run the installer script by typing `bash Miniconda3-latest-MacOSX-x86_64.sh`.
* Note: Your file name may be different depending upon your operating system!
  replace Miniconda3-latest-MacOSX-x86_64.sh with whatever the name of the file
  you downloaded was.
* Accept the defaults.
* After the installer has completed completely close and restart your terminal
  program (this sources the newly modified path).
* Verify that your install is working by typing `conda --version` into the terminal.
  You should see a response like `conda 4.5.11` or similar (though yours may be a
  different version number).

Setting up the environment
--------------------------
* We'll be using conda environments for the workshop (again, we'll explain more
  during the course or checkout `this MetPy Monday <https://www.youtube.com/watch?v=15DNH25UCi0>`_
  if you can't wait). After installing conda, open a terminal (or the Anaconda Prompt
  if you're on a Windows machine).
* Download the `environment.yml` file that will tell your system what all we need for the
  workshop. Note where you download it, this will be the `Downloads` directory by default on
  most systems, which is fine. Right click and "save"
  `this link <https://raw.githubusercontent.com/Unidata/python-gallery/master/environment.yml>`_
  to download.
* Open a terminal (Anaconda prompt on Windows) and navigate to whatever directory the `environment.yml`
  file was saved in. Generally `cd ~/Downloads`.
* Run the command `conda env create` and wait for the installation to finish.
* Run the command `conda activate gallery` to activate the unidata environment and
  verify that everything is ready.

Running an example
------------------
* Find the example you wish to run and download the example as a python script
  or jupyter notebook, depending on how you wish to run it.
* Ensure that the `gallery` environment is activated.
* If you are running the example as a script, run `python the_script_name.py`
* If you are running the example as a notebook start the jupyter environment
  with `jupyter notebook` or `jupyter lab`
* When you want to return to the root environment, run the command `conda deactivate`
  to exit the `gallery` environment.

Contact Us
----------

* For questions and discussion, join Unidata's python-users_
  mailing list
* To submit questions to Unidata developers, `email us`_!

.. _python-users: https://www.unidata.ucar.edu/support/#mailinglists
.. _email us: support-python@unidata.ucar.edu

Related Projects
----------------

* MetPy_ is a Python toolkit for meteorology
* netCDF4-python_ is the officially blessed Python API for netCDF_
* siphon_ is an API for accessing remote data on `THREDDS Data Server`__

.. _MetPy: https://unidata.github.io/MetPy
.. _netCDF4-python: https://unidata.github.io/netcdf4-python/
.. _netCDF: https://www.unidata.ucar.edu/software/netcdf/
.. _siphon: https://unidata.github.io/siphon
__ https://www.unidata.ucar.edu/software/thredds/current/tds/