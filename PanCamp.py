import json
def abrirarchivo():
    mijson=[]
    with open("productos.json",encoding="utf-8")as openfile:
        mijson=json.load(openfile)
    return mijson
def guardarArchivo(midata):
    with open("productos.json","w")as outfile:
        json.dump(midata,outfile)
class clientes:
    def __init__(self, id, nombre, direccion):
        self.id=id
        self.nombre=nombre
        self.direccion=direccion
        print(clientes)
class empleados:
    def __init__(self, id, nombre_vendedor, cargo):
        self.id=id
        self.nombre_vendedor=nombre_vendedor
        self.cargo=cargo
class productos:
    def __init__(self, id, nombre_producto, cantidad, precio):
        self.id=id
        self.nombre_producto=nombre_producto
        self.cantidad=cantidad
        self.precio=precio
class ruta:
    def __init__(self, nombre, modulo):
        self.nombre=nombre
        self.modulo=modulo
        self.cliente=[]
    def agregarCliente(self, clinete):
        if len(self.cliente)<20:
            self.camper.append(clientes)
            return True
        else:
            return False
class pancamp:
    def __init__(self, id, nombre, direccion):
        self.id=id
        self.nombre=nombre
        self.direccion=direccion
    def estadoclientes(self, nombre, direccion):
        print("estado de los clientes: ")
        for cliente in clientes:
            print(f"Nombre: {cliente.nombre}{cliente.direccion}-estado:{cliente.estado}")
    def estadoempleados(self, nombre_vendedor, cargo):
        print("estado de los empleados: ")
        for empleado in empleados:
            print(f"Nombre: {empleado.nombre_vendedor}{empleado.cargo}-estado: {empleados.estado}")
    def estadoproductos(self, nombre_producto, cantidad, precio):
        print("estado de los productos: ")
        for producto in productos:
            print(f"Nombre: {producto.nombre_producto}{producto.cantidad}{producto.precio}-estado:{producto.estado}")
    def eliminarcliente(self, listacliente):
        idcliente=input("por favor ingrese el id del cliente que desea eliminar: ")
        for cliente in listacliente:
            if cliente.id==idcliente:
                listacliente.remove(cliente)
                print("Cliente eliminado exitosamente")
                return
            print("No se encontro ningún cliente con ese id")
    def eliminarproducto(self, listaproductos):
        idproducto=input("ingrese el id del producto que desea eliminar: ")
        for producto in listaproductos:
            if producto.id==idproducto:
                listaproductos.remove(producto)
                print("Producto eliminado exitosamente")
                return
            print("No se encontro ningún producto con ese id")
class reporte:
    def __init__(self):
        self.clientes=[]
        self.empleados=[]
        self.productos=[]
        self.ruta=[]
        self.pancamp=pancamp("2", "yessica","el puerto")
    def clientenuevo(self, cliente):
        self.cliente.append(cliente)
    def rutanueva(self, ruta):
        rutanueva=ruta(id, nombre)
        self.ruta.append(rutanueva)
    def clienteruta(self, cliente, rutanombre):
        for rutas in self.ruta:
            if ruta.agregarCliente(cliente):
                return True
            else:
                return False
    def empleadonuevo(self, empleado):
        self.cliente.append(empleado)
    def rutanueva(self, ruta):
        rutanueva=ruta(id, nombre, )
        self.ruta.append(rutanueva)
    def empleadoruta(self, empleado, rutanombre):
        for rutas in self.ruta:
            if ruta.agregarempleado(empleado):
                return True
            else:
                return False
    def productonuevo(self, producto):
        self.producto.append(producto)
    def rutanueva(self, ruta):
        rutanueva=ruta(id, nombre)
        self.ruta.append(rutanueva)
    def productoruta(self, producto, rutanombre):
        for rutas in self.ruta:
            if ruta.agregarproducto(producto):
                return True
            else:
                return False
    print("----- MENU -----")
    print("1. cliente")
    print("2. empleado")
    print("3. producto")
    print("4. salir")
opc=input("Elige una de las opciones: ")
if opc=="1":
    print("---- Menu Clientes ----")
    print("1. revisar informacion")
    print("2. salir")
    x=int(input("Elige una de las opciones: "))
    if x==1:
        miinfo=abrirarchivo()
        for i in miinfo[0]["cliente"]:
            print("-------------------")
            print("ID:",i["id"])
            print("Nombre:",i["nombre"])
            print("Direccion",i["direccion"])
    elif x==2:
        print("Hata luego, vuelve pronto")
elif opc=="2":
    miinfo=abrirarchivo()
    print("----- Menu empleados ----")
    print("1. estado de los empleados")
    print("2. salir")
    x=int(input("Elige una de las opciones: "))
    if x==1:
        print("1. crupo 1")
        print("2. grupo 2")
        grupo=int(input("Elige una de la opciones: "))
        miinfo=abrirarchivo()
        if grupo==1:
            print("este es el estado de los empleados en el grupo 1")
            for empleado in miinfo[0]["empleados"]:
                if empleado["grupo"]=="1":
                    print(f"Nombre:{empleado["nombre"]}, estado:{empleado["estado"]}")
        elif grupo ==2:
            print("este es el estado de los empleados del grupo 2: ")
            for empleado in miinfo[0]["empleados"]:
                if empleado["grupo"]=="2":
                    print(f"Nombre: {empleado["nombre"]}, estado:{empleado["estado"]}")
        elif x==4:
            print("hasta luego, vuelve pronto")
    elif opc=="3":
        print("--------Menú pancamp----------")
        print("1. Registrar cliente")
        print("2. Actualizar datos nuevos del empleado")
        print("3. Reporte empleados")
        print("4. Eliminar clientes")
        print("7. Salir del programa")
        x=int(input("Elige una de nuestras opciones: "))
        if x==1:
            id=int(input("ingrese el id del nuevo cliente: "))
            nombre=int(input("ingrese el nombre del nuevo cliente: "))
            direccion=int(input("ingrese la direccion del nuevo cliente: "))
            nuevo_cliente={
                "id":id,
                "nombre":nombre,
                "direccion":direccion,
            }
            miinfo=abrirarchivo()
            miinfo[0]["clientes"].append(nuevo_cliente)
            guardarArchivo(miinfo)
            print("el nuevo cliente se ha registrado exitosamente")
        elif x==2:
            miinfo=abrirarchivo()
            idempleado=int(input("ingrese el id del empleadoque desea actualizar datos: "))
            empleadoEncontrado=None
            for empleado in miinfo[0]["empleados"]:
                if empleado["id"]==idempleado:
                    empleadoEncontrado=empleado
                    break
            if empleadoEncontrado:
                print("seleccione cual de los datos desea actualizar: ")
                print("1. nombre")
                print("2. cargo")
                opc=int(input("ingrese la opcion que desea acrualizar: "))
                if opc==1:
                    nuevonombre=input("ingrese el nuevo nombre del empleado: ")
                    empleadoEncontrado["nombre"]=nuevonombre
                elif opc==2:
                    nuevocargo=("ingrese el nuevo cargo del empleado: ")
                    empleadoEncontrado["cargo"]=nuevocargo
                else:
                    print("esa opcion no existe, por favor elige otra")
                guardarArchivo(miinfo)
                print("los datos se han actualizado exitosamente")
            else:
                print("no se encontro ningun empleado con ese id")
        elif x==3:
            miinfo=abrirarchivo()
            print("reporte de los empleados: ")
            empleadoslaborando= False
            for empleado in miinfo[0]["empleados"]:
                if empleado["estado"]=="laborando":
                    print(f"Nombre: {empleado["nombre"]}")
                    print(f"estado: {empleado["estado"]}")
                    print("-------------------")
                    empleadoslaborando=True
            if not empleadoslaborando:
                print("no hay empleados laborando actualmente")
        elif x==4:
            miinfo=abrirarchivo()
            eliminarempleado=input("ingrese el id del cliente que desea eliminar: ")
            empleadoEncontrado= False
            for grupo in miinfo:
                for empleado in grupo["empleados"]:
                    if empleado ["id"]==eliminarempleado:
                        grupo["empleados"].remove(empleado)
                        empleadoEncontrado=True
                        break
                if empleadoEncontrado:
                    break
            if empleadoEncontrado:
                guardarArchivo(miinfo)
                print("el empleado ha sido eliminado exitosamente")
            else:
                print("el empleado no ha sido encontrado")
    elif opc=="4":
        print("Gracias pot usar nuestro programa, vuelve pronto.")
