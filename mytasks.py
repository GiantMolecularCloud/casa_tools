#
# User defined tasks setup.
# Generated from buildmytask.
#

if sys.path[1] != '/mnt/fhgfs/krieger/modules/casa_tools':
  sys.path.insert(1, '/mnt/fhgfs/krieger/modules/casa_tools')
from odict import odict
if not globals().has_key('mytasks') :
  mytasks = odict()

mytasks['grow_image'] = 'Grows the spatial extend of an image.'

if not globals().has_key('task_location') :
  task_location = odict()

task_location['grow_image'] = '/mnt/fhgfs/krieger/modules/casa_tools'
import inspect
myglobals = sys._getframe(len(inspect.stack())-1).f_globals
tasksum = myglobals['tasksum'] 
for key in mytasks.keys() :
  tasksum[key] = mytasks[key]

from grow_image_cli import  grow_image_cli as grow_image
