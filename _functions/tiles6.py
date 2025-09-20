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
# 6 image files
#
#  NW           NE           SE           SW
#  +-----+--+   +--+-----+   +--+--+--+   +--+--+--+
#  |    6| 1|   | 6|    1|   | 5| 6| 1|   | 5| 6| 1|
#  |     +--+   |--+     |   +--+--+--+   +--+--+--+
#  |     | 2|   | 5|     |   | 4|    2|   |    4| 2|
#  +--+--+--+   +--+--+--+   |--+     |   |     +--+
#  | 5| 4| 3|   | 4| 3| 2|   | 3|     |   |     | 3|
#  +--+--+--+   +--+--+--+   +--+-----+   +-----+--+
#


def create_tiles6(_args:list, temp_dir:str, _size:list):

  #
  # 5 files are 1/2, Strictly speaking, it's different.
  #

  tmp_dic = []
  if 'NW' == _args.direction:
    tmp_dic = [1, 2, 3, 4, 5]
  elif 'NE' == _args.direction:
    tmp_dic = [2, 3, 4, 5, 6]
  elif 'SE' == _args.direction:
    tmp_dic = [1, 3, 4, 5, 6]
  elif 'SW' == _args.direction:
    tmp_dic = [1, 2, 3, 5, 6]

  resize_parts_width = (int(_size['width']) - int(_args.gap_size)) / 2
  resize_parts_height = (int(_size['height']) - int(_args.gap_size)) / 2
  resize_parts = '%sx%s!' % (int(resize_parts_width), int(resize_parts_height))

  for idx in tmp_dic:
    ret = subprocess_run([ 'magick',
        _args.input_files[idx - 1],
        '-resize', resize_parts,
        os.path.join(temp_dir, 'parts_' + str(idx) + '.mpc'),
      ])


  #
  # Combine the following to 11
  #
  #  NW      NE     SE     SW
  #  -+--+   +--+-  +--+-  -+--+
  #   | 1|   | 6|   | 5|    | 1|
  #   +--+   |--+   +--+-  -+--+
  #   | 2|   | 5|   | 4|    | 2|
  #  -+--+   +--+-  |--+    +--+
  #   | 3|   | 4|   | 3|    | 3|
  #  -+--+   +--+-  +--+-  -+--+
  #

  tmp_parts_1 = tmp_parts_2 = tmp_parts_3 = None
  if 'NW' == _args.direction:
    tmp_parts_1 = os.path.join(temp_dir, 'parts_1.mpc')
    tmp_parts_2 = os.path.join(temp_dir, 'parts_2.mpc')
    tmp_parts_3 = os.path.join(temp_dir, 'parts_3.mpc')
  elif 'NE' == _args.direction:
    tmp_parts_1 = os.path.join(temp_dir, 'parts_6.mpc')
    tmp_parts_2 = os.path.join(temp_dir, 'parts_5.mpc')
    tmp_parts_3 = os.path.join(temp_dir, 'parts_4.mpc')
  elif 'SE' == _args.direction:
    tmp_parts_1 = os.path.join(temp_dir, 'parts_5.mpc')
    tmp_parts_2 = os.path.join(temp_dir, 'parts_4.mpc')
    tmp_parts_3 = os.path.join(temp_dir, 'parts_3.mpc')
  elif 'SW' == _args.direction:
    tmp_parts_1 = os.path.join(temp_dir, 'parts_1.mpc')
    tmp_parts_2 = os.path.join(temp_dir, 'parts_2.mpc')
    tmp_parts_3 = os.path.join(temp_dir, 'parts_3.mpc')

  size_parts = '%sx%s' % (int(resize_parts_width), int(_args.gap_size))
  ret = subprocess_run([
      'magick', '-size', size_parts, 'xc:' + _args.gap_color, os.path.join(temp_dir, 'base_parts_1.mpc')
    ])
  ret = subprocess_run([ 'magick',
      tmp_parts_1,
      os.path.join(temp_dir, 'base_parts_1.mpc'),
      tmp_parts_2,
      os.path.join(temp_dir, 'base_parts_1.mpc'),
      tmp_parts_3,
      '-append',
      os.path.join(temp_dir, 'parts_11.mpc'),
    ])


  #
  # Combine the following to 21
  #
  #  NW         NE        SE        SW
  #  +--+--+-   +--+--+-  -+--+--+  +--+--+-
  #  | 5| 4|    | 3| 2|    | 6| 1|  | 5| 6|
  #  +--+--+-   +--+--+-  -+--+--+   +--+--+
  #

  tmp_parts_5 = tmp_parts_4 = None
  if 'NW' == _args.direction:
    tmp_parts_5 = os.path.join(temp_dir, 'parts_5.mpc')
    tmp_parts_4 = os.path.join(temp_dir, 'parts_4.mpc')
  elif 'NE' == _args.direction:
    tmp_parts_5 = os.path.join(temp_dir, 'parts_3.mpc')
    tmp_parts_4 = os.path.join(temp_dir, 'parts_2.mpc')
  elif 'SE' == _args.direction:
    tmp_parts_5 = os.path.join(temp_dir, 'parts_6.mpc')
    tmp_parts_4 = os.path.join(temp_dir, 'parts_1.mpc')
  elif 'SW' == _args.direction:
    tmp_parts_5 = os.path.join(temp_dir, 'parts_5.mpc')
    tmp_parts_4 = os.path.join(temp_dir, 'parts_6.mpc')

  size_parts = '%sx%s' % (int(_args.gap_size), int(resize_parts_height))
  ret = subprocess_run([
      'magick', '-size', size_parts, 'xc:' + _args.gap_color, os.path.join(temp_dir, 'base_parts_2.mpc')
    ])
  ret = subprocess_run([ 'magick',
      tmp_parts_5,
      os.path.join(temp_dir, 'base_parts_2.mpc'),
      tmp_parts_4,
      '+append',
      os.path.join(temp_dir, 'parts_21.mpc'),
    ])


  #
  # Combine the following to 31
  #
  #  NW        NE        SE        SW
  #  +-----+-  -+-----+  -+--+--+  +--+--+-
  #  |    6|    |    1|   | 6| 1|  | 5| 6|
  #  |     +-  -+     |  -+--+--+  +--+--+-
  #  |     |    |     |   |    2|  |    4|
  #  +--+--+-  -+--+--+  -+     |  |     +-
  #  | 5| 4|    | 3| 2|   |     |  |     |
  #  +--+--+-  -+--+--+  -+-----+  +-----+-
  #

  tmp_parts_6 = tmp_parts_7 = None
  if 'NW' == _args.direction:
    tmp_parts_6 = _args.input_files[5]
    tmp_parts_7 = os.path.join(temp_dir, 'parts_21.mpc')
  elif 'NE' == _args.direction:
    tmp_parts_6 = _args.input_files[0]
    tmp_parts_7 = os.path.join(temp_dir, 'parts_21.mpc')
  elif 'SE' == _args.direction:
    tmp_parts_6 = os.path.join(temp_dir, 'parts_21.mpc')
    tmp_parts_7 = _args.input_files[1]
  elif 'SW' == _args.direction:
    tmp_parts_6 = os.path.join(temp_dir, 'parts_21.mpc')
    tmp_parts_7 = _args.input_files[3]

  size_parts = '%sx%s' % (int(_size['width']), int(_args.gap_size))
  ret = subprocess_run([
      'magick', '-size', size_parts, 'xc:' + _args.gap_color, os.path.join(temp_dir, 'base_parts_3.mpc')
    ])
  ret = subprocess_run([ 'magick',
      tmp_parts_6,
      os.path.join(temp_dir, 'base_parts_3.mpc'),
      tmp_parts_7,
      '-append',
      os.path.join(temp_dir, 'parts_31.mpc'),
    ])


  #
  # +append 31 and 11 to final
  #

  size_parts = '%sx%s' % (int(_args.gap_size), (int(resize_parts_height) * 3) + (int(_args.gap_size) * 2))
  ret = subprocess_run([
      'magick', '-size', size_parts, 'xc:' + _args.gap_color, os.path.join(temp_dir, 'base_parts_4.mpc')
    ])

  tmp_parts_8 = tmp_parts_9 = None
  if 'NW' == _args.direction:
    tmp_parts_8 = os.path.join(temp_dir, 'parts_31.mpc')
    tmp_parts_9 = os.path.join(temp_dir, 'parts_11.mpc')
  elif 'NE' == _args.direction:
    tmp_parts_8 = os.path.join(temp_dir, 'parts_11.mpc')
    tmp_parts_9 = os.path.join(temp_dir, 'parts_31.mpc')
  elif 'SE' == _args.direction:
    tmp_parts_8 = os.path.join(temp_dir, 'parts_11.mpc')
    tmp_parts_9 = os.path.join(temp_dir, 'parts_31.mpc')
  elif 'SW' == _args.direction:
    tmp_parts_8 = os.path.join(temp_dir, 'parts_31.mpc')
    tmp_parts_9 = os.path.join(temp_dir, 'parts_11.mpc')

  ret = subprocess_run([ 'magick',
      tmp_parts_8,
      os.path.join(temp_dir, 'base_parts_4.mpc'),
      tmp_parts_9,
      '+append',
      _args.output_file
    ])


#
