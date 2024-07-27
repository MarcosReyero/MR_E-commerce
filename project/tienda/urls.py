from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'carritos', views.CarritoViewSet)
router.register(r'pedidos', views.PedidoViewSet)
router.register(r'pedido-productos', views.PedidoProductoViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('producto/<int:id>/', views.producto_detalle, name='producto_detalle'),
    path('carrito/', views.carrito, name='carrito'),
    path('checkout/', views.checkout, name='checkout'),
    path('api/', include(router.urls)),
]
