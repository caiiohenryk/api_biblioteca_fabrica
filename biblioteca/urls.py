from rest_framework import routers
from .views import LivroViewSet, TituloViewSet

router = routers.DefaultRouter()
router.register(r'titulo', TituloViewSet)
router.register(r'livro', LivroViewSet)

urlpatterns = router.urls