#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
import subprocess
import argparse


#
#
#

def subprocess_check_output(_exec_args:list):
  try:
    # raise ValueError()
    return subprocess.check_output(_exec_args, encoding='utf-8')
  except:
    subprocess_error_message('subprocess.check_output', _exec_args)
    sys.exit()


def subprocess_run(_exec_args:list):
  try:
    # raise ValueError()
    return subprocess.run(_exec_args, encoding='utf-8')
  except:
    subprocess_error_message('subprocess.run', _exec_args)
    sys.exit()


def subprocess_error_message(message:str, _exec_args:list):
  print('\033[31m' + 'Something wrong: ' + message + '\033[0m')
  print('\033[31m' + str(_exec_args) + '\033[0m')


#
#
#

def message_yellow(message:str) -> str:
  return '\033[33m' + message + '\033[0m'


def message_red(message:str) -> str:
  return '\033[31m' + message + '\033[0m'


#
#
#

def get_abs_file_path(value: str | None) -> str:
  return os.path.abspath(value)


def check_file_existence(value: str) -> str:
  is_file = os.path.isfile(value)

  if not is_file:
    raise argparse.ArgumentTypeError(message_red(
      f"Non-existent file: {value}"
    ))
  return get_abs_file_path(value)


##
