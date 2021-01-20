from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # ex: /5/
    path('<str:question_str>/', views.str, name='str'),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]