from incomechecker.views import MonthlyPayViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path
from incomechecker import views
router = DefaultRouter()
router.register(r'', MonthlyPayViewSet, base_name='MonthlyPay')
urlpatterns = router.urls


urlpatterns = [
    path('chart', views.chart, name='chart'),
    
]