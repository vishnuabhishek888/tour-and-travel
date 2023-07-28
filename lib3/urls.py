from django .contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register('cities', Area_CitiesViewSet)
router.register('states', StateViewSet)
router.register('destination', DestinationViewSet)
router.register('pick_up', Pick_UpViewset)
router.register('drop', DropViewset)
router.register('transfer', TransferViewset)
router.register('activities', ActivitiesViewset)
router.register('Trip_Detail',Trip_DetailViewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/',include('api.urls')),
    path('', include(router.urls)),

]
