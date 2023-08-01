from django.urls import path
from app2.views import * 
app_name = 'app2'

urlpatterns=[
    path('anime_list/',anime_list,name='anime_list'),
]