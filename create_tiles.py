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

  parser.add_argument('-i', '--input',
    nargs = '+',
    metavar = 'Input files, 2 to 6',
    required = True,
    type = str,
    help = message_yellow('Input image files'))

  parser.add_argument('-o', '--output',
    metavar = 'Output file',
    required = True,
    type = str,
    help = message_yellow('Output image file'))

  parser.add_argument('-t', '--tyling_type',
    choices = [ 'landscape', 'portrait', '4tiles', '5tiles', '6tiles', ],
    required = True,
    help = message_yellow('Tyling type'))

  parser.add_argument('-s', '--gap_size',
    default = 10,
    type = int,
    help = message_yellow('Spacing between images'))

  parser.add_argument('-c', '--gap_color',
    default = '#00000000',
    type = str,
    help = message_yellow('Color between images'))

  parser.add_argument('-d', '--direction',
    default = 'NW',
    choices = [ 'NW', 'NE', 'SE', 'SW', ],
    type = str,
    help = message_yellow('Direction, NW(default), NE, SE, SW, valid only when the argument is 5tiles or 6tiles, ignored otherwise'))

  args = parser.parse_args()


  #
  # Check the number of input files and tyling type
  #

  if 6 == len(args.input) and '6tiles' == args.tyling_type:
    pass
  elif 5 == len(args.input) and '5tiles' == args.tyling_type:
    pass
  elif 4 == len(args.input) and '4tiles' == args.tyling_type:
    pass
  elif 2 <= len(args.input) and 'landscape' == args.tyling_type:
    pass
  elif 2 <= len(args.input) and 'portrait' == args.tyling_type:
    pass
  else:
    parser.error(message_red('The number of input files and tyling_type do not match'))


  #
  # Check file's width and height
  #

  dic_size = {
    'height': -1,
    'width': -1,
  }

  tmp_flg = True
  for in_file in args.input:
    ret = subprocess_check_output([
        'identify', '-format', '%w %h', in_file
      ])
    tmp_width = ret.split(' ')[0]
    tmp_height = ret.split(' ')[1]
    print(message_yellow('%s: %sx%s' % (os.path.basename(in_file), tmp_width, tmp_height)))

    if -1 == dic_size['width'] and -1 == dic_size['height']:
      dic_size['width'] = tmp_width
      dic_size['height'] = tmp_height

    else:
      if 'landscape' == args.tyling_type:
        if dic_size['height'] != tmp_height:
          tmp_flg = False
      elif 'portrait' == args.tyling_type:
        if dic_size['width'] != tmp_width:
          tmp_flg = False
      else:
        if dic_size['width'] != tmp_width or dic_size['height'] != tmp_height:
          tmp_flg = False

  if False == tmp_flg:
    parser.error(message_red('Not all images are the same size, width and height'))


  #
  #
  #

  if 1 == args.gap_size % 2:
    parser.error(message_red('`gap_size` does not accept odd numbers, I\'m so sorry.'))


  #
  # Create temporary directory
  #

  temp_dir = tempfile.mkdtemp(prefix = 'create_tiles_')


  #
  # Go to main logic
  #

  if '6tiles' == args.tyling_type:
    create_tiles6(args, temp_dir, dic_size)

  elif '5tiles' == args.tyling_type:
    create_tiles5(args, temp_dir, dic_size)

  elif '4tiles' == args.tyling_type:
    create_tiles4(args, temp_dir, dic_size)

  elif 'landscape' == args.tyling_type or 'portrait' == args.tyling_type:
    create_landscape_or_portrait(args, temp_dir, dic_size)

  print(message_yellow(os.path.basename(args.output)))


  #
  # Remove temporary directory and exit this
  #

  shutil.rmtree(temp_dir)

  sys.exit()


  #
