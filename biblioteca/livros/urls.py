from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index'),
               path('livro/<int:id>/', views.livro, name='livro'),
               path('emprestimo', views.emprestimo, name='emprestimo'),
               path('busca', views.busca, name='busca')
               ]
