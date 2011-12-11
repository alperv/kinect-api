from django.conf.urls.defaults import *
from piston.resource import Resource
from kinectsite_piston.api.handlers import BlogpostHandler

blogpost_handler = Resource(BlogpostHandler)

urlpatterns = patterns('',
   #url(r'^blogpost/(?P<post_slug>[^/]+)/', blogpost_handler),
   url(r'^', blogpost_handler),
)

