from django.urls import include,path
from rest_framework import routers
from .views import *
router=routers.DefaultRouter()
router.register(r'mg', MgViewset)
router.register(r'ss', ssviewset)

urlpatterns = [
   path('', include(router.urls)),
]