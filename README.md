# 🔐 Generador de Diccionarios de Contraseñas

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Status](https://img.shields.io/badge/Estado-Activo-green) ![License](https://img.shields.io/badge/Licencia-MIT-brightgreen)

## 📌 Descripción

Este script en Python genera diccionarios de contraseñas basados en patrones comunes. Usa nombres, apellidos y fechas de nacimiento para crear combinaciones que podrían ser utilizadas como contraseñas por muchas personas.

📜 **Principales características:**
- Generación de combinaciones basadas en **nombre y apellidos**.
- Inclusión de **hijos** en la generación de claves.
- Añadido de **números y caracteres especiales**.
- Variantes con mayúsculas y minúsculas.
- Guarda el resultado en un archivo `.txt`.

## 🚀 Instalación y Uso

### **1️⃣ Requisitos**
Asegúrate de tener **Python 3.x** instalado. Puedes verificarlo con:
```
python --version
```
### **2️⃣ Clonar el repositorio**
```
git clone https://github.com/tu-usuario/generador-diccionarios.git
cd generador-diccionarios
```
###3️⃣ Ejecutar el script
```
python generador.py
```
## ⚙️ Ejemplo de Uso
El programa solicitará información como nombre, apellidos y fecha de nacimiento:
```
Nombre: Juan
Primer apellido: Pérez
Segundo apellido: Gómez
Año de nacimiento (YYYY): 1987
¿Tiene hijos? (s/n): s
¿Cuántos hijos tiene?: 2
Nombre del hijo: Carolina
Nombre del hijo: Miguel
```
### **🔹 Salida generada en diccionario.txt:**

```
JuPeGo87
jupego87!
CarMi87
carMi87$
```

## 📄 Licencia
Este proyecto está bajo la licencia MIT

##📬 Contacto
Si tienes sugerencias o mejoras, ¡haz un pull request o contáctame en GitHub! 🚀
