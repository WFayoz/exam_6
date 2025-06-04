from django.urls import path

from app.views import homeView, reviewView, aboutUs

urlpatterns = [
    path('', homeView, name='home'),
    path('review', reviewView, name='review'),
    path('we', aboutUs, name='about')
]
