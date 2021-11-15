from django.urls import path

from . import views


urlpatterns = [
    path('main_test', views.main_test, name="main_test"),
    path('main_view', views.main_view, name="main_view"),
    path('', views.default_page, name="default_page"),
    
]