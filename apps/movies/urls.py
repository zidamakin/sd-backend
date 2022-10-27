from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieList.as_view(), name='movie_list'),
    path('<int:pk>/', views.MovieDetail.as_view(), name='movie_detail')
]