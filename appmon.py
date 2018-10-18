'''

    Monitor program used to start and restart
    a list of tasks defined in a config file.

    If this script runs under pythonw,
    it will not show a title in windows taskbar.

    (Emulate same behaviour as hstart.exe)

    Any python script with no GUI and running under pythonw.exe
    will not show a title in windows taskbar.

'''

DEBUG = 0

import os
import sys
import time
import datetime
import threading
import subprocess

py   = sys.version_info
py3k = py >= (3, 0, 0)

if py3k:
    from configparser import ConfigParser
else:
    from ConfigParser import ConfigParser

def log(task_description, msg):
    filename = '{}.log'.format(task_description)
    now = datetime.datetime.now().strftime('%d-%b-%Y %H:%M')
    with open(filename, 'at') as f:
        f.write('{} - {}\n'.format(now, msg))

def task(task_description, d_env):
    '''
        Run in a thread.
        Log the activity.
        Chdir, start a program, wait finish execution, delay, then restart.
    '''
    cmd = d_env.get('RUNCMD')
    d_env.update(os.environ) #some apps (like pygtk) read PATH from env
    os.chdir(d_env.get('WORK_FOLDER', os.getcwd()))
    if not cmd:
        log(task_description, 'No RUNCMD defined.')
        return
    log(task_description, 'Start: {}'.format(cmd))
    cnt = 0
    if DEBUG:
        print ('Start: {}'.format(cmd))
    while True:
        d_env['ReStarted'] = str(cnt)
        try:
            p = subprocess.Popen(cmd, env=d_env)
            p.wait()
        except Exception as ex:
            if DEBUG:
                print ('Error task "{}": {}:'.format(task_description, ex))
            log(task_description, 'Error: {}'.format(ex))
            break
        if DEBUG:
            print ('Restart: {}'.format(cmd))
        cnt += 1
        log(task_description, 'Restart #{}'.format(cnt))
        time.sleep(float(d_env.get('RESTART_WAIT', 0)))

def main():
    #
    config = ConfigParser()
    if len(sys.argv) > 1:
        config.read(sys.argv[1])
    else:
        config.read("startup.cnf")
    if 0:
        print('Config:')
        for section_name in config.sections():
            print ('Section: {}'.format(section_name))
            print ('  Options: {}'.format(config.options(section_name)))
            for name, value in config.items(section_name):
                print ('  {} = {}'.format(name, value))
            print('\n')
    else:
        for section_name in config.sections():
            if DEBUG:
                print(section_name)
            d_env = {}
            for name, value in config.items(section_name):
                d_env[name.upper()] = value
                if DEBUG:
                    print ('  {} = {}'.format(name.upper(), value))
            t = threading.Thread(target=task, kwargs=dict(
                task_description=section_name, d_env=d_env))
            t.daemon = True #when main ends, all tasks ends
            t.start()
            #delay between starts
            time.sleep(1)
            if DEBUG:
                print ('='*30)
    while True:
        #no need if t.daemon = False
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print (ex)
    msg = "Press Enter to exit."
    if py3k:
        input(msg)
    else:
        raw_input(msg)

