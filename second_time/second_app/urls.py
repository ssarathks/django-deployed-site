from django.conf.urls import url
from second_app import views
app_name = 'second_app'

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^user_logout/$', views.user_logout,name='user_logout'),
    url(r'^registration/$', views.registration_view,name='registration_view'),    

]
