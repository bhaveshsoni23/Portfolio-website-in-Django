from django.urls import path

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index,name='listings'),
    path('facedetect/', TemplateView.as_view(template_name="listings/facedetect.html"),name='facedetect'),
    path('maskdetect/', TemplateView.as_view(template_name="listings/maskDetect.html"),name='maskdetect'),
]