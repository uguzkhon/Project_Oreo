from django.urls import path
from . import views

urlpatterns = [
    path('', views.hame_page),
    path('about-us', views.about_page),
    path('contacts', views.contact_page)
]
