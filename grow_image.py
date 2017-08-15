#
# This file was generated using xslt from its XML file
#
# Copyright 2009, Associated Universities Inc., Washington DC
#
import sys
import os
from  casac import *
import string
from taskinit import casalog
from taskinit import xmlpath
#from taskmanager import tm
import task_grow_image
def grow_image(infile='', outfile='', growpix=100):

        """Grows the spatial extend of an image.
grow_image(infile  = 'test.image',
            outfile = 'test_grown.image',
            growpix = 100
            )
grow_image(infile  = 'test.image',
            outfile = 'test_grown.image',
            growpix = [100,200]
            )
  
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['infile'] = infile
        mytmp['outfile'] = outfile
        mytmp['growpix'] = growpix
	pathname="file:///mnt/fhgfs/krieger/scripts/casa_tools/"
	trec = casac.utils().torecord(pathname+'grow_image.xml')

        casalog.origin('grow_image')
        if trec.has_key('grow_image') and casac.utils().verify(mytmp, trec['grow_image']) :
	    result = task_grow_image.grow_image(infile, outfile, growpix)

	else :
	  result = False
        return result
