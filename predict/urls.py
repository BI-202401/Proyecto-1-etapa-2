from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('predict/', views.review_list, name='review_list'),
    path('reviewgroup/', views.review_group),
    path('reviewcreate/', csrf_exempt(views.review_create),
         name='reviewCreate'),
]
