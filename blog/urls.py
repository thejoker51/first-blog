
# impor url and views for blog app
from django.conf.urls import url
from . import views

# post_list is the name of the URL that will identify the view
urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]