from django.conf.urls import url
from second_app import views
app_name = 'second_app'

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^user_logout/', views.user_logout,name='user_logout'),
    url(r'^registration/', views.registration_view,name='registration_view'),
    url(r'^cbview/', views.CBView.as_view(),name='cbview'),
    url(r'^template_view/', views.TemplatePageView.as_view(),name='template_view'),
    url(r'^school_list_view/', views.SchoolListView.as_view(),name='school_list_view'),
    url(r'^school/(?P<pk>\d+)/$', views.SchoolDetailView.as_view(),name='school_detail_view'),
    url(r'^school_create/$', views.SchoolCreateView.as_view(),name='school_create_view'),
    url(r'^student_create/$', views.StudentCreateView.as_view(),name='student_create_view'),    
    url(r'^school_update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(),name='school_update_view'),
    url(r'^school_delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(),name='school_delete_view'),

]
