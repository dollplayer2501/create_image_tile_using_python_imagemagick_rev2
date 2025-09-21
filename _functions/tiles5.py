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
# 5 image files
#
#   NW           NE           SE           SW
#   +-----+---+  +---+-----+  +---+--+--+  +--+--+---+
#   |    5|  1|  |  5|    1|  |  4| 5| 1|  | 4| 5|  1|
#   |     |   |  |   |     |  |   |  |  |  |  |  |   |
#   |     |   |  |   |     |  |   +--+--+  +--+--+   |
#   |     +---+  +---+     |  +---+    2|  |    3+---+
#   +--+--+  2|  |  4+--+--+  |  3+     |  |     |  2|
#   | 4| 3|   |  |   | 3| 2|  |   |     |  |     |   |
#   |  |  |   |  |   |  |  |  |   |     |  |     |   |
#   +--+--+---+  +---+--+--+  +---+-----+  +-----+---+
#
#   For example, in the case of NW
#     Reduce image No.1 and NO.2 to 3/4
#     Reduce image No.3 and NO.4 to 1/2
#


def create_tiles5(_args:list, temp_dir:str, _size:list):

  #
  # 2 files are 1/2, Strictly speaking, it's different.
  #
  #   NW        NE        SE        SW
  #   +--+--+    +--+--+  -+--+--+  +--+--+-
  #   | 4| 3|    | 3| 2|   | 5| 1|  | 4| 5|
  #   |  |  |    |  |  |   |  |  |  |  |  |
  #   +--+--+-  -+--+--+   +--+--+  +--+--+
  #    4  3       4  3      4  3     4  3
  #

  tmp_parts_3 = tmp_parts_4 = None
  if 'NW' == _args.direction:
    tmp_parts_4 = _args.input[3]
    tmp_parts_3 = _args.input[2]
  elif 'NE' == _args.direction:
    tmp_parts_4 = _args.input[2]
    tmp_parts_3 = _args.input[1]
  elif 'SE' == _args.direction:
    tmp_parts_4 = _args.input[4]
    tmp_parts_3 = _args.input[0]
  elif 'SW' == _args.direction:
    tmp_parts_4 = _args.input[3]
    tmp_parts_3 = _args.input[4]

  resize_parts = '%sx%s' % ((int(_size['width']) - int(_args.gap_size)) / 2, '')
  ret = subprocess_run([ 'magick',
      tmp_parts_4,
      '-resize', resize_parts,
      os.path.join(temp_dir, 'parts_4.mpc')
    ])
  ret = subprocess_run([ 'magick',
      tmp_parts_3,
      '-resize', resize_parts,
      os.path.join(temp_dir, 'parts_3.mpc')
    ])
  ret_parts_3_height = subprocess_check_output([
      'identify', '-format', '%h', os.path.join(temp_dir, 'parts_3.mpc')
    ])

  parts_31_height = int(_size['height']) + int(_args.gap_size) + int(ret_parts_3_height)
  parts_11_height = ((int(_size['height']) / 4 * 3) * 2) + int(_args.gap_size)
  parts_31_gap_height = int(_args.gap_size) + (int(parts_11_height) - int(parts_31_height))

  # +append 3 and 4 to 21

  size_parts = '%sx%s' % (int(_args.gap_size), ret_parts_3_height)
  ret = subprocess_run([
      'magick', '-size', size_parts, 'xc:' + _args.gap_color, os.path.join(temp_dir, 'base_parts_2.mpc')
    ])
  ret = subprocess_run([ 'magick',
      os.path.join(temp_dir, 'parts_4.mpc'),
      os.path.join(temp_dir, 'base_parts_2.mpc'),
      os.path.join(temp_dir, 'parts_3.mpc'),
      '+append',
      os.path.join(temp_dir, 'parts_21.mpc'),
    ])


  #
  # -append 5 and 21 to 31
  #
  #   NW        NE        SE        SW
  #   +-----+-  -+-----+  -+--+--+  +--+--+-
  #   |    5|    |    1|   | 5| 1|  | 4| 5|
  #   |     |    |     |   |  |  |  |  |  |
  #   |     |    |     |   +--+--+  +--+--+
  #   |     +-  -+     |  -+    2|  |    3+-
  #   +--+--+    +--+--+   +     |  |     |
  #   | 4| 3|    | 3| 2|   |     |  |     |
  #   |  |  |    |  |  |   |     |  |     |
  #   +--+--+-  -+--+--+  -+-----+  +-----+-
  #

  tmp_parts_5_1 = tmp_parts_5_2 = None
  if 'NW' == _args.direction:
    tmp_parts_5_1 = _args.input[4]
    tmp_parts_5_2 = os.path.join(temp_dir, 'parts_21.mpc')
  elif 'NE' == _args.direction:
    tmp_parts_5_1 = _args.input[0]
    tmp_parts_5_2 = os.path.join(temp_dir, 'parts_21.mpc')
  elif 'SE' == _args.direction:
    tmp_parts_5_1 = os.path.join(temp_dir, 'parts_21.mpc')
    tmp_parts_5_2 = _args.input[1]
  elif 'SW' == _args.direction:
    tmp_parts_5_1 = os.path.join(temp_dir, 'parts_21.mpc')
    tmp_parts_5_2 = _args.input[2]

  size_parts = '%sx%s' % (int(_size['width']), int(parts_31_gap_height))
  ret = subprocess_run([
      'magick', '-size', size_parts, 'xc:' + _args.gap_color, os.path.join(temp_dir, 'base_parts_3.mpc')
    ])
  ret = subprocess_run([ 'magick',
      tmp_parts_5_1,
      os.path.join(temp_dir, 'base_parts_3.mpc'),
      tmp_parts_5_2,
      '-append',
      os.path.join(temp_dir, 'parts_31.mpc'),
    ])



  #
  # 2 files are 3/4, Strictly speaking, it's different.
  #
  #   NW      NE      SE      SW
  #   -+---+  +---+-  +---+-  -+---+
  #    |  1|  |  5|   |  4|    |  1|
  #    |   |  |   |   |   |    |   |
  #    |   |  |   |   |   +-  -+   |
  #    +---+  +---+   +---+    +---+
  #   -+  2|  |  4+-  |  3+    |  2|
  #    |   |  |   |   |   |    |   |
  #    |   |  |   |   |   |    |   |
  #   -+---+  +---+-  +---+-  -+---+
  #

  tmp_parts_1 = tmp_parts_2 = None
  if 'NW' == _args.direction:
    tmp_parts_1 = _args.input[0]
    tmp_parts_2 = _args.input[1]
  elif 'NE' == _args.direction:
    tmp_parts_1 = _args.input[4]
    tmp_parts_2 = _args.input[3]
  elif 'SE' == _args.direction:
    tmp_parts_1 = _args.input[3]
    tmp_parts_2 = _args.input[2]
  elif 'SW' == _args.direction:
    tmp_parts_1 = _args.input[0]
    tmp_parts_2 = _args.input[1]

  resize_parts = '%sx%s' % (int(_size['width']) / 4 * 3, int(_size['width']) / 4 * 3)
  ret = subprocess_run([ 'magick',
      tmp_parts_1,
      '-resize', resize_parts,
      os.path.join(temp_dir, 'parts_1.mpc')
    ])
  ret = subprocess_run([ 'magick',
      tmp_parts_2,
      '-resize', resize_parts,
      os.path.join(temp_dir, 'parts_2.mpc')
    ])

  # -append 1 and 2 to 11

  size_parts = '%sx%s' % (int(_size['width']) / 4 * 3, int(_args.gap_size))
  ret = subprocess_run([
      'magick', '-size', size_parts, 'xc:' + _args.gap_color, os.path.join(temp_dir, 'base_parts_1.mpc')
    ])
  ret = subprocess_run([ 'magick',
      os.path.join(temp_dir, 'parts_1.mpc'),
      os.path.join(temp_dir, 'base_parts_1.mpc'),
      os.path.join(temp_dir, 'parts_2.mpc'),
      '-append',
      os.path.join(temp_dir, 'parts_11.mpc'),
    ])


  #
  # +append 31 and 11
  #

  tmp_parts_31 = tmp_parts_11 = None
  if 'NW' == _args.direction:
    tmp_parts_31 = os.path.join(temp_dir, 'parts_31.mpc')
    tmp_parts_11 = os.path.join(temp_dir, 'parts_11.mpc')
  elif 'NE' == _args.direction:
    tmp_parts_31 = os.path.join(temp_dir, 'parts_11.mpc')
    tmp_parts_11 = os.path.join(temp_dir, 'parts_31.mpc')
  elif 'SE' == _args.direction:
    tmp_parts_31 = os.path.join(temp_dir, 'parts_11.mpc')
    tmp_parts_11 = os.path.join(temp_dir, 'parts_31.mpc')
  elif 'SW' == _args.direction:
    tmp_parts_31 = os.path.join(temp_dir, 'parts_31.mpc')
    tmp_parts_11 = os.path.join(temp_dir, 'parts_11.mpc')

  size_parts = '%sx%s' % (int(_args.gap_size), int(parts_11_height))
  ret = subprocess_run([
      'magick', '-size', size_parts, 'xc:' + _args.gap_color, os.path.join(temp_dir, 'base_parts_4.mpc')
    ])

  ret = subprocess_run([ 'magick',
      tmp_parts_31,
      os.path.join(temp_dir, 'base_parts_4.mpc'),
      tmp_parts_11,
      '+append',
      _args.output
    ])


#
