from django.urls import path
from .views import home, message_list

urlpatterns = [
  path("", home, name="home"),
  path("xabarlar/", message_list, name="messages"),
]