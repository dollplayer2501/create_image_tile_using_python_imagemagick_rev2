Using Python and ImageMagick, image files are arranged in tiles according to certain rules.

## Prerequisite:

- All images must be the same size  
The image size is checked in the script.
- Install ImageMagick beforehand  
I am not using Python's ImageMagick library, but am using `subprocess.run(['magick', ...], ...)`.  
It uses ImageMagick ver.7 syntax.


## Usage:

I think it would be better to create a batch file and run it rather than specifying the files one by one from the console and executing them in real time.  
Check `create_tiles.sh`.

|Arguments|Default|Remarks|
|---|---|---|
|Input image files||The order has meaning, files are not checked for existence|
|Output image file||The end of the *input image files name* without an argument name will be the output file name|
|`-tt`, `--tyling_type`||`6tiles`, `5tiles`, `4tiles`, `landscape`, `portrait`|
|`-gs`, `--gap_size`|`10`||
|`-gc`, `--gap_color`|`#00000000`||
|`-di`, `--direction`|`NE`|(option) Direction, `NW`(default), `NE`, `SE`, `SW`, valid only when the `--tyling_type` value is `5tiles` or `6tiles`, ignored otherwise|


### 6 tiles

|`NW`|`NE`|`SE`|`SW`|
|--|--|--|--|
|<img src="./tiles6_NW.png" width="150">|<img src="./tiles6_NE.png" width="150">|<img src="./tiles6_SE.png" width="150">|<img src="./tiles6_SW.png" width="150">|

```
python3 ./create_tiles.py \
  ./sample1.png \
  ./sample2.png \
  ./sample3.png \
  ./sample4.png \
  ./sample5.png \
  ./sample6.png \
  ./tiles6_NW.png \
  --tyling_type 6tiles \
  --gap_size 20 \
  --gap_color '#72170faa'
  --direction NW
```


### 5 tiles

|`NW`|`NE`|`SE`|`SW`|
|--|--|--|--|
|<img src="./tiles5_NW.png" width="150">|<img src="./tiles5_NE.png" width="150">|<img src="./tiles5_SE.png" width="150">|<img src="./tiles5_SW.png" width="150">|

```
python3 ./create_tiles.py \
  ./sample1.png \
  ./sample2.png \
  ./sample3.png \
  ./sample4.png \
  ./sample5.png \
  ./tiles5_NW.png \
  --tyling_type 5tiles \
  --gap_size 20 \
  --gap_color '#72170faa'
  --direction NW
```


### 4 tiles

<img src="./tiles4.png" width="150">

```
python3 ./create_tiles.py \
  ./sample1.png \
  ./sample2.png \
  ./sample3.png \
  ./sample4.png \
  ./tiles4..tmp.png \
  --tyling_type 4tiles \
  --gap_size 20 \
  --gap_color '#72170faa'
```


### Landscape

<img src="./tiles_landscape.png" height="60">

```
python3 ./create_tiles.py \
  ./sample1.png \
  ./sample2w.png \
  ./sample3.png \
  ./tiles_landscape.png \
  --tyling_type landscape \
  --gap_size 20 \
  --gap_color '#72170faa'
```


### Portrait

<img src="./tiles_portrait.png" width="100">

```
python3 ./create_tiles.py \
  ./sample1.png \
  ./sample2w.png \
  ./sample3.png \
  ./tiles_portrait.png \
  --tyling_type portrait \
  --gap_size 20 \
  --gap_color '#72170faa'
```


<!-- -->
