from django.urls import path,include
from .views import ProjectViewset,main
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('/main',main)
# ]

router = DefaultRouter()
router.register('project',ProjectViewset, basename='project')
urlpatterns = router.urls
