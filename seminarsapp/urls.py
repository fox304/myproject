from django.urls import path
from seminarsapp import views

urlpatterns = [
    path('', views.random_number),
    path('number/', views.random_number, name='ran'),
    path('dice/', views.random_dice),
    path('coin/', views.random_coin),
    path('num2/', views.random_number2),
    path('dice2/', views.random_dice2),
    path('coin2/', views.random_coin2),
    path('coin3/<int:n>', views.AAA.as_view()),
    path('art/<int:id_author>/', views.view_title_articls),
    # path('art2/<int:id_article>/', views.view_articl, name='article' ),
    path('art3/<int:id_article>/', views.view_articl, name='article3' ),
    path('random_all/', views.random_all, name='random_all' ),
    path('new_author_form/', views.new_author_form, name='new_author' ),
    path('new_article_form/', views.new_article_form, name='new_articl' ),


]