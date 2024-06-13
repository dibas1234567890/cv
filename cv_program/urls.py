from django.contrib import admin
from django.urls import path

from cv_program.views.resume_downloader import resume_downloader_view


urlpatterns = [
    path("", resume_downloader_view.index, name='index'),
    path("download", resume_downloader_view.cv_exporter , name='download'),
] 