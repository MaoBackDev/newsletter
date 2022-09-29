from django.urls import path

from .views import *

app_name = 'newsletter'
urlpatterns = [
    path('optin/', newsletter_signup, name='optin'),
    path('unsuscribe/', newsletter_unsuscribe, name='unsuscribe'),
]