#!/usr/bin/python3
import os
from os.path import expanduser

def execute_in_dir(dirname):
  def execute_in_dir_decorator(callback):
    def decorated_callback(*args, **kw):
      cwd = os.getcwd()
      os.chdir(dirname)
      callback(*args, **kw)
      os.chdir(cwd)
    return decorated_callback
  return execute_in_dir_decorator

# say_what tells WHAT method is currently being executed
def say_what(callback):
  def decorated_callback(*args, **kw):
    print(f'Begin executing {callback.__name__}')
    callback(*args, **kw)
    print(f'Finished executing {callback.__name__}')
  return decorated_callback

def curdir():
  print(f'Current directory: {os.getcwd()} ')

@execute_in_dir(expanduser('~'))
@say_what
def do_something_in_home(arg1, arg2, kw1, kw2=44):
  curdir()
  print(f'arg1={arg1}, arg2={arg2}, kw1={kw1}, kw2={kw2}')

@execute_in_dir('/tmp')
@say_what
def do_something_in_tmp():
  curdir()

curdir()
do_something_in_home(1, 2, kw1=3)
curdir()
do_something_in_tmp()
curdir()