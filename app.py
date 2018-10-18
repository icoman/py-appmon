#!/usr/bin/python

"""
    Sample PythonCard application
    used for py-appmon

    Install PythonCard from
    http://pythoncard.sourceforge.net/

"""


import os, time
import sys, traceback

import wx
from PythonCard import model, dialog, timer

class MyBackground(model.Background):

    def on_close(self, event):
        #self.MakeModal(False)
        self.Destroy()
        sys.exit(0)

    def on_initialize(self, event):
        try:
            msg = ' '.join(sys.argv[1:]) or 'No title'
            title = '{} pid={}'.format(msg, os.getpid())
            self.title = title
            self.components.titluapp.text = title
            
            self.flag_secunde = True
            self.myTimer = timer.Timer(self.components.textceas, -1) # create a timer
            self.myTimer.Start(500) # launch timer, to fire every x ms

            msg = ''
            for i in os.environ:
                N = 48
                value = os.environ[i]
                if len(value)>N:
                    value = '{}...'.format(value[:N])
                msg += '{} = {}\n'.format(i, value)
            self.components.envinfo.text = msg
        except Exception as ex:
            self.errDialog(ex)

    def errDialog(self, errmsg):
        err = traceback.format_exc()
        if len(err) < 6:
            err = ''
        msg = '{}\n\n{}'.format(errmsg, err)
        result = dialog.messageDialog(self, msg, 'Runtime error',wx.ICON_ERROR | wx.OK) #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL)
        self.panel.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))

    def on_textceas_timer(self, event):
        self.flag_secunde = not self.flag_secunde
        format = "%%H:%%M%c%%S" % (self.flag_secunde and ':' or ' ')
        s = time.strftime(format,time.localtime())
        self.components.textceas.text = s

    def on_iesire_command(self, event):
        self.close()

if __name__ == '__main__':
    app = model.Application(MyBackground)
    app.MainLoop()
