from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from rest_framework import viewsets
from .models import Producto, Carrito, CarritoProducto, Pedido, Categoria, PedidoProducto
from .serializers import ProductoSerializer, CarritoSerializer, PedidoSerializer, CategoriaSerializer, PedidoProductoSerializer
from .forms import RegisterForm, ProductoForm
import logging
from django.template import TemplateDoesNotExist
from django.db.models import Sum

# Custom decorator to check if the user is a superuser
def admin_required(function=None, redirect_field_name='next', login_url='login'):
    if function is None:
        return user_passes_test(lambda u: u.is_superuser, login_url=login_url)(admin_required)
    return user_passes_test(lambda u: u.is_superuser, login_url=login_url)(function)

# Administration views
@admin_required
def admin_view(request):
    return render(request, 'admin_view.html')

@admin_required
def admin_panel(request):
    return render(request, 'tienda/admin_panel.html')

@admin_required
def add_product(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_products')
    else:
        form = ProductoForm()
    return render(request, 'tienda/add_product.html', {'form': form})

@admin_required
def view_products(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/view_products.html', {'productos': productos})

@admin_required
def edit_product(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('view_products')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'tienda/edit_product.html', {'form': form})

@admin_required
def delete_product(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('view_products')
    return render(request, 'tienda/delete_product.html', {'producto': producto})

# Authentication views
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'tienda/register.html', {'form': form})

logger = logging.getLogger(__name__)

def login_view(request):
    try:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                auth_login(request, user)
                return redirect('home')
        else:
            form = AuthenticationForm()
        return render(request, 'tienda/login.html', {'form': form})
    except TemplateDoesNotExist as e:
        logger.error(f"Template not found: {e}")
        return render(request, 'tienda/error.html', {'message': 'Template not found: login.html'})
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return render(request, 'tienda/error.html', {'message': 'An unexpected error occurred'})

def logout_view(request):
    auth_logout(request)
    return redirect('home')

# Model views
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

# General views
def home(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/home.html', {'productos': productos})

def producto_detalle(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'tienda/producto_detalle.html', {'producto': producto})

@login_required
def carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    return render(request, 'tienda/carrito.html', {'carrito': carrito})

@login_required
def checkout(request):
    if request.method == 'POST':
        carrito = get_object_or_404(Carrito, usuario=request.user)
        total = carrito.productos.aggregate(total=Sum('precio'))['total']
        pedido = Pedido.objects.create(
            usuario=request.user,
            total=total,
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
