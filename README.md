<h1 align="center">NREIP Fall Mentorship Program - FALL 2020</h1>

# Table of Contents

1. [About](https://github.com/JsAviles/NREIP_FallMentorship2020#about)
2. [Operating Instructions](https://github.com/JsAviles/NREIP_FallMentorship2020#Operating-Instructions)
3. [Functionality](https://github.com/JsAviles/NREIP_FallMentorship2020#Functionality)
4. [Sample Output](https://github.com/JsAviles/NREIP_FallMentorship2020#Sample-output)
5. [Contributors](https://github.com/JsAviles/NREIP_FallMentorship2020#Contributors)

## About

Fall project assigned by the United States Naval Academy, which purposed me with exploring image compression and simulating Lossless image encoding.
## Operating Instructions

* **Update pip**

        $ pip3 install --upgrade pip

* **Install numpy**

        $ pip3 install numpy

* **Intall Pillow**

        $ pip3 install Pillow

* **Run**

        $ python3 imgCompy.py

## Functionality

imgCompy.py uses stem.jpg and creates several files for comparison:

* **NREIP_uncompF.txt** - Text file containing the uncompressed raw data of the image stem.jpg
* **NREIP_compF.txt** - Text file containing the lossess encoded raw data (compressed) of stemp.jpg
* **NREIP_uncompressed_image.tiff** - Raw image before lossless compression occurs
* **NREIP_compressed_image.tiff** -  Raw image recreated after lossless compress/decompress occurs

For comparison we see that the NREIP_compF.txt file is over 70% smaller in size than its uncompressed counter part.

We also can see that the images created using the raw data from NREIP_compF.txt and NREIP_uncompF.txt are identical, as shown below.


![alt text](https://i.gyazo.com/e63a546d639d3930c890be3a43946b1d.png)


## Sample output

    $ python3 imgCompy.py

![alt text](https://i.gyazo.com/1606d88d3e7bc569727835669d4bbb80.png)
## Contributors

**Jesus Sebastian Aviles**

![alt text](https://i.gyazo.com/30c872a61a8257508866840b44592530.png)

Contact info:

* sebastian_aviles@yahoo.com

* [Linkedin](https://www.linkedin.com/in/sebastian-aviles-215b3471/)
