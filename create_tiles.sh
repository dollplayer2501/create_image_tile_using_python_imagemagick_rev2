#!/bin/bash

option_gap_size=10
option_gap_color='#ff000088'

option_resize_1='300x'
option_resize_2='x100'
option_resize_3='150x'


#
#
#

magick -size 640x360 xc:"#808080" -fill "#000000" -gravity Center -pointsize 256 -annotate +0+0 "1" ./sample1.png
magick -size 640x360 xc:"#808080" -fill "#000000" -gravity Center -pointsize 256 -annotate +0+0 "2" ./sample2.png
magick -size 740x360 xc:"#808080" -fill "#000000" -gravity Center -pointsize 256 -annotate +0+0 "2w" ./sample2w.png
magick -size 640x460 xc:"#808080" -fill "#000000" -gravity Center -pointsize 256 -annotate +0+0 "2h" ./sample2h.png
magick -size 640x360 xc:"#808080" -fill "#000000" -gravity Center -pointsize 256 -annotate +0+0 "3" ./sample3.png
magick -size 640x360 xc:"#808080" -fill "#000000" -gravity Center -pointsize 256 -annotate +0+0 "4" ./sample4.png
magick -size 640x360 xc:"#808080" -fill "#000000" -gravity Center -pointsize 256 -annotate +0+0 "5" ./sample5.png
magick -size 640x360 xc:"#808080" -fill "#000000" -gravity Center -pointsize 256 -annotate +0+0 "6" ./sample6.png


#
# landscape
#
#  +---+---+...+---+
#  |  1|  2|   |  n|
#  +---+---+...+---+

python3 ./create_tiles.py \
  ./sample1.png \
  ./sample2w.png \
  ./sample3.png \
  ./tiles_landscape..tmp.png \
  --tyling_type landscape \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color

magick ./tiles_landscape..tmp.png -resize $option_resize_2 ./tiles_landscape.png
rm ./tiles_landscape..tmp.png


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

python3 ./create_tiles.py \
  ./sample1.png \
  ./sample2h.png \
  ./sample3.png \
  ./tiles_portrait..tmp.png \
  --tyling_type portrait \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color

magick ./tiles_portrait..tmp.png -resize $option_resize_3 ./tiles_portrait.png
rm ./tiles_portrait..tmp.png


#
# 4 image files
#
#  +---+---+
#  |  4|  1|
#  +---+---+
#  |  3|  2|
#  +---+---+

python3 ./create_tiles.py \
  ./sample1.png \
  ./sample2.png \
  ./sample3.png \
  ./sample4.png \
  ./tiles4..tmp.png \
  --tyling_type 4tiles \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color

magick ./tiles4..tmp.png -resize $option_resize_1 ./tiles4.png
rm ./tiles4..tmp.png


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
  ./sample1.png \
  ./sample2.png \
  ./sample3.png \
  ./sample4.png \
  ./sample5.png \
  ./tiles5_NW..tmp.png \
  --tyling_type 5tiles \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color \
  --direction NW

magick ./tiles5_NW..tmp.png -resize $option_resize_1 ./tiles5_NW.png
rm ./tiles5_NW..tmp.png


python3 ./create_tiles.py \
  ./sample1.png \
  ./sample2.png \
  ./sample3.png \
  ./sample4.png \
  ./sample5.png \
  ./tiles5_NE..tmp.png \
  --tyling_type 5tiles \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color \
  --direction NE

magick ./tiles5_NE..tmp.png -resize $option_resize_1 ./tiles5_NE.png
rm ./tiles5_NE..tmp.png


python3 ./create_tiles.py \
  ./sample1.png \
  ./sample2.png \
  ./sample3.png \
  ./sample4.png \
  ./sample5.png \
  ./tiles5_SE..tmp.png \
  --tyling_type 5tiles \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color \
  --direction SE

magick ./tiles5_SE..tmp.png -resize $option_resize_1 ./tiles5_SE.png
rm ./tiles5_SE..tmp.png


python3 ./create_tiles.py \
  ./sample1.png \
  ./sample2.png \
  ./sample3.png \
  ./sample4.png \
  ./sample5.png \
  ./tiles5_SW..tmp.png \
  --tyling_type 5tiles \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color \
  --direction SW

magick ./tiles5_SW..tmp.png -resize $option_resize_1 ./tiles5_SW.png
rm ./tiles5_SW..tmp.png


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
  ./sample1.png \
  ./sample2.png \
  ./sample3.png \
  ./sample4.png \
  ./sample5.png \
  ./sample6.png \
  ./tiles6_NW..tmp.png \
  --tyling_type 6tiles \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color \
  --direction NW

magick ./tiles6_NW..tmp.png -resize $option_resize_1 ./tiles6_NW.png
rm ./tiles6_NW..tmp.png


python3 ./create_tiles.py \
  ./sample1.png \
  ./sample2.png \
  ./sample3.png \
  ./sample4.png \
  ./sample5.png \
  ./sample6.png \
  ./tiles6_NE..tmp.png \
  --tyling_type 6tiles \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color \
  --direction NE

magick ./tiles6_NE..tmp.png -resize $option_resize_1 ./tiles6_NE.png
rm ./tiles6_NE..tmp.png


python3 ./create_tiles.py \
  ./sample1.png \
  ./sample2.png \
  ./sample3.png \
  ./sample4.png \
  ./sample5.png \
  ./sample6.png \
  ./tiles6_SE..tmp.png \
  --tyling_type 6tiles \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color \
  --direction SE

magick ./tiles6_SE..tmp.png -resize $option_resize_1 ./tiles6_SE.png
rm ./tiles6_SE..tmp.png


python3 ./create_tiles.py \
  ./sample1.png \
  ./sample2.png \
  ./sample3.png \
  ./sample4.png \
  ./sample5.png \
  ./sample6.png \
  ./tiles6_SW..tmp.png \
  --tyling_type 6tiles \
  --gap_size $option_gap_size \
  --gap_color $option_gap_color \
  --direction SW

magick ./tiles6_SW..tmp.png -resize $option_resize_1 ./tiles6_SW.png
rm ./tiles6_SW..tmp.png


#
#
#

rm ./sample1.png
rm ./sample2.png
rm ./sample2w.png
rm ./sample2h.png
rm ./sample3.png
rm ./sample4.png
rm ./sample5.png
rm ./sample6.png


##
