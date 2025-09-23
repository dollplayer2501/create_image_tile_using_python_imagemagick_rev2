#!/bin/bash

option_gap_size=10
option_gap_color='#ff000088'

option_resize_1='300x'
option_resize_2='x100'
option_resize_3='150x'


#
#
#

tmpdir=$(mktemp -d /tmp/create_tiles_sh.XXXXXXXX) || exit 1
trap 'rm -rf "$tmpdir"' EXIT

#
#
#

magick -size 640x360 xc:'#808080' -fill '#000000' -gravity Center -pointsize 256 -annotate +0+0 '1'  ${tmpdir}/sample1.png
magick -size 640x360 xc:'#808080' -fill '#000000' -gravity Center -pointsize 256 -annotate +0+0 '2'  ${tmpdir}/sample2.png
magick -size 740x360 xc:'#808080' -fill '#000000' -gravity Center -pointsize 256 -annotate +0+0 '2w' ${tmpdir}/sample2w.png
magick -size 640x460 xc:'#808080' -fill '#000000' -gravity Center -pointsize 256 -annotate +0+0 '2h' ${tmpdir}/sample2h.png
magick -size 640x360 xc:'#808080' -fill '#000000' -gravity Center -pointsize 256 -annotate +0+0 '3'  ${tmpdir}/sample3.png
magick -size 640x360 xc:'#808080' -fill '#000000' -gravity Center -pointsize 256 -annotate +0+0 '4'  ${tmpdir}/sample4.png
magick -size 640x360 xc:'#808080' -fill '#000000' -gravity Center -pointsize 256 -annotate +0+0 '5'  ${tmpdir}/sample5.png
magick -size 640x360 xc:'#808080' -fill '#000000' -gravity Center -pointsize 256 -annotate +0+0 '6'  ${tmpdir}/sample6.png


#
# landscape
#
#  +---+---+...+---+
#  |  1|  2|   |  n|
#  +---+---+...+---+
#

python3 ./create_tiles.py \
  --input \
    ${tmpdir}/sample1.png \
    ${tmpdir}/sample2w.png \
    ${tmpdir}/sample3.png \
  --output ${tmpdir}/tiles_landscape..tmp.png \
  --tyling_type landscape \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color

magick ${tmpdir}/tiles_landscape..tmp.png -resize $option_resize_2 ./samples/tiles_landscape.png


#
# portrait
#
#  +---+
#  |  1|
#  +---+
#  |  2|
#  +---+
#  .   .
#  +---+
#  |  n|
#  +---+
#

python3 ./create_tiles.py \
  --input \
    ${tmpdir}/sample1.png \
    ${tmpdir}/sample2h.png \
    ${tmpdir}/sample3.png \
  --output ${tmpdir}/tiles_portrait..tmp.png \
  --tyling_type portrait \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color

magick ${tmpdir}/tiles_portrait..tmp.png -resize $option_resize_3 ./samples/tiles_portrait.png


#
# 4 image files
#
#  +---+---+
#  |  4|  1|
#  +---+---+
#  |  3|  2|
#  +---+---+
#

python3 ./create_tiles.py \
  --input \
    ${tmpdir}/sample1.png \
    ${tmpdir}/sample2.png \
    ${tmpdir}/sample3.png \
    ${tmpdir}/sample4.png \
  --output ${tmpdir}/tiles4..tmp.png \
  --tyling_type 4tiles \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color

magick ${tmpdir}/tiles4..tmp.png -resize $option_resize_1 ./samples/tiles4.png


#
# 5 image files
#
#   NW           NE           SE           SW
#   +-----+---+  +---+-----+  +---+--+--+  +--+--+---+
#   |    5|  1|  |  5|    1|  |  4| 5| 1|  |  |  |   |
#   |     |   |  |   |     |  |   |  |  |  |  |  |   |
#   |     |   |  |   |     |  |   +--+--+  +--+--+   |
#   |     +---+  +---+     |  +---+    2|  |     +---+
#   +--+--+  2|  |  4+--+--+  |  3+     |  |     |   |
#   | 4| 3|   |  |   | 3| 2|  |   |     |  |     |   |
#   |  |  |   |  |   |  |  |  |   |     |  |     |   |
#   +--+--+---+  +---+--+--+  +---+-----+  +-----+---+
#

python3 ./create_tiles.py \
  --input \
    ${tmpdir}/sample1.png \
    ${tmpdir}/sample2.png \
    ${tmpdir}/sample3.png \
    ${tmpdir}/sample4.png \
    ${tmpdir}/sample5.png \
  --output ${tmpdir}/tiles5_NW..tmp.png \
  --tyling_type 5tiles \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color \
  --direction NW

magick ${tmpdir}/tiles5_NW..tmp.png -resize $option_resize_1 ./samples/tiles5_NW.png

python3 ./create_tiles.py \
  --input \
    ${tmpdir}/sample1.png \
    ${tmpdir}/sample2.png \
    ${tmpdir}/sample3.png \
    ${tmpdir}/sample4.png \
    ${tmpdir}/sample5.png \
  --output ${tmpdir}/tiles5_NE..tmp.png \
  --tyling_type 5tiles \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color \
  --direction NE

magick ${tmpdir}/tiles5_NE..tmp.png -resize $option_resize_1 ./samples/tiles5_NE.png

python3 ./create_tiles.py \
  --input \
    ${tmpdir}/sample1.png \
    ${tmpdir}/sample2.png \
    ${tmpdir}/sample3.png \
    ${tmpdir}/sample4.png \
    ${tmpdir}/sample5.png \
  --output ${tmpdir}/tiles5_SE..tmp.png \
  --tyling_type 5tiles \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color \
  --direction SE

magick ${tmpdir}/tiles5_SE..tmp.png -resize $option_resize_1 ./samples/tiles5_SE.png

python3 ./create_tiles.py \
  --input \
    ${tmpdir}/sample1.png \
    ${tmpdir}/sample2.png \
    ${tmpdir}/sample3.png \
    ${tmpdir}/sample4.png \
    ${tmpdir}/sample5.png \
  --output ${tmpdir}/tiles5_SW..tmp.png \
  --tyling_type 5tiles \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color \
  --direction SW

magick ${tmpdir}/tiles5_SW..tmp.png -resize $option_resize_1 ./samples/tiles5_SW.png


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

python3 ./create_tiles.py \
  --input \
    ${tmpdir}/sample1.png \
    ${tmpdir}/sample2.png \
    ${tmpdir}/sample3.png \
    ${tmpdir}/sample4.png \
    ${tmpdir}/sample5.png \
    ${tmpdir}/sample6.png \
  --output ${tmpdir}/tiles6_NW..tmp.png \
  --tyling_type 6tiles \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color \
  --direction NW

magick ${tmpdir}/tiles6_NW..tmp.png -resize $option_resize_1 ./samples/tiles6_NW.png

python3 ./create_tiles.py \
  --input \
    ${tmpdir}/sample1.png \
    ${tmpdir}/sample2.png \
    ${tmpdir}/sample3.png \
    ${tmpdir}/sample4.png \
    ${tmpdir}/sample5.png \
    ${tmpdir}/sample6.png \
  --output ${tmpdir}/tiles6_NE..tmp.png \
  --tyling_type 6tiles \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color \
  --direction NE

magick ${tmpdir}/tiles6_NE..tmp.png -resize $option_resize_1 ./samples/tiles6_NE.png

python3 ./create_tiles.py \
  --input \
    ${tmpdir}/sample1.png \
    ${tmpdir}/sample2.png \
    ${tmpdir}/sample3.png \
    ${tmpdir}/sample4.png \
    ${tmpdir}/sample5.png \
    ${tmpdir}/sample6.png \
  --output ${tmpdir}/tiles6_SE..tmp.png \
  --tyling_type 6tiles \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color \
  --direction SE

magick ${tmpdir}/tiles6_SE..tmp.png -resize $option_resize_1 ./samples/tiles6_SE.png

python3 ./create_tiles.py \
  --input \
    ${tmpdir}/sample1.png \
    ${tmpdir}/sample2.png \
    ${tmpdir}/sample3.png \
    ${tmpdir}/sample4.png \
    ${tmpdir}/sample5.png \
    ${tmpdir}/sample6.png \
  --output ${tmpdir}/tiles6_SW..tmp.png \
  --tyling_type 6tiles \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color \
  --direction SW

magick ${tmpdir}/tiles6_SW..tmp.png -resize $option_resize_1 ./samples/tiles6_SW.png


##
