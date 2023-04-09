from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name = 'index'),
    path('<str:name>',views.greeting,name = 'greeting'), #could be used to send data from url to backend.
]