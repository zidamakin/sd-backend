from django.urls import path
from .views import CategoryList

urlpatterns = [
    path('', CategoryList.as_view(), name='Category_list'),
]