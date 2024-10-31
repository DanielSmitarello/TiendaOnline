class Carro:
    def __init__(self, request):
        self.request = request  # Guarda el objeto request para usarlo en la clase
        self.session = request.session  # Guarda la sesión del usuario
        carro = self.session.get('carro')  # Intenta obtener el carrito de la sesión actual
        if not carro:
            carro = self.session['carro'] = {}  # Si no existe, crea un carrito vacío en la sesión
        else:
            self.carro = carro  # Si existe, asigna el carrito obtenido a la variable de instancia

    def agregar(self, producto):
        if str(producto.id) not in self.carro.keys():  # Verifica si el producto no está en el carrito
            self.carro[producto.id] = {  # Si no está, lo agrega al carrito con sus detalles
                'producto_id': producto.id,  # Guarda el ID del producto
                'nombre': producto.nombre,  # Guarda el nombre del producto
                'precio':str(producto.precio),
                'cantidad': 1,  # Inicializa la cantidad del producto en 1
                'imagen': producto.imagen.url,  # Guarda la URL de la imagen del producto
            }
        else:
            for clave, valor in self.carro.items():
                if clave==str(producto.id):
                    valor['cantidad']=valor['cantidad']+1
                    break
        self.guardar_carro() 
        
    def guardar_carro(self):
        self.session['carro'] = self.carro 
        self.session.modified = True
    
    def eliminar_carro(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
    
    def restar_producto_carro(self,producto):
        for clave, valor in self.carro.items():
                if clave==str(producto.id):
                    valor['cantidad']=valor['cantidad']-1
                    if valor['cantidad']<1:
                        self.eliminar_carro(producto)
                    break
        self.guardar_carro()

    def limpiar_carro(self):
        carro = self.session['carro'] = {}
        self.session.modified=True

    def obtener_total_precio(self):
        total = 0
        for item in self.carro.values():
            total += float(item['precio']) * item['cantidad']
        return total

    def obtener_cantidad_articulos(self):
        total_articulos=0
        for item in self.carro.values():
            total_articulos += item['cantidad']
        return total_articulos

