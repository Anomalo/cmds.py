from pprint import *
import os
import sys
import glob
import __main__ as main


def read(f):
        #reads the file and returns a list of parsed commands
        f = open(f,'r')
        txt = f.read()
        #gets rid of tabs
        txt = txt.replace('\t','')
        cmds = txt.splitlines()
        CMDS = []
        #gets rid of comments
        for cmd in cmds:
                CMD = cmd.split('\x23')[0]
                if CMD == '':
                        CMD = '\x23'
                CMDS.append(CMD)
        cmds = CMDS
        #separates commands
        TXT = ''.join(CMDS)
        CMDS = TXT.split('\x23')
        for i in range(CMDS.count('')):
                CMDS.remove('')
        return(CMDS)


def show(f):
        #prints the commands in the file
        n=1
        for line in read(f):

                print n,')\n', line,'\n'*2
                n+=1
def run():
        #run the commands in the file
        cmds = read()
        for cmd in cmds:
                print cmd
                os.system(cmd)


def seeAll():
        #print the commands of all .cmd files in the directort
        os.system('clear')
        files = glob.glob('*.cmd')
        for f in files:
                print f
                show(f)


arg = sys.argv[-1]

if arg == (main.__file__):
        seeAll()
else:
        show(arg)

