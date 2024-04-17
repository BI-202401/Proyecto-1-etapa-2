from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('predict/', views.review_list, name='review_list'),
    path('predict/bad', views.review_list_bad, name='review_list'),
    path('predict/good', views.review_list_good, name='review_list'),
    path('predict/medium', views.review_list_3, name='review_list'),
    path('predict/1', views.review_list_1, name='review_list'),
    path('predict/2', views.review_list_2, name='review_list'),
    path('predict/3', views.review_list_3, name='review_list'),
    path('predict/4', views.review_list_4, name='review_list'),
    path('predict/5', views.review_list_5, name='review_list'),
    path('predict/all', views.review_list_all, name='review_list'),
    path('reviewgroup/', views.review_group),
    path('reviewcreate/', csrf_exempt(views.review_create),
         name='reviewCreate'),
]
