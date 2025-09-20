#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The size of each image is assumed to be Full HD, 1920x1080
"""

import os
import sys
import argparse
import glob
import tempfile
import shutil


from _functions.common_function import (
  subprocess_check_output,
  subprocess_run,
  subprocess_error_message,
  message_yellow,
  message_red,
)

from _functions.tiles4 import create_tiles4
from _functions.tiles5 import create_tiles5
from _functions.tiles6 import create_tiles6
from _functions.landscape_or_portrait import create_landscape_or_portrait


if __name__ == "__main__":

  #
  # Handling arguments
  #

  parser = argparse.ArgumentParser(
    formatter_class = argparse.RawDescriptionHelpFormatter,
    description = message_yellow('Arrange image files in tiles.'))

  parser.add_argument('input_files',
    nargs = '+',
    metavar = 'Input files',
    help = message_yellow('Input image files'))
  parser.add_argument('output_file',
    metavar = 'Output file',
    help = message_yellow('Output image file'))

  parser.add_argument('-tt', '--tyling_type',
    choices = [ 'landscape', 'portrait', '4tiles', '5tiles', '6tiles',],
    help = message_yellow('Tyling type'))
  parser.add_argument('-gs', '--gap_size',
    default = 10,
    type = int,
    help = message_yellow('Spacing between images'))
  parser.add_argument('-gc', '--gap_color',
    default = '#00000000',
    type = str,
    help = message_yellow('Spacing between images'))

  parser.add_argument('-di', '--direction',
    default = 'NW',
    choices = ['NW', 'NE', 'SE', 'SW'],
    type = str,
    help = message_yellow('Direction, NW(default), NE, SE, SW, valid only when the argument is 5tiles or 6tiles, ignored otherwise'))

  args = parser.parse_args()


  #
  # Check file's width and height
  #

  dic_size = {
    'height': -1,
    'width': -1,
  }

  for in_file in args.input_files:
    ret = subprocess_check_output([
        'identify', '-format', '%w %h', in_file
      ])

    if -1 == dic_size['width'] and -1 == dic_size['height']:
      dic_size['width'] = ret.split(' ')[0]
      dic_size['height'] = ret.split(' ')[1]

    else:
      tmp_flg = True
      if 'landscape' == args.tyling_type:
        if dic_size['height'] != ret.split(' ')[1]:
          tmp_flg = False
      elif 'portrait' == args.tyling_type:
        if dic_size['width'] != ret.split(' ')[0]:
          tmp_flg = False
      else:
        if dic_size['width'] != ret.split(' ')[0] or dic_size['height'] != ret.split(' ')[1]:
          tmp_flg = False

      if True == tmp_flg:
        print(message_yellow('Image files\' size are no probrem: ' + os.path.basename(in_file)))
      else:
        print(message_red(
          '%s: %sx%s, %sx%s' % (
            in_file, str(ret.split(' ')[0]), str(ret.split(' ')[1]), str(dic_size['width']), str(dic_size['height'])
          )
        ))
        sys.exit()


  #
  #
  #

  temp_dir = tempfile.mkdtemp(prefix = 'create_tiles_')

  if '6tiles' == args.tyling_type:
    create_tiles6(args, temp_dir, dic_size)

  elif '5tiles' == args.tyling_type:
    create_tiles5(args, temp_dir, dic_size)

  elif '4tiles' == args.tyling_type:
    create_tiles4(args, temp_dir, dic_size)

  elif 'landscape' == args.tyling_type or 'portrait' == args.tyling_type:
    create_landscape_or_portrait(args, temp_dir, dic_size)


  #
  #
  #

  shutil.rmtree(temp_dir)


  #
  #
  #

  sys.exit()
