#!/bin/bash

# Verifica si el usuario tiene permisos de superusuario
if [ "$EUID" -ne 0 ]; then
  echo "Este script debe ejecutarse con privilegios de superusuario. Usa sudo."
  exit 1
fi

# Obtiene la ruta del directorio del script
carpeta_a_copiar="$(cd "$(dirname "$0")" && pwd)"

# Verifica si la carpeta de origen existe
if [ ! -d "$carpeta_a_copiar" ]; then
  echo "La carpeta '$carpeta_a_copiar' no existe."
  exit 1
fi

# Ruta de destino (en este caso, /usr/bin)
destino="/usr/bin"

# Verifica si la carpeta de destino existe
if [ -d "$destino/mdadm-notify" ]; then
  rm -rf "$destino/mdadm-notify"
fi

# Copia la carpeta al destino
cp -r "$carpeta_a_copiar" "$destino"

# Verifica si la operación de copia fue exitosa
if [ $? -eq 0 ]; then
  echo "Carpeta copiada exitosamente a $destino."
else
  echo "Error al copiar la carpeta a $destino."
  exit 1
fi

#Establece permisos
chmod 700 -R "$destino/mdadm-notify"
exit 0