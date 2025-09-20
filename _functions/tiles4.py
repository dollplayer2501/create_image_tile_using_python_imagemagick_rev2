#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import os

from _functions.common_function import (
  subprocess_check_output,
  subprocess_run,
  subprocess_error_message,
  message_yellow,
)


#
# 4 image files
#
#  +---+---+
#  |  4|  1|
#  +---+---+
#  |  3|  2|
#  +---+---+
#


def create_tiles4(_args:list, temp_dir:str, _size:list):

  size_parts = '%sx%s' % (int(_size['width']), int(_args.gap_size))
  ret = subprocess_run([
      'magick', '-size', size_parts, 'xc:' + _args.gap_color, os.path.join(temp_dir, 'base_parts_1.mpc')
    ])
  ret = subprocess_run([ 'magick',
      _args.input_files[0],
      os.path.join(temp_dir, 'base_parts_1.mpc'),
      _args.input_files[1],
      '-append',
      os.path.join(temp_dir, 'parts_1.mpc'),
    ])
  ret = subprocess_run([ 'magick',
      _args.input_files[3],
      os.path.join(temp_dir, 'base_parts_1.mpc'),
      _args.input_files[2],
      '-append',
      os.path.join(temp_dir, 'parts_2.mpc'),
    ])

  size_parts = '%sx%s' % (int(_args.gap_size), int((int(_size['height']) * 2) + int(_args.gap_size)))
  ret = subprocess_run([
      'magick', '-size', size_parts, 'xc:' + _args.gap_color, os.path.join(temp_dir, 'base_parts_2.mpc')
    ])

  ret = subprocess_run([ 'magick',
      os.path.join(temp_dir, 'parts_2.mpc'),
      os.path.join(temp_dir, 'base_parts_2.mpc'),
      os.path.join(temp_dir, 'parts_1.mpc'),
      '+append',
      _args.output_file
    ])


#
