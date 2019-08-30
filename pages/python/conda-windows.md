---
title: Getting Going with Python on a Windows
---

The aim of this web page is to help you get started with Python on Windows. We will explain what a package management tool is, how to download `conda` package management tool via the Anaconda installer, and guide you on the Windows Command Prompt so that you can use `conda` from the command line. Finally, we will wrap up by installing one library with `conda`.

## What Is a Package Management Tool?

A package management tool is a software application that helps you manage software libraries that enable you to get your work done. These software libraries may relate to plotting for scientific publication or accessing certain kinds of data, for example.

When you start using Python, you will want use software libraries that are not part of the standard Python installation. For example, you may wish to use the [Unidata metpy library](https://pypi.python.org/pypi/MetPy) for meteorological data and visualization. Anaconda from Continuum Analytics will help you install `metpy` easily.

## Installing the `conda` Package Management Tool

The `conda` package management tool is part of the Anaconda software package. Install `conda` by navigating to the [Anaconda download page](https://www.anaconda.com/distribution/). Scroll down to the "Anaconda for Windows" portion of the web page.

Download the Python 3.5 version by clicking on the "Windows 64 bit Graphical Installer" link. It is a big download, so it is best to be on fast network. Open the installer file you just downloaded. It should be named something like `Anaconda[version]-Windows-x86_64`.

This action will guide you through the [conda installation on Windows](https://docs.continuum.io/anaconda/install#anaconda-for-windows-install). The last step of the installation process will ask you if you want to add Anaconda to my the PATH environment variable. Ensure this option is checked.

## Windows Command Prompt

The Windows Command Prompt is a software program that gives you the ability to give text based instructions to your computer. 

To open the Windows Command Prompt, left-click on the Windows Start menu located in the lower left portion  of the desktop and search for 'Command Prompt' in the search box located at the bottom of the menu.

In the Windows Command Prompt, you will see some text such as **`C:\Users\Jane>`**. This is known as the **command line**. The command line is where you give text instructions to your computer.

## Interacting with `conda`

Let's make sure conda is installed by entering this instruction on the command line:

    conda list

yields

    # packages in environment at C:\Users\Jane\AppData\Local\Continuum\Anaconda3:
    #
    alabaster                 0.7.7                    py35_0  
    anaconda                  4.0.0               np110py35_0  
    anaconda-client           1.4.0                    py35_0  
    ...
    numexpr                   2.5                 np110py35_0  
    numpy                     1.10.4                   py35_0  
    odo                       0.4.2                    py35_0  
    ...
    yaml                      0.1.6                         0  
    zeromq                    4.1.3                         0  
    zlib                      1.2.8                         0

which will list linked packages in a conda environment. You’ll notice libraries such as the scientific computing library [numpy](http://www.numpy.org/) that you will probably be making use of.

## Getting Our Feet Wet by Installing Metpy with `conda`

We first have to give `conda` an instruction on where to find `metpy` on the `conda-forge` channel.

    conda config --add channels conda-forge

We can now install `metpy`:

    conda install metpy

Let's verify we installed `metpy` with the following command:

    conda list

should yield amongst other libraries:

    # packages in environment at /Users/chastang/anaconda:
    #
    ...
    metpy                     0.3.0                    py35_1    conda-forge
    ...

## In Summary

You have just learned how to:

-   Download `conda`
-   Install `conda`
-   Installed the `metpy` library with `conda`

In future installments of the Unidata Online Python training, we will be using `conda` to install various libraries.
