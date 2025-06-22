#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from _functions.common_function import (
  subprocess_check_output,
  subprocess_run,
  subprocess_error_message,
  message_yellow,
)


#
# +/-append
#
#  +: Landscape
#
#    +---+---+...+---+
#    |  1|  2|   |  n|
#    +---+---+...+---+
#
#  -: Portrait
#
#    +---+
#    |  1|
#    +---+
#    |  2|
#    +---+
#    .   .
#    +---+
#    |  n|
#    +---+
#


def create_landscape_or_portrait(_args:list, _size:list):

  size_parts = ''
  if 'landscape' == _args.tyling_type:
    size_parts = '%sx%s' % (int(_args.gap_size), int(_size['height']))
  else:
    size_parts = '%sx%s' % (int(_size['width']), int(_args.gap_size))

  ret = subprocess_run([
      'magick', '-size', size_parts, 'xc:' + _args.gap_color, 'base_parts.mpc'
    ])
  exec_args = [
      'magick',
    ]
  for in_file in _args.input_files:
    exec_args.append(in_file)
    exec_args.append('base_parts.mpc')
  exec_args.pop(-1)

  if 'landscape' == _args.tyling_type:
    exec_args.append('+append')
  else:
    exec_args.append('-append')

  exec_args.append(_args.output_file)
  ret = subprocess_run(exec_args)


#
