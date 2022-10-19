from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.delete_post, name='delete'),
    path('update/<int:id>/', views.update_post, name='update')

]