from django.urls import path,include
from .views import HomePageView

urlpatterns = [
    path('home/',HomePageView.as_view(),name='home'),
    path('',HomePageView.as_view(),name='book_list'),
]
