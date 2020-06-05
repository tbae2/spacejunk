from django.urls import path
from . import views

app_name = 'mapplot'
urlpatterns= [
    path('', views.MapPlotView.as_view(), name='index'),
    path('api/importtle/',views.importTle, name='load-tle-data'),
    path('api/importsatellites/',views.importSatellites, name='load-sat-data')
]

