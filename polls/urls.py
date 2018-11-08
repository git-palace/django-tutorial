from django.conf.urls import url
import views

urlpatterns = [
    url('', views.index, name='index'),
    url('<int:question_id>/', views.detail, name='detail'),
    url('<int:question_id>/results', views.results, name='results'),
    url('<int:question_id>/vote', views.vote, name='vote'),
]
