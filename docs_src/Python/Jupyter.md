---
title: IPython / Jupyter Cheatsheet
category: python
tags:
---
### [IPython]( http://ipython.org/ ) / [Jupyter](http://jupyter.org/)

- Using IPython makes interactive work easy.
    - Better shell
    - Notebook interface
    - Embeddable kernel
    - Parallel python

### IPython shell shortcuts

- TAB expansion to complete python names and file paths
- ~ and * directory / file expansion
- many "magic" methods:

```
%lsmagic                # list of all magic methods
%quickref               # cheatsheet
%magic
```

### Help

```
?                       # overall help
help                    # python help system
?someobj or someobj?    # help
??someobj or someobj??  # detailed help
```

``%pdoc`` ``%pdef`` ``%psource``  for docstring, function definition, source code only.

### Run

To run a program directly from the IPython console:

```
%run somescript.py      # instead of execfile("somescript.py") at the python prompt
```

``%run`` has special flags for timing the execution of your scripts (``-t``) or for running them under the control of either Python's pdb debugger (``-d``) or profiler (``-p``):

```
%run -d myscript.py
```

### Other Commands

```
%edit %ed               # edit then execute
%save
%load example.py        # load local (example) file (or url) allowing modification
%load http://matplotlib.org/plot_directive/mpl_examples/mplot3d/contour3d_demo.py
%macro                  # define macro with range of history lines, filenames or string objects
%recall

%whos                   # list identifiers you have defined interactively
%reset  -f -s           # remove objects -f for force -s for soft (leaves history).
```

- ```%reset``` is not a kernel restart
- Restart with ``Ctrl+.`` in "qtconsole"
- ``import module ; reload(module)`` to reload a module from disk

### Debugging

```
%debug                  # jump into the Python debugger (pdb)
%pdb                    # start the debugger on any uncaught exception.

%cd                     # change directory
%pwd                    # print working directory
%env                    # OS environment variables
```

### OS Commands

```
!OScommand
!ping www.bbc.co.uk
%alias                  # system command alias
```

### History

```
_ __ ___                # etc... for previous outputs.
_i _ii _i4              # etc.. for previous input. _ih for list of previous inputs
```

### GUI integration

Start with ``ipython --gui=qt`` or at the IPython prompt:

```
%gui wx
```

Arguments can be ``wx``, ``qt``, ``gtk`` and ``tk``.

### Matplotlib / pylab graphics in an iPython shell

Start with: ``ipython --matplotlib`` ( or ``--matplotlib=qt`` etc...)

At the IPython prompt:

```
%matplotlib             # set matplotlib to work interactively; does not import anythig
%matplotlib  inline
%matplotlib qt          # request a specific GUI backend
%pylab inline
```

``%pylab`` makes the following imports:

```python
import numpy
import matplotlib
from matplotlib import pylab, mlab, pyplot
np = numpy
plt = pyplot
from IPython.display import display
from IPython.core.pylabtools import figsize, getfigs
from pylab import *
from numpy import *
```

### [Qtconsole - an improved console]( http://ipython.org/ipython-doc/stable/interactive/qtconsole.html )

At the command prompt:

```
ipython.exe qtconsole --pylab=inline --ConsoleWidget.font_size=10
```

alternative: --matplotlib inline
or within IPython:

```
%matplotlib  inline
%pylab inline
```

To embed plots, SVG or HTML in qtconsole, call display:

```
from IPython.core.display import display, display_html
from IPython.core.display import display_png, display_svg
display(plt.gcf()) # embeds the current figure in the qtconsole
display(*getfigs()) # embeds all active figures in the qtconsole
#or:
f = plt.figure()
plt.plot(np.rand(100))
display(f)
```

[ipython and ipython notebook for matlab users]( http://xcorr.net/2013/04/19/ipython-and-ipython-notebook-for-matlab-users/ )

### IPython Notebook web-based interface

- Start with: ipython notebook and switch to browser
- Keyboard shortcuts:
    - ``Enter`` to edit a cell
    - ``Shift + Enter`` to evaluate
    - ``Ctrl + m`` or ``Esc`` for the "command mode"

In command mode:

     h list of keyboard shortcuts
     1-6 to convert to heading cell
     m to convert to markdown cell
     y to convert to code
     c copy / v paste
     d d delete cell
     s save notebook
     . to restart kernel
