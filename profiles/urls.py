from django.urls import path
from profiles.views import *

urlpatterns = [
    path('create-profile', create_profile, name="create-profile" ),
    
]