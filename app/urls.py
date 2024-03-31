from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("", views.index, name='index'),
    path("mail/", views.Contactview.as_view(), name ='mail')

]