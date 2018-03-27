from django.conf.urls import url

from . import views
app_name = 'weather'

urlpatterns = [
    url(r'^json/', views.index, name='index'),
    url(r'^$', views.first_page, name='first'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^login/',views.UserLogin, name='login'),
    url(r'^register/',views.register, name='register'),
    url(r'^logout/',views.UserLogout, name='logout'),
    url(r'^map/',views.map, name='map'),
    url(r'^dash/(?P<pid1>[0-9]+)/', views.detail, name='detail'),
    url(r'^addplant/', views.addplant, name='addplant'),
    url(r'^numplants/',views.numplants,name='numplants')
]
