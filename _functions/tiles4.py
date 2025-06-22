#! /usr/bin/env python3
# -*- coding: utf-8 -*-


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


def create_tiles4(_args:list, _size:list):

  size_parts = '%sx%s' % (int(_size['width']), int(_args.gap_size))
  ret = subprocess_run([
      'magick', '-size', size_parts, 'xc:' + _args.gap_color, 'base_parts_1.mpc'
    ])
  ret = subprocess_run([ 'magick',
      _args.input_files[0],
      'base_parts_1.mpc',
      _args.input_files[1],
      '-append',
      'parts_1.mpc',
    ])
  ret = subprocess_run([ 'magick',
      _args.input_files[3],
      'base_parts_1.mpc',
      _args.input_files[2],
      '-append',
      'parts_2.mpc',
    ])

  size_parts = '%sx%s' % (int(_args.gap_size), int((int(_size['height']) * 2) + int(_args.gap_size)))
  ret = subprocess_run([
      'magick', '-size', size_parts, 'xc:' + _args.gap_color, 'base_parts_2.mpc'
    ])

  ret = subprocess_run([ 'magick',
      'parts_2.mpc',
      'base_parts_2.mpc',
      'parts_1.mpc',
      '+append',
      _args.output_file
    ])


#
