from django.conf.urls import url

from . import views

app_name = 'login'

urlpatterns = [
    url(r'^$', views.ShowLogin, name='ShowLogin'),
    url(r'^register/$', views.MakeRegistration, name="MakeRegistration"),
    url(r'^login/$', views.Login, name="Login")
]