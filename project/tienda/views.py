from django.shortcuts import render, get_object_or_404
from .models import Producto, Carrito, CarritoProducto, Pedido, models,Categoria, PedidoProducto
from .serializers import ProductoSerializer, CarritoSerializer, PedidoSerializer, CategoriaSerializer,PedidoProductoSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoProductoViewSet(viewsets.ModelViewSet):
    queryset = PedidoProducto.objects.all()
    serializer_class = PedidoProductoSerializer

def home(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/home.html', {'productos': productos})

def producto_detalle(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'tienda/producto_detalle.html', {'producto': producto})

def carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    return render(request, 'tienda/carrito.html', {'carrito': carrito})

def checkout(request):
    if request.method == 'POST':
        carrito = Carrito.objects.get(usuario=request.user)
        pedido = Pedido.objects.create(
            usuario=request.user,
            total=carrito.productos.aggregate(total=models.Sum('precio'))['total'],
            direccion=request.POST['direccion'],
            estado='pendiente'
        )
        for item in CarritoProducto.objects.filter(carrito=carrito):
            PedidoProducto.objects.create(
                pedido=pedido,
                producto=item.producto,
                cantidad=item.cantidad,
                precio=item.producto.precio
            )
        carrito.productos.clear()
        return render(request, 'tienda/checkout.html', {'pedido': pedido})
    return render(request, 'tienda/checkout.html')
