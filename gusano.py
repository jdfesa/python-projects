import shutil   # Módulo para operaciones de archivos (copiar, mover, etc.)
import sys      # Permite acceder a los argumentos que pasamos al script por consola
import os       # Sirve para manejar nombres de archivos, rutas, extensiones, etc.

# Verificamos que el script reciba exactamente 1 argumento adicional (además del nombre del script)
if len(sys.argv) != 2:
    print("Uso: python copia.py <cantidad>")  # Mensaje de ayuda
    sys.exit(1)  # Terminamos el programa con error

# Intentamos convertir el argumento en un número entero
try:
    cantidad = int(sys.argv[1])  # Cantidad de copias a crear
except ValueError:               # Si no se puede convertir (ej: "hola")
    print("El argumento debe ser un número entero")
    sys.exit(1)  # Salimos con error

# Obtenemos el nombre del script y su extensión por separado
# Ejemplo: "copia.py" -> nombre="copia", ext=".py"
nombre, ext = os.path.splitext(sys.argv[0])

# Creamos tantas copias como indicó el usuario
for i in range(cantidad):
    # Nuevo nombre: copia_0.py, copia_1.py, ...
    nuevo_nombre = f"{nombre}_{i}{ext}"

    # Copiamos el archivo original (este script mismo) con el nuevo nombre
    shutil.copy(sys.argv[0], nuevo_nombre)

    # Mostramos en consola lo que se ha creado
    print(f"Creado: {nuevo_nombre}")

