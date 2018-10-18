@echo off


SET DIR=App-appmon
rd %DIR% /s /q
c:\Python27\python c:\Python27\Scripts\cxfreeze --base-name=Win32GUI -OO -c -s --icon=hmon.ico --install-dir=%DIR% appmon.py
:c:\Python27\python c:\Python27\Scripts\cxfreeze --base-name=Console -OO -c -s --icon=hmon.ico --install-dir=%DIR% appmon.py

copy *.cnf %DIR%\

del %DIR%\tcl*.*
del %DIR%\tk*.*
rd /s /q %DIR%\tcl
rd /s /q %DIR%\tk


pause

