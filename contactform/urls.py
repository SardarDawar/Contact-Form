from django.conf.urls import url
from .views import Contact


urlpatterns = [
  url('^contact/',Contact,name='contact'),

]
