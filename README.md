# Project Braille
El objetivo de este proyecto es desarrollar una interfaz intuitiva para traducir texto, audios e imagenes a braille.

# Software requerido
- Qt Designer(https://build-system.fman.io/qt-designer-download)
- Python 3.9.0(https://www.python.org/downloads/)
- Visual Studio Code(https://code.visualstudio.com/)
- Poetry administrador de dependencias de python(https://python-poetry.org/)

# Instrucciones de instalación
- Paso 1 - Clonar el repositorio mediante el comando: **git clone https://github.com/Aguilerimon/ProjectBraille.git**
- Paso 2 - Posicionarse en el directorio clonado mediante una terminal o CMD de Windows
- Paso 3 - Instalaremos todas la dependencias ligadas al proyecto mediante el comando: **poetry install**
- Paso 4 - Actualizaremos las dependencias mediante el comando: **poetry update**
- Paso 5 - Para ejecutar el archivo **'main.py'** dentro del fichero 'projectbraille' se debe ejecutar el entorno virtual mediante el comando: **poetry shell**
- Paso 6 - El comando para ejecutar **'main.py'** dentro del entorno virtual es: **python main.py**

# Generalidades de desarrollo
Para poder ejecutar el programa cada vez que se realice un cambio a la interfaz grafica mediante Qt Designer es necesario convertir el archivo 'UI_Principal.ui' a un archivo del mismo nombre pero con la extension '.py'. Esto se logra mediante el siguiente comando: **pyside2-uic UI_Principal.ui > UI_Principal.py**. Un posible error a esto es que al convertir el archivo '.ui' a extension '.py', este sea codificado con UTF-16 y el interprete solo ejecuta UTF-8, esto se cambia facilmente desde VS Code desde la barra azul inferior, solo se dar clic al apartado en donde indica 'UTF-16' y cambiarlo a 'UTF-8'.
