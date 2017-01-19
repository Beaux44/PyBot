from py_compile import compile as pyc # imports py_compile.compile() and names it "pyc"

from os import rename as move # imports os.rename() and names it move, because even though it is called "rename," it is just moving the file

from os import remove as rem # imports  os.remove() and names it "rem"

from time import sleep as t # imports time.sleep() and names it "t"

from os.path import dirname as fpath # imports os.path.dirname() and names it "fpath"

from os.path import realpath as rpath # imports os.path.realpath() and names it "rpath"

from sys import exit as quit # imports sys.exit() and names it "quit"

# this is used to find the directory this file is in, it is later used
# to move the other files to "/release/file.pyc," I just hadn't wanted
# clutter in the building directory. (These notes are for the
# "path = fpath(rpath(__file__))" bit below this note, I know it's  bit lengthy)
path = fpath(rpath(__file__))

# these make a .pyc version of all these files
pyc("Read.py")
pyc("Settings.py")
pyc("Socket.py")
pyc("Commands.py")
pyc("Run.py")
pyc("Threads.py")

try: # if the file does not exist, it will bring up an error
    # these remove the current file because on windows,
    # moving a file to another file's directory even if they
    # are the same file, brings up an error.
    rem(path + "/release/Read.pyc")
    rem(path + "/release/Settings.pyc")
    rem(path + "/release/Socket.pyc")
    rem(path + "/release/Commands.pyc")
    rem(path + "/release/Run.pyc")
    rem(path + "/release/Threads.pyc")

except:
    t(.5) # waits half a second (to let the HDD remove the .pyc files)
    # moves the .pyc in the building directory to the release directory
    move("Read.pyc", path + "/release/Read.pyc")
    move("Settings.pyc", path + "/release/Settings.pyc")
    move("Socket.pyc", path + "/release/Socket.pyc")
    move("Commands.pyc", path + "/release/Commands.pyc")
    move("Run.pyc", path + "/release/Run.pyc")
    move("Threads.pyc", path + "/release/Threads.pyc")
    quit() # exits the program

#identical to the except block
t(.5)
move("Read.pyc", path + "/release/Read.pyc")
move("Settings.pyc", path + "/release/Settings.pyc")
move("Socket.pyc", path + "/release/Socket.pyc")
move("Commands.pyc", path + "/release/Commands.pyc")
move("Run.pyc", path + "/release/Run.pyc")
move("Threads.pyc", path + "/release/Threads.pyc")
