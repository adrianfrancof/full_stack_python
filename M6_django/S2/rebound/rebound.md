###### versión de python
```
python --version
```
###### listar paquetes instalados
```
pip list
```
###### ejecutar instalador de paquetes
```
pip --version
```
###### actualizar pip
```
python.exe -m pip install --upgrade pip
```
###### crear un entorno virtual
> abrir carpeta en la terminal donde se quiera generar el entorno local
> cd nombre_carpeta_entorno_local
> cd .. # para ir a la carpeta anterior
> ls    # verificar que estamos en la carpeta correcta
> pwd   # verificar ruta actual
> abrir con click derecho una terminal en visual estudio code

```
python -m venv env
python -m venv nombre_entorno
python -m venv proyecto_django
```
###### ejecutar entorno virtual
> windows:
```
nombre_entorno\Scripts\activate.ps1
nombre_entorno\Scripts\activate
```
> linux:
```
nombre_entorno/bin/activate.ps1
```
###### desactivar entorno virtual
```
deactivate
```
##### obtener y cambiar la poliza de ejecución de script en powershell
```
Get-ExecutionPolicy
```
> abrir powershell como administrador

> ejecutar para dar permisos de ejecución de scripts
```
Set-ExecutionPolicy RemoteSigned
```
###### listar paquetes instalados
```
pip list
```
###### instalar django en el entorno virtual mediante el instalador de paquetes (pip)
```
pip install django
```
###### listar paquetes instalados
```
pip list
```
###### comando de ayuda pip
```
pip help
```
###### conocer el entorno global
```
python -c "import sys; print(sys.executable)"
```