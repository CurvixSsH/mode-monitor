# Mode-monitor
Modo monitor: Potente herramienta de hacking que permite capturar y analizar paquetes en redes inalámbricas sin restricciones. Ideal para descubrir vulnerabilidades, interceptar comunicaciones y realizar ataques. Uso responsable y ético es fundamental, cumpliendo las leyes y regulaciones aplicables.

# MON.PY

Este script te permite cambiar el modo de red de una interfaz de red específica a modo monitor. Utiliza la biblioteca subprocess para ejecutar los comandos necesarios.

Para utilizar este script, sigue los siguientes pasos:
1. Ejecuta el script.
2. Ingresa el nombre de la interfaz de red cuando se te solicite.
3. El script desactivará la interfaz de red, la renombrará agregando "mon" al nombre original y la volverá a activar en modo monitor.

Nota: Este script requiere privilegios de sudo para ejecutar los comandos de configuración de red.

# EJEMPLO DE USO:
git clone

cd mode-monitor

$ python mon.py

Ingresa el nombre de la red: Ejemplo = wlan0

Una vez ejecutado, el script realizará la configuración necesaria y mostrará el estado actual de las interfaces de red utilizando el comando `iwconfig`.

Asegúrate de tener los permisos necesarios y de comprender las implicaciones de cambiar el modo de red antes de ejecutar este script.

# SISTEMAS COMPATIBLES= DEBIAN

 1. Kali linux
 2. Ubuntu
