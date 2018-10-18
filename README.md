# Python App Monitor
A simple [Python](https://www.python.org/) application written 
for [Microsoft Windows](https://www.microsoft.com/en-us/windows) and 
used to start and restart a list of tasks defined in a config file.

In [Windows](https://www.microsoft.com/en-us/windows) any python script 
with no GUI (just console) and started under **pythonw.exe** will not show 
a title in windows taskbar.

This application is inspired by [hstart](https://www.ntwind.com/software/hstart.html) 
and [Erlang supervisor](http://erlang.org/doc/man/supervisor.html).

Start program from Windows Command Prompt using:
```bat
     start pythonw appmon.py config_file.cnf
``` 

A sample config file:

```ini

;
; A sample config file
;for starting two processes
;

[process one]
RUNCMD = c:\python27\pythonw some-app.py with some arguments
WORK_FOLDER = c:\some working folder for app one
;some environment vars
SCALE=5
IGNOREFACTOR=10
SAMPLES=500
;STEPS=64


[process two]
RUNCMD = c:\python27\pythonw some-app.py with some arguments
WORK_FOLDER = c:\some working folder for app two
;some environment vars
SCALE=5
IGNOREFACTOR=10
SAMPLES=500
;STEPS=64

```

The compiled version using [cx_freeze](https://pypi.org/project/cx_Freeze/) with **Win32GUI** also works, run **taskkill /f /im appmon.exe** to kill it.

No copyright specified.

Feel free to use this software for both personal and commercial.
