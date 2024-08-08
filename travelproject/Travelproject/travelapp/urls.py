from . import  views
from django.urls import path

app_name = 'travelapp'
urlpatterns = [

    path('',views.demo,name='demo'),
    path('generic/',views.more,name='more'),
    path('thanks/',views.thanks,name='thanks')
]
