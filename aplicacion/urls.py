from django.urls import path, include
from .views import*
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', home, name="home"),
    path('producto/', productos, name="productos"),
    path('acerca/', acerca, name="acerca"),
    path('proveedor/', proveedor, name="proveedor"),
    path('clientes/', clientes, name="clientes"),
    path('producto_form/', productoForm, name="producto_form"),
    path('agregar_producto/', agregarProducto2, name="agregar_producto"),
    path('producto/', views.productos, name="productos"),
    path('proveedor/', views.proveedor, name="proveedor"),
    path('clientes/', views.clientes, name="clientes"),
    path('agregar_cliente/', agregarCliente, name="agregar_cliente"),
    path('buscar_cliente/', buscarCliente, name="buscar_cliente"),
    path('buscar_producto/', buscarProducto, name="buscar_producto"),
    path('buscar3/', buscar3, name="buscar3"),
    path('buscar2/', buscar2, name="buscar2"),
    path('agregar_proveedor/', agregarProveedor, name="agregar_proveedor"),
    path('buscar_proveedor/', buscarProveedor, name="buscar_proveedor"),
    path('buscar4/', buscar4, name="buscar4"),
    path('update_producto/<id_producto>', updateProducto, name="update_producto"),
    path('delete_producto/<id_producto>', deleteProducto, name="delete_producto"),
    path('update_cliente/<int:pk>', ClienteUpdate.as_view(), name="update_cliente"),
    path('delete_cliente/<int:pk>', ClienteDelete.as_view(), name="delete_cliente"),
    path('update_proveedor/<int:pk>', ProveedorUpdate.as_view(), name="update_proveedor"),
    path('delete_proveedor/<int:pk>', ProveedorDelete.as_view(), name="delete_proveedor"),
    path('login/', login_request, name="login" ),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout" ),
    path('registro/', register, name="registro" ),
    path('editar_perfil/', editarPerfil, name="editar_perfil" ),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar" ),


]
