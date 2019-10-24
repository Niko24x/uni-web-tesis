from django.conf.urls import url                                                                                                                              
from .views import default_map

app_name = 'maps'
urlpatterns = [ 
    url(r'', default_map, name="default"),
]