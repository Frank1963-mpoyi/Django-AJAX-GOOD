
from django.urls import path
from .views import home, save_data




urlpatterns = [
    path('', home),
    path('save', save_data, name="save"),# we pass this url to ajax post
    path('delate', save_data, name="delete")
]
