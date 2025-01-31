from django.urls import path
from . import views
<<<<<<< HEAD
urlpatterns = [
    path('', views.index, name='movies.index'),
    path('<int:id>/', views.show, name='movies.show'),
    path('<int:id>/review/create/', views.create_review,
        name='movies.create_review'),
    path('<int:id>/review/<int:review_id>/edit/',
        views.edit_review, name='movies.edit_review'),
    path('<int:id>/review/<int:review_id>/delete/',
        views.delete_review, name='movies.delete_review'),
]
=======

urlpatterns = [
    path('', views.index, name='movies.index'),
    path('<int:id>/', views.show, name='movies.show'),
    path('<int:id>/review/create/', views.create_review, name='movies.create_review'),
    path('<int:id>/review/<int:review_id>/edit/', views.edit_review, name='movies.edit_review'),
    path('<int:id>/review/<int:review_id>/delete/', views.delete_review, name='movies.delete_review'),
]
>>>>>>> 34cdd02e7b63105c3685ae56cab15bcfcdf10102
