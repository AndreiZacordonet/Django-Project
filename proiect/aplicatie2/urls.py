from django.urls import path

from aplicatie2 import views

app_name = 'companies'

urlpatterns = [
    path('', views.CompaniesView.as_view(), name='lista_companii'),
    path('adaugare/', views.CreateCompanieView.as_view(), name='Adauga'),
    path('<int:pk>/update/', views.UpdateCompanieView.as_view(), name='Modifica'),
    path('<int:pk>/stergere/', views.delete_companie, name='Sterge'),
    path('<int:pk>/activeaza/', views.activate_companie, name='Activeaza'),
]
