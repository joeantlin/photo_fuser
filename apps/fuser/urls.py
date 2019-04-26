from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard$', views.dashboard),
    url(r'^profile$', views.profile),
    url(r'^viewimage/(?P<id>\d+)$', views.viewimage),
    url(r'^createimage$', views.createimage),
    url(r'^finalize$', views.finalize),
    url(r'^delete/(?P<type>\w+)/(?P<deleteid>\d+)$', views.delete),
]

# if settings.DEBUG:
#     #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)