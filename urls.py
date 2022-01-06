from rest_framework import routers
from .views import *

app_name = 'itemsapp'

router = routers.SimpleRouter()
router.register(r'products', StudentCurd, basename="products")
urlpatterns = router.urls
