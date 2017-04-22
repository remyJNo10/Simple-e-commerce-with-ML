from django.conf.urls import url
from . import views

app_name = 'homepage'

urlpatterns = [
    url(r'^$', views.ShowHomepage, name='ShowHomepage'),
    url(r'^product/(?P<name>.*)/buy$', views.buy,name = 'buy'),
    url(r'^product/(?P<name>.*)/', views.ShowProduct, name="showProduct"),
]