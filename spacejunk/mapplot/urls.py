from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('api/importtle/',views.importTle, name='load-tle-data'),
    path('api/importsatellites/',views.importSatellites, name='load-sat-data')
]

