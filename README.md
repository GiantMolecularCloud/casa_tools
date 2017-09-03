# casa_tools

A collections of custom CASA tasks that I need every once in a while.
CASA: https://casa.nrao.edu/

This repo contains compiled tasks that can be imported into CASA by running mytasks.py. Due to an incompatibility with CASA 5.0.0, these are currently compiled and working under CASA 4.7. This will change in the future, so that these do not run using CASA <5 anymore but have to be recompiled with the desired version of CASA.

## available tasks

* grow_image
* ...

## task details

#### `grow_image`
```
inp(grow_image)
#  grow_image :: Grows the spatial extend of an image.
infile    =  ''    #  image to be grown
outfile   =  ''    #  grown image
growpix   =  100   #  Number of pixels to grow the image (on both sides!). Must be either a single int or a list of two ints.
```

## more to come ...
