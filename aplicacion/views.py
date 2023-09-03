from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import*
from .forms import*
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth       import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, "aplicacion/home.html")      
@login_required
def acerca(request):
    return render(request, "aplicacion/acerca.html")  
@login_required
def productos(request):

    contexto = {'productos': Producto.objects.all(), 'titulo':'Listado de Productos' }
    return render(request, "aplicacion/productos.html", contexto)
@login_required
def proveedor(request):
    return render(request, "aplicacion/proveedor.html")
@login_required
def clientes(request):

    contexto = {'clientes': Cliente.objects.all(), 'titulo':'Listado de Clientes' }
    return render(request, "aplicacion/clientes.html", contexto)
@login_required
def productoForm(request):
    if request.method == "POST":
        producto = Producto(nombre=request.POST['nombre'],
                            numero=request.POST['numero'],
                            stock=request.POST['stock'],)
        producto.save()
        
    return render(request, "aplicacion/agregarProdructo2.html")


@login_required
def agregarProducto2(request):
    miForm = None  
    
    if request.method == "POST":
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto_nombre = miForm.cleaned_data.get('nombre')
            producto_numero = miForm.cleaned_data.get('numero')
            producto_stock = miForm.cleaned_data.get('stock')
            producto = Producto(nombre=producto_nombre, numero=producto_numero, stock=producto_stock)
            producto.save()
            
          
            return redirect('productos') 
    else:
        miForm = ProductoForm()

    return render(request, "aplicacion/agregarProducto2.html", {"form": miForm})
@login_required
def agregarCliente(request):
    miForm2 = None
    if request.method == "POST":
        miForm2 = ClienteForm(request.POST)
        if miForm2.is_valid():
            cliente_nombre = miForm2.cleaned_data.get('nombre')
            cliente_apellido = miForm2.cleaned_data.get('apellido')
            cliente_email = miForm2.cleaned_data.get('email')
            cliente = Cliente(nombre=cliente_nombre, apellido=cliente_apellido, email=cliente_email)
            cliente.save()
            
           
            return redirect('clientes')
    else:
        miForm2 = ClienteForm()

    return render(request, "aplicacion/agregarCliente.html", {"form": miForm2})
@login_required   
def buscarCliente(request):
    return render(request, "aplicacion/buscarCliente.html")
@login_required
def buscar3(request):
    if 'buscar' in request.GET:
        patron = request.GET['buscar']
        clientes = Cliente.objects.filter(nombre__icontains=patron)
        contexto = {"clientes": clientes, 'titulo': 'El resultado de tu búsqueda', 'mensaje': ''}
        
        if clientes.exists():
            mensaje = f"Se encontraron {clientes.count()} cliente(s) con el dato '{patron}'"
        else:
            mensaje = f"No se encontraron clientes con el dato '{patron}'"
        
        contexto['mensaje'] = mensaje
        return render(request, "aplicacion/clientes.html", contexto)
   
    return HttpResponse("No se ingresó nada para buscar")
@login_required    
def buscarProducto(request):
    return render(request, "aplicacion/buscarProducto.html")
@login_required    
def buscar2(request):
    if 'buscar' in request.GET:
        patron = request.GET['buscar']
        productos = Producto.objects.filter(nombre__icontains=patron)
        contexto = {"productos": productos, 'titulo': 'Resultado de la búsqueda de productos', 'mensaje': ''}
        
        if productos.exists():
            mensaje = f"Se encontraron {productos.count()} producto(s) con el dato '{patron}'"
        else:
            mensaje = f"No se encontraron productos con el dato '{patron}'"
        
        contexto['mensaje'] = mensaje
        return render(request, "aplicacion/productos.html", contexto)
   
    return HttpResponse("No se ingresó nada para buscar productos")
@login_required
def agregarProveedor(request):
    miForm3 = None
    if request.method == "POST":
        miForm3 = ProveedorForm(request.POST)
        if miForm3.is_valid():
            proveedor_nombre = miForm3.cleaned_data.get('nombre')
            proveedor_apellido = miForm3.cleaned_data.get('apellido')
            proveedor_email = miForm3.cleaned_data.get('email')
            proveedor= Proveedor(nombre=proveedor_nombre,
                              apellido=proveedor_apellido,
                              email=proveedor_email,)
        
            proveedor.save()
            
           
            return redirect('proveedor')  # Reemplaza 'lista_productos' con el nombre de tu vista de lista de productos
    else:
        miForm3 = ProveedorForm()

    return render(request, "aplicacion/agregarProveedor.html", {"form": miForm3})
@login_required    
def buscarProveedor(request):
    return render(request, "aplicacion/buscarProveedor.html")

@login_required
def buscar4(request):
    if 'buscar' in request.GET:
        patron = request.GET['buscar']
        proveedor = Proveedor.objects.filter(nombre__icontains=patron)
        contexto = {"proveedor": proveedor, 'titulo': 'Resultado de la búsqueda de proveedores', 'mensaje': ''}
        
        if proveedor.exists():
            mensaje = f"Se encontraron {proveedor.count()} proveedor(es) con el dato '{patron}'"
        else:
            mensaje = f"No se encontraron proveedores con el dato '{patron}'"
        
        contexto['mensaje'] = mensaje
        return render(request, "aplicacion/proveedor.html", contexto)
   
    return HttpResponse("No se ingresó nada para buscar proveedores")
@login_required
def proveedor(request):

    contexto = {'proveedor': Proveedor.objects.all(), 'titulo':'Listado de Proveedores' }
    return render(request, "aplicacion/proveedor.html", contexto)

#_____
@login_required
def updateProducto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == "POST":
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto.nombre= miForm.cleaned_data.get('nombre')
            producto.numero= miForm.cleaned_data.get('numero')
            producto.stock= miForm.cleaned_data.get('stock')
            producto.save()
            return redirect (reverse_lazy('productos'))
    else:
        miForm= ProductoForm(initial={
            'nombre':producto.nombre,
            'numero':producto.numero,
            'stock':producto.stock,
            })
        return render(request, "aplicacion/agregarProducto2.html", {'form': miForm})
@login_required    
def deleteProducto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    producto.delete()
    return redirect (reverse_lazy('productos'))


class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model=Cliente
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('clientes')

class ClienteDelete(LoginRequiredMixin,DeleteView):
    model=Cliente
    success_url = reverse_lazy('clientes')

class ProveedorUpdate(LoginRequiredMixin,UpdateView):
    model=Proveedor
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('proveedor')

class ProveedorDelete(LoginRequiredMixin,DeleteView):
    model=Proveedor
    success_url = reverse_lazy('proveedor')


#_______LOGIN_______
#
def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar

                return render(request, "aplicacion/base.html", {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son incorrectos'})
        else:
            return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son incorrectos'})

    miForm =   AuthenticationForm()      

    return render(request, "aplicacion/login.html", {"form":miForm}) 

def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "aplicacion/registro.html", {"form":miForm})

#__

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"aplicacion/base.html")
        else:
            return render(request,"aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) 
        if form.is_valid():
            u = User.objects.get(username=request.user)

            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

           
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

           
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form })
