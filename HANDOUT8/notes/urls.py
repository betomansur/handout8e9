from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/notes/<int:note_id>/', views.api_note),
    path('api/notes/', views.api_note_all),
    path('delete', views.delete_post, name='delete'),
    path('update/<int:id>/', views.update_post, name='update')

]