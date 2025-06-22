#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import subprocess


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


def message_yellow(message:str) -> str:
  return '\033[33m' + message + '\033[0m'


def message_red(message:str) -> str:
  return '\033[31m' + message + '\033[0m'


##
