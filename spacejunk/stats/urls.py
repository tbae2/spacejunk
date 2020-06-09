from django.urls import path
from . import views

urlpatterns = [
    path('',views.StatsView.as_view(),name='stats'),
    path('api/loadlaunchsites',views.importLaunchSite,name='load-launch-site'),
    path('api/loadcountryscore',views.importCountryScore,name='load-country-score')
]
