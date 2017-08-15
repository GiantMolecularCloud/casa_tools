#
# This file was generated using xslt from its XML file
#
# Copyright 2014, Associated Universities Inc., Washington DC
#
import sys
import os
#from casac import *
import casac
import string
import time
import inspect
import gc
import numpy
from odict import odict
from types import * 
from task_grow_image import grow_image
class grow_image_cli_:
    __name__ = "grow_image"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (grow_image_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'infile':None, 'outfile':None, 'growpix':None, }


    def result(self, key=None):
	    #### and add any that have completed...
	    return None


    def __call__(self, infile=None, outfile=None, growpix=None, ):

        """Grows the spatial extend of an image.

	Detailed Description: 

grow image: grow the size of an image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Grow the spatial size of an image by the given number of pixels. Growing is
done symmetrically to each side at the moment. The final image will be
larger by 2*growpix.
To be done: option to treat the input size as the target size
            option to enter physical size (e.g. in arcmin)

Mandatory unnamed, ordered arguments:
    infile      Path and file name of the input file. Must be a format known
                to CASA: image, fits or miriad image
    outfile     Path and file name of the grown image. Is always a CASA image
    growpix     Number of pixels that the image is grown. A single integer
                grows the image on all four sides. Differing grow scales can 
                be given as a list of two integers.
    
	Arguments :
		infile:	image to be grown
		   Default Value: 

		outfile:	grown image
		   Default Value: 

		growpix:	Number of pixels to grow the image (on both sides!). Must be either a single int or a list of two ints.
		   Default Value: 100

	Returns: void

	Example :

grow_image(infile  = 'test.image',
            outfile = 'test_grown.image',
            growpix = 100
            )
grow_image(infile  = 'test.image',
            outfile = 'test_grown.image',
            growpix = [100,200]
            )
  
        """
	if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=sys._getframe(len(inspect.stack())-1).f_globals
	#casac = self.__globals__['casac']
	casalog = self.__globals__['casalog']
	casa = self.__globals__['casa']
	#casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'grow_image'
        self.__globals__['taskname'] = 'grow_image'
        ###
        self.__globals__['update_params'](func=self.__globals__['taskname'],printtext=False,ipython_globals=self.__globals__)
        ###
        ###
        #Handle globals or user over-ride of arguments
        #
        if type(self.__call__.func_defaults) is NoneType:
            function_signature_defaults={}
	else:
	    function_signature_defaults=dict(zip(self.__call__.func_code.co_varnames[1:],self.__call__.func_defaults))
	useLocalDefaults = False

        for item in function_signature_defaults.iteritems():
                key,val = item
                keyVal = eval(key)
                if (keyVal == None):
                        #user hasn't set it - use global/default
                        pass
                else:
                        #user has set it - use over-ride
			if (key != 'self') :
			   useLocalDefaults = True

	myparams = {}
	if useLocalDefaults :
	   for item in function_signature_defaults.iteritems():
	       key,val = item
	       keyVal = eval(key)
	       exec('myparams[key] = keyVal')
	       self.parameters[key] = keyVal
	       if (keyVal == None):
	           exec('myparams[key] = '+ key + ' = self.itsdefault(key)')
		   keyVal = eval(key)
		   if(type(keyVal) == dict) :
                      if len(keyVal) > 0 :
		         exec('myparams[key] = ' + key + ' = keyVal[len(keyVal)-1][\'value\']')
		      else :
		         exec('myparams[key] = ' + key + ' = {}')
	 
        else :
            print ''

            myparams['infile'] = infile = self.parameters['infile']
            myparams['outfile'] = outfile = self.parameters['outfile']
            myparams['growpix'] = growpix = self.parameters['growpix']


	result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['infile'] = infile
        mytmp['outfile'] = outfile
        mytmp['growpix'] = growpix
	pathname="file:///mnt/fhgfs/krieger/modules/casa_tools/"
	trec = casac.casac.utils().torecord(pathname+'grow_image.xml')

        casalog.origin('grow_image')
	try :
          #if not trec.has_key('grow_image') or not casac.casac.utils().verify(mytmp, trec['grow_image']) :
	    #return False

          casac.casac.utils().verify(mytmp, trec['grow_image'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('grow_image', 'grow_image.last', myparams, self.__globals__,scriptstr=scriptstr)
          tname = 'grow_image'
          spaces = ' '*(18-len(tname))
          casalog.post('\n##########################################'+
                       '\n##### Begin Task: ' + tname + spaces + ' #####')
          if type(self.__call__.func_defaults) is NoneType:
              casalog.post(scriptstr[0]+'\n', 'INFO')
          else :
              casalog.post(scriptstr[1][1:]+'\n', 'INFO')
          result = grow_image(infile, outfile, growpix)
          casalog.post('##### End Task: ' + tname + '  ' + spaces + ' #####'+
                       '\n##########################################')

	except Exception, instance:
          if(self.__globals__.has_key('__rethrow_casa_exceptions') and self.__globals__['__rethrow_casa_exceptions']) :
             raise
          else :
             #print '**** Error **** ',instance
	     tname = 'grow_image'
             casalog.post('An error occurred running task '+tname+'.', 'ERROR')
             pass

        gc.collect()
        return result
#
#
#
    def paramgui(self, useGlobals=True, ipython_globals=None):
        """
        Opens a parameter GUI for this task.  If useGlobals is true, then any relevant global parameter settings are used.
        """
        import paramgui
	if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=sys._getframe(len(inspect.stack())-1).f_globals

        if useGlobals:
	    if ipython_globals == None:
                myf=self.__globals__
            else:
                myf=ipython_globals

            paramgui.setGlobals(myf)
        else:
            paramgui.setGlobals({})

        paramgui.runTask('grow_image', myf['_ip'])
        paramgui.setGlobals({})

#
#
#
    def defaults(self, param=None, ipython_globals=None, paramvalue=None, subparam=None):
	if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=sys._getframe(len(inspect.stack())-1).f_globals
        if ipython_globals == None:
            myf=self.__globals__
        else:
            myf=ipython_globals

        a = odict()
        a['infile']  = ''
        a['outfile']  = ''
        a['growpix']  = 100


### This function sets the default values but also will return the list of
### parameters or the default value of a given parameter
        if(param == None):
                myf['__set_default_parameters'](a)
        elif(param == 'paramkeys'):
                return a.keys()
        else:
            if(paramvalue==None and subparam==None):
               if(a.has_key(param)):
                  return a[param]
               else:
                  return self.itsdefault(param)
            else:
               retval=a[param]
               if(type(a[param])==dict):
                  for k in range(len(a[param])):
                     valornotval='value'
                     if(a[param][k].has_key('notvalue')):
                        valornotval='notvalue'
                     if((a[param][k][valornotval])==paramvalue):
                        retval=a[param][k].copy()
                        retval.pop(valornotval)
                        if(subparam != None):
                           if(retval.has_key(subparam)):
                              retval=retval[subparam]
                           else:
                              retval=self.itsdefault(subparam)
		     else:
                        retval=self.itsdefault(subparam)
               return retval


#
#
    def check_params(self, param=None, value=None, ipython_globals=None):
      if ipython_globals == None:
          myf=self.__globals__
      else:
          myf=ipython_globals
#      print 'param:', param, 'value:', value
      try :
         if str(type(value)) != "<type 'instance'>" :
            value0 = value
            value = myf['cu'].expandparam(param, value)
            matchtype = False
            if(type(value) == numpy.ndarray):
               if(type(value) == type(value0)):
                  myf[param] = value.tolist()
               else:
                  #print 'value:', value, 'value0:', value0
                  #print 'type(value):', type(value), 'type(value0):', type(value0)
                  myf[param] = value0
                  if type(value0) != list :
                     matchtype = True
            else :
               myf[param] = value
            value = myf['cu'].verifyparam({param:value})
            if matchtype:
               value = False
      except Exception, instance:
         #ignore the exception and just return it unchecked
         myf[param] = value
      return value
#
#
    def description(self, key='grow_image', subkey=None):
        desc={'grow_image': 'Grows the spatial extend of an image.',
               'infile': 'image to be grown',
               'outfile': 'grown image',
               'growpix': 'Number of pixels to grow the image (on both sides!). Must be either a single int or a list of two ints.',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['infile']  = ''
        a['outfile']  = ''
        a['growpix']  = 100

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
	      return a[paramname]
grow_image_cli = grow_image_cli_()
