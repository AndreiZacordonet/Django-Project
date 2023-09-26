from django.urls import path

from aplicatie1 import views

app_name = 'locations'

urlpatterns = [
    path('', views.LocationsView.as_view(), name='lista_locatii'),  #url gol care prea ruta principala (in cazul nostru "locations/")
    path('adaugare/', views.CreateLocationView.as_view(), name='Adauga'),
    path('<int:pk>/update/', views.UpdateLocationView.as_view(), name='Modifica'),   #<int:pk> inseamna ca primary key este de tip int
    path('<int:pk>/stergere/', views.delete_location, name='Sterge'),
    path('<int:pk>/activeaza/', views.activate_location, name='Activeaza'),
]