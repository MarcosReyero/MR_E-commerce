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
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('admin-custom/', views.admin_panel, name='admin_panel'), 
    path('add-product/', views.add_product, name='add_product'),  
    path('view-products/', views.view_products, name='view_products'),  
    path('edit-product/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:pk>/', views.delete_product, name='delete_product'),]


