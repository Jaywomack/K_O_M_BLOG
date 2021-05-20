from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('postlist/', views.post_list, name='post_list'),
    path('contact/', views.contact, name='contact'),
    path('support/', views.support, name='support'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)