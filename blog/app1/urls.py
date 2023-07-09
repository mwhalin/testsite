

from django.urls import include, path

from .import views

urlpatterns = [

    path('post_list/',views.post_list),
    path('post/<int:pk>/', views.post_detail , name='post_detail'),
    path('test/',views.test),
    path('post/new/', views.post_new, name='post_new'),


]