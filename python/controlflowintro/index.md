---
title: Control Flow
---

Control flow concerns how programs proceed in their execution to arrive a desired outcome. Often times, we write programs to make decisions based on certain **conditions** such as input from the user or values in the data. Different conditions lead to a variety scenarios. Programs can make choices concerning meteorological conditions such as wind velocity. Consider a Python program that draws wind barbs on a map. It will have to take actions depending on the velocity of the wind data. The program will have to draw a flag for winds of greater than 47 knots but only one barb for 10 knot winds.

In addition, control flow can also concern a program repeatedly executing a set of statements while proceeding through a list of values or while some condition has not yet been met. A rawinsonde may send data until a certain pressure level has been attained, for example.

Control flow can be complex and programmers must learn to manage that complexity and keep it in check in order to write programs that can be understood by others and maintained in the long term. One way of managing that complexity is by delegating the control flow to **functions** to get a specific task done (e.g., unit conversion). Functions make code more readable, and easier to maintain as well as create units of reusable code that can be used in other parts of your program or in different programs.

In this section, we will examine three Jupyter notebooks on control flow: one that examines [conditional statements](http://nbviewer.jupyter.org/github/Unidata/online-python-training/blob/master/notebooks/Conditionals.ipynb), one that makes use of [loops](http://nbviewer.jupyter.org/github/Unidata/online-python-training/blob/master/notebooks/Loops.ipynb), and finally a notebook that employs [functions](http://nbviewer.jupyter.org/github/Unidata/online-python-training/blob/master/notebooks/Functions.ipynb) to improve the readability and reuse of code.
