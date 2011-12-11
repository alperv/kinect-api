from piston.handler import BaseHandler
from kinectsite_piston.api.models import Images 
from piston.utils import rc
import Image
import os

class BlogpostHandler(BaseHandler):
   allowed_methods = ('GET','POST')
   #model = Images

   def read(self, request):
      base = Images.objects
      return base.all()

   def create(self, request):
      if request.content_type:
          data = request.data
      name = request.FILES["image"].name
      image = Image.open(request.FILES["image"])
      image.save('/Users/aydemir/tmp/' + name)
      rc.ALL_OK
