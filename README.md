# Sistema de Gestión para Tienda

## Descripción

Este proyecto consiste en un sistema de gestión para una tienda desarrollado en Python. Su propósito es facilitar la administración de clientes, productos, inventario y ventas mediante una aplicación de consola organizada en módulos.

La información se almacena en archivos JSON, permitiendo conservar los datos registrados entre ejecuciones. Además, el sistema genera facturas en formato TXT para cada venta realizada.

---

## Funcionalidades

### Gestión de Clientes

* Registro de clientes.
* Consulta de clientes registrados.
* Búsqueda por NIT o nombre.
* Actualización de información de contacto.
* Eliminación de clientes sin historial de ventas.

### Gestión de Productos

* Registro de productos.
* Consulta del inventario.
* Búsqueda de productos por código o nombre.
* Actualización de precios.
* Ajuste de existencias.
* Control de stock mínimo.
* Eliminación de productos sin ventas registradas.
* Exportación del inventario a formato CSV.

### Gestión de Ventas

* Registro de ventas.
* Manejo de carrito de compras.
* Validación de stock disponible.
* Cálculo automático de subtotal, IVA y total.
* Actualización automática del inventario.
* Generación de facturas.
* Almacenamiento del historial de ventas.

### Control de Acceso

* Inicio de sesión mediante usuario y contraseña.
* Acceso para administrador y cajero.

---

## Estructura del Proyecto

```text
proyecto-progra-pos/

├── main.py
├── modulos/
│   ├── archivos.py
│   ├── clientes.py
│   ├── productos.py
│   ├── ventas.py
│   └── utilidades.py
├── datos/
│   ├── clientes.json
│   ├── productos.json
│   └── ventas.json
├── facturas/
└── README.md
```

---

## Requisitos

* Python 3.10 o superior.

Verificar la versión instalada:

```bash
python --version
```

---

## Instalación y Ejecución

### Clonar el repositorio

```bash
git clone https://github.com/jsaccastro-sketch/proyecto-progra-pos.git
```

### Ingresar a la carpeta del proyecto

```bash
cd proyecto-progra-pos
```

### Ejecutar el sistema

```bash
python main.py
```

---

## Usuarios de Acceso

| Usuario | Contraseña | Rol           |
| ------- | ---------- | ------------- |
| admin   | 1234       | Administrador |
| cajero  | 1234       | Cajero        |

---

## Almacenamiento de Datos

El sistema utiliza archivos JSON para almacenar la información de manera persistente.

### clientes.json

Contiene la información de los clientes registrados:

* NIT
* Nombre
* Teléfono
* Correo electrónico

### productos.json

Contiene la información del inventario:

* Código
* Nombre
* Categoría
* Precio
* Stock disponible
* Stock mínimo

### ventas.json

Contiene el historial de ventas realizadas:

* Identificador de venta
* Fecha y hora
* Cliente asociado
* Productos vendidos
* Subtotal
* IVA
* Total

---

## Facturas

Cada venta confirmada genera automáticamente una factura en formato TXT dentro de la carpeta:

```text
facturas/
```

Las facturas incluyen:

* Número de venta.
* Fecha y hora.
* NIT del cliente.
* Productos vendidos.
* Subtotal.
* IVA.
* Total de la compra.

---

## Tecnologías Utilizadas

* Python 3
* JSON
* Programación Modular
* Git
* GitHub

---

## Evidencias de Funcionamiento

### Inicio de Sesión

<img width="658" height="318" alt="imagen" src="https://github.com/user-attachments/assets/cf88ab12-5125-4ac0-9291-e4d3a2e705a8" />


### Menú Principal

<img width="400" height="190" alt="imagen" src="https://github.com/user-attachments/assets/ab6edaeb-cf1a-4e1e-b6d9-b6f016dae824" />
<img width="401" height="158" alt="imagen" src="https://github.com/user-attachments/assets/9ac5198b-165f-44c9-9257-56b3bfe63e07" />


### Gestión de Clientes

<img width="333" height="236" alt="imagen" src="https://github.com/user-attachments/assets/9f402e70-8129-4ca1-8599-7f029f80ac42" />


### Gestión de Productos

<img width="370" height="265" alt="imagen" src="https://github.com/user-attachments/assets/e76a50b5-276c-4c63-8f23-3b677a2593de" />


### Registro de Ventas

<img width="300" height="120" alt="imagen" src="https://github.com/user-attachments/assets/97c50a83-cf40-415e-ac15-d3afac6053d2" />


### Factura Generada

<img width="474" height="354" alt="imagen" src="https://github.com/user-attachments/assets/41b6bc06-741a-40b2-9e21-63910db04b65" />


---

## Autores

* Josue Saul Sac Castro
* Matias Tello Alvarado
* Jose Manuel Lopez Lopez

---

## Observaciones

Proyecto desarrollado con fines académicos para aplicar conceptos de programación modular, manejo de archivos JSON, validación de datos y desarrollo de aplicaciones en Python.
