# Patentamens

El objetivo del repositorio es poder visualizar estadisticas variadas de una instancia del juego de las patentes.

Estadisticas generales como el **número de patentes encontradas por persona** , o más copadas como **cuanto pagaría una apuesta de quien encuentra la próxima patente**. Y muchas más para sorprenderse y divertirse con tus amigos.

# ¿Que es el juego de las patentes?

Es un juego simple el cual consiste en encontrar, en orden numérico, patentes con número desde la 000 hasta la 999. Algo así como completar un albúm de figuritas.

### ¿Como se juega?
La manera más facil de empezar a jugar es creando un grupo de chat, por ejemplo en WhatsApp, con tus amigos y a partir de ahí empiezan la busqueda de la patente con número 000. Cuando alguien la encuentra, le saca una foto y la envía al grupo, a partir de ahí se puede buscar la próxima patente y se va avanzando.

### Reglas generales

La regla más importante es que no se puede sacar foto de una patente que no sea la que se está buscando. Es común, y les va a pasar, de encontrarse justo con la patente que le sigue a la que se está buscando, pero si aún no se encontró la anterior, entonces simplemente habrá que dejarla pasar y no guardarse la foto para mandarla luego de que se encuentre la actual.

### Reglas extras

Puede suceder de que las patentes del país en el que se esté jugando tengan otro tipo de formato, con más números por ejemplo. En este caso la patente solo es válida si tiene 3 o más números y los últimos 3 números son los que forman el número que se está buscando. Por ejemplo, si se está buscando la patente 010 y se encuentra una patente con el número 8010, entonces es válida. Sin embargo si se encuentra una patente con número 10, entonces no es válida.

# Recopilación de datos

Para poder lograr la generación de estadisticas y gráficos es necesario contar con los datos actuales de su juego de las patentes.
La manera más sencilla de recopilar los datos es creandose un google sheets y llenar los datos de cada patente encontrada.

Cada patente encontrada se debe llenar con los siguientes datos:

 `patente, encontradaPor, fecha, vehiculo,  horaDelDia, marca`

Ejemplo:
```
patente | encontradaPor | fecha    | vehiculo | horaDelDia | marca

000     | Juan          | 1/1/2023 | Auto     | 16         | Jeep
001     | Santi         | 2/1/2023 | Auto     | 10         | Toyota       

```
Es importante notar que no es necesario tener siempre actualizado estos datos, se puede hacer perfectamente cuando se desee ver las estadisticas en algún momento, mirando el historial de fotos del grupo.

Una vez recopiladas se debe exportar en formato *CSV* y guardado con el nombre `data.csv`, remplazando el archivo de ejemplo sobre mi juego, que viene junto al repositorio.


# Instalación

- Instalar [Python](https://www.python.org/downloads/)

- Instalar [Anaconda](https://docs.anaconda.com/free/anaconda/install/linux/) para usar los notebooks de Jupyter y las librerias necesarias. 

# Uso con VSCode

- Desde VSCode, abrir el archivo `patentamens.ipynb`

- Seleccionar el interprete de Python que viene con Anaconda en VSCode (`Ctrl+Shift+P` -> `Python: Select Interpreter`)

- Seleccionar el **Kernel** de Jupyter, en la parte superior derecha de la ventana de VSCode, al interprete de Python de Anaconda

- Seguir las instrucciones del **Setup**

- Ejecutar las celdas de código en orden, se puede con `Shift+Enter`
