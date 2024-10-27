from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze'),
    path('aboutus',views.aboutus, name='About us'),
    path('contactus',views.contactus, name='Contact us')
]
