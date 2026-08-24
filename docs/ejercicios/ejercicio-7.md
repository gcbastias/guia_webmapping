# Ejercicios — Unidad 7

Guía práctica paso a paso: instalación de MapStore 2025, gestión de usuarios y roles, creación y edición de mapas con servicios OGC, importación de datos locales, gestión de capas y estilos, servicios WFS y filtrado, creación de *widgets*, exportación y compartición de mapas, gestión de contextos con geoprocesamiento WPS, y creación de paneles de control (*dashboards*).

**1. Descarga e instalación de MapStore**
- En la página de inicio de la documentación de MapStore (`https://mapstore.readthedocs.io/en/latest/`) se accede al apartado **Downloads**. MapStore está disponible para Linux y Windows, con dos tipos de instalación: **desde un paquete binario** o **mediante un archivo WAR**.
- En el ejercicio se realiza una instalación mediante un **archivo bin comprimido**: en la página de *releases* de GitHub (`geosolutions-it/MapStore2`), dentro del apartado **Assets** de la versión estable (ej. **v2025.01.01**), se descarga el archivo `mapstore2-2025.01.01-bin.zip`.
- Se descomprime el archivo `.zip`, generando una carpeta **mapstore2** con las subcarpetas: `bin`, `conf`, `jre`, `lib`, `logs`, `temp`, `webapps`, `work`, y los archivos `mapstore2-shutdown.bat`/`.sh` y **`mapstore2-startup.bat`**/`.sh`.
- **MapStore utiliza un servidor Apache Tomcat**; el archivo `startup.bat` inicia el servidor. **Cada vez que se quiera trabajar con MapStore hay que abrir el servidor** ejecutando este archivo, lo que abre dos ventanas de símbolo de sistema con información del proceso.
- Una vez finalizada la operación, se escribe en el navegador: `http://localhost:8082/mapstore`, abriéndose la vista de inicio **"Bienvenido a MapStore"**.
- MapStore utiliza **Java**. Si se trabaja en el mismo equipo donde ya se instaló GeoServer, no es necesario ningún ajuste adicional. Si se trabaja en un equipo distinto o surgen problemas al iniciar, hay que comprobar que la variable de entorno **JAVA_HOME** apunta correctamente al JRE, desde `Panel de Control → Sistema → Configuración avanzada del sistema → Variables de entorno`.
- **Nota:** al iniciar sesión con MapStore, al abrir un mapa el navegador preguntará si se permite acceder a la ubicación; es conveniente **permitir el acceso**, ya que si no se hace, algunas opciones (como la identificación de elementos del mapa) no estarán activas.

**2. Gestión de usuarios MapStore**
- En la barra de menú de la página de inicio hay un icono para seleccionar el idioma y otro para el usuario. El icono **azul** hace referencia a un **usuario anónimo**.
- Al hacer clic sobre el icono de usuario se abre el menú de **iniciar sesión**. MapStore crea por defecto, al instalarse, un usuario con **rol de administrador**: usuario `admin`, clave `admin`. Tras el login se pasa a ser **usuario administrador** (icono verde) y se muestra una nueva página con más opciones, entre ellas el botón **Agregar recurso**, que permite: **Crear mapa**, **Crear panel**, **Crear geohistoria** y **Crear contexto**.

*Crear un nuevo usuario*
- Desde el menú del usuario (icono verde) se accede a **Administrador de cuentas de usuario**, que muestra la vista de usuarios existentes (por defecto: `admin`, `guest`, `user`).
- Se hace clic en **Nuevo** y se completan los datos: nombre de usuario (ej. `alumno`), clave y confirmación, y el rol (**USER** o **ADMIN**) — se crea un usuario normal (**USER**). Tras pulsar **Crear**, el nuevo usuario aparece en la vista de usuarios.

*Administrar grupos de usuarios*
- En el menú superior, pestaña **Grupos**, se muestran los grupos existentes (por defecto `testGroup`). Se pulsa **Nuevo grupo**, se escribe un **nombre** (ej. `Mappinggis`) y una descripción, y en la pestaña siguiente se **añaden miembros** al grupo (ej. el usuario `alumno`). Se finaliza con **Guardar**.
- De vuelta en "Administrar usuarios", el usuario `alumno` aparece asociado a los grupos `Mappinggis` y `everyone` (grupo al que pertenecen todos los usuarios por defecto), con iconos para editar o borrar el usuario.

*Trabajando con usuarios y roles*
- Los **roles** determinan qué permisos tiene cada usuario para realizar tareas sobre un mapa. Como **usuario administrador** se dispone de herramientas completas sobre cada mapa: abrir propiedades, añadir a favoritos, compartir y borrar.
- Si un usuario normal (ej. `alumno`) no pertenece al grupo autorizado a ver un mapa, **no lo verá** en su página de inicio. Para asignar permisos hay que usar la herramienta de edición (icono de "abrir propiedades") sobre el mapa: pestaña **Permisos** → botón de edición → **+Agregar permiso** → seleccionar el grupo (ej. `Mappinggis`) en la lista de **Grupos** → hacer clic en **Aplicar los cambios** (icono de guardado en verde).
- Al cerrar sesión de administrador y volver a iniciar sesión como el usuario `alumno`, ahora sí se muestran ambos mapas, aunque con opciones más limitadas: en el menú de tres puntos solo aparece **Compartir** (no **Eliminar**), y al abrir "propiedades" solo se ofrece la información del mapa, sin el menú de permisos.

**3. Interfaz de MapStore**
- Al acceder a un mapa se obtiene una vista con un mapa base de OpenStreetMap y los distintos menús de MapStore.
- En la parte superior: botones para **regresar a la página de inicio** y el icono del **menú de usuario**, junto con la opción de idioma y el botón **"Acerca de..."** (información sobre la versión de MapStore).
- **Barra de utilidades** de la vista de mapas:

| Icono | Función |
|---|---|
| Mostrar posición | Da la posición del usuario |
| Acercar / Alejar | Zoom + / Zoom − |
| Pantalla completa | Vista a pantalla completa |
| Ajustar a la máxima extensión | Encuadra todo el contenido del mapa |
| Modo 3D | Visualización con Cesium |
| Expandir/replegar (···) | Muestra nuevas opciones, entre ellas **Buscar objetos en el mapa** |

- El **menú de pie de página** contiene una escala gráfica y una escala numérica (permite elegir la escala), las coordenadas de la posición del ratón (visibles si el icono está en verde, ocultas si está en azul) y un botón para elegir el **sistema de coordenadas (CRS)**.
- **Menú lateral** (derecha) con las utilidades de MapStore:

| Icono | Función |
|---|---|
| Exportar | Exporta capas/anotaciones a JSON |
| Importar | Importa archivos KML, KMZ, GPX o GeoJSON |
| Catálogo (agregar capas al mapa) | Añade servicios OGC (WMS, WFS, CSW, WMTS) |
| Medir | Herramienta de medición |
| Ajustes | Configuración |
| Compartir | Comparte el mapa (enlace, redes sociales, embebido) |
| Documentación | Acceso a la documentación de MapStore |
| Tutorial | Tutorial guiado |
| Activar vistas del mapa | Activa geohistorias/vistas del mapa |

- **Barra de menú superior** de un mapa: **Guardar**, **Guardar como**, **Eliminar**, nombre del mapa, y **Abrir propiedades** (icono junto al nombre), que muestra las pestañas: Información, Permisos y Acerca de.
- En la esquina inferior izquierda del mapa hay una ventana con el **mapa de fondo** (por defecto OpenStreetMap); al hacer clic se despliega una lista para elegir otro mapa de fondo entre los disponibles.

**4. Creación y edición de mapas con MapStore**

*Acceso a datos de GeoServer mediante WMS*
- El botón **Agregar capas al mapa** (icono de carpeta) permite añadir **servicios OGC** como los que proporciona GeoServer, gracias a la perfecta integración de MapStore con GeoServer para trabajar con WMS, WFS, etc.
- En la ventana de **Catálogo**, se hace clic en el signo **+** para crear un nuevo servicio. En **Tipo** se selecciona **WMS**, se escribe un **Título** (ej. `geoserver`) y en **Url**: `http://localhost:8080/geoserver/wms`. Se hace clic en **Guardar**.
- **Nota importante:** para poder crear un nuevo catálogo, **GeoServer debe estar abierto**; en caso contrario se obtiene un error de conexión.
- Una vez creado el servicio, se accede a él mediante el botón **Buscar**, mostrando todas las capas de GeoServer. Se añaden al mapa con el botón **+** las capas **cities**, **countries** y **rivers**.
- Si al cargar una capa aparece el error *"Este servicio no soporta el sistema de coordenadas geográficas del mapa"*, se debe a que el mapa de MapStore no está en el mismo sistema de coordenadas que las capas de GeoServer. Se soluciona haciendo clic en el icono de **selección de proyección** (esquina inferior derecha) y eligiendo **EPSG:4326**.
- Hay que **guardar** los cambios con **Guardar como**, asignar un nombre (ej. `MappingGIS`) y hacer clic en **Crear**.
- Desde el **menú de capas** (esquina superior izquierda) se puede fijar el **orden** de las capas (arrastrando con el marcador con forma de mano que aparece junto al nombre de la capa) y su **transparencia/opacidad** (deslizador). Haciendo clic en el icono **>** situado a la derecha del nombre de la capa se muestra su **leyenda**.

*Creación de Anotaciones*
- MapStore permite dibujar elementos sobre el mapa de forma rápida y sencilla. Las **geometrías** disponibles son: marcadores, líneas, polígonos, textos o círculos. Es una herramienta interesante porque los elementos creados pueden ser **exportados**, permitiendo compartir esas geometrías.
- Desde el **botón de capas** (esquina superior izquierda) se accede al botón **Anotaciones**. Se abre el menú para crear una nueva anotación, con pestañas: **Propiedades** (Título y Descripción), **Geometrías** y **Ajustes**.
- En la pestaña **Geometrías** se selecciona el icono del **marcador** y se navega por el mapa hasta elegir el lugar donde dibujarlo; al hacer clic sobre el punto, sus coordenadas se transmiten al formulario. Desde el menú **Estilo** se pueden definir los estilos de la geometría (marcador, glifo, imagen, opacidad, tamaño, rotación, punto de anclaje).
- También se pueden dibujar otras geometrías, como un **polígono**, directamente sobre el mapa.
- Cuando se termina de dibujar, hay que **guardar el mapa** (aparece la ventana "Crear una copia del recurso actual", donde se asigna un nombre, ej. `Anotación Plaza Mayor`, y se pulsa **Crear**).

*Importar capas locales*
- MapStore permite añadir datos geográficos de un archivo al mapa. Los **formatos admitidos** son: **KML, KMZ, GPX o GeoJSON** (los shapefiles deben estar comprimidos).
- En el menú se elige **Importar**, abriéndose la ventana de importación de archivos ("Suelta contextos de mapas o archivos vectoriales aquí" / "Selecciona archivos…").
- Se importa un archivo GeoJSON de ejemplo llamado **SalamancaMonumental.geojson**. MapStore muestra una ventana ("Añadir fichero en local") donde se puede elegir el **estilo** de la nueva capa: en forma de **marcador** (`Marker`, con opciones de `Stroke` y `Fill`) o en forma de **círculo** (eligiendo color y grosor del contorno —`Stroke`— y color de relleno y tamaño —`Fill`—), además de la opción **Zoom sobre el fichero shape**. Se hace clic en **Terminar** y se **guarda** el mapa.
- Al habilitar la capa en el menú de gestión de capas, se puede seleccionar cualquiera de los nuevos marcadores para que se abra un control a la derecha con sus datos (los que trae el archivo GeoJSON importado). Si se hace clic sobre el botón **de información**, se muestra también la dirección del punto seleccionado, obtenida de la base de datos **Nominatim** de OpenStreetMap.

*Gestión de capas*
- La **tabla de contenidos** ofrece las herramientas para gestionar las capas en MapStore (botón de capas en la esquina superior izquierda). Al seleccionar una capa (ej. `cities`) se muestra un nuevo menú con sus opciones:

| Icono / opción | Función |
|---|---|
| Zoom | A la extensión de la capa seleccionada |
| Configuración (llave inglesa) | Configuración de la capa seleccionada |
| Filtrar capas | Aplica un filtro sobre la capa |
| Abrir tabla de atributos | Muestra los datos alfanuméricos de la capa |
| Eliminar | Elimina la capa seleccionada |
| Crear *widget* | Crea un *widget* para la capa seleccionada |
| Exportar datos | Exporta los datos de la capa |

- Además, situándose sobre una capa del gestor de capas y haciendo **clic con el botón derecho del ratón**, se abre un menú con opciones adicionales: **Zoom a la extensión de la capa seleccionada**, **Eliminar la capa seleccionada**, **Golpe fuerte** y **Vidrio espía**.
  - **Vidrio espía**: herramienta con forma de círculo que, al mover el cursor sobre el mapa, va mostrando y ocultando los elementos de la capa dentro de esa área circular.
  - **Golpe fuerte**: crea una línea sobre el mapa de tal manera que a un lado oculta los elementos de la capa y al otro los muestra.
  - Ambas herramientas se pueden ajustar mediante la opción **Configurar** (radio de la lupa o dirección de la línea de "Golpe fuerte": vertical/horizontal).

*Gestión de estilos*
- MapStore permite utilizar los **estilos definidos en GeoServer**. Para ello, en GeoServer se entra en `Capas` → se selecciona la capa (ej. `earth:cities`) → pestaña **Publicación** → en la sección de estilos se selecciona en la ventana izquierda el estilo adicional deseado (ej. `earth:cities_labels`) y se traslada al panel derecho (**Estilos seleccionados**) con la flecha, guardando los cambios.
- De vuelta en MapStore, se reinicia el mapa, se selecciona la capa `cities` en la tabla de contenidos y se hace clic en la herramienta de **estilo** (icono de llave inglesa/cuentagotas), que muestra los estilos disponibles para la capa (ej. `cities_filter`, `cities_labels`). Al elegir uno, el mapa se actualiza mostrando la capa con el estilo seleccionado.

*Servicios WFS en MapStore*
- Además de WMS, MapStore permite utilizar otros servicios como **WFS**, **CSW** o **WMTS**.
- Para crear un nuevo mapa con un servicio WFS: en el catálogo se crea una nueva conexión (signo **+**), se elige **Tipo: WFS**, se escribe un título y en **Url**: `http://localhost:8080/geoserver/wfs`. En **Ajustes avanzados** se marca la opción **"Buscar en la selección de servicios"** y se hace clic en **Guardar**.
- Se busca y añade al mapa la capa **cities**. Se **guarda** el mapa (ej. como `Mapas WFS`).
- Desde la **tabla de contenidos**, seleccionando la capa `cities` y accediendo a la herramienta de **estilo**, se puede definir un nuevo estilo para los círculos de las ciudades (color de relleno, color de línea, ancho de línea, radio, rotación…), disponiendo de un **Editor de código** para un control más avanzado del estilo.

*Filtrando los datos*
- Una de las capacidades más interesantes de MapStore es su capacidad para manejar los datos y realizar operaciones sobre ellos obtenidos vía WFS, empezando por el **filtrado de datos**.
- Seleccionando la capa `cities` y haciendo clic en el icono de **filtrar capas**, se puede crear un **filtro por atributo** haciendo clic en el signo **+**: se elige el **atributo** (ej. `pop_max`), el **operador** (ej. `>`, mayor que) y el **valor** (ej. `10.000.000`), filtrando así las ciudades con población superior a ese valor.
- Además del filtro por atributo, se puede filtrar por **región de interés**, seleccionando un área definida por un **rectángulo, círculo o polígono**, junto con el tipo de **operación geométrica**: **intersecta**, **está contenido** o **contiene**.
- Tras dibujar la geometría del filtro (ej. un círculo, ajustando su radio con el botón de **editar**), siempre hay que hacer clic en **Validar** para aplicar el filtro.
- Con el filtro activo, los datos y los *widgets* que genere MapStore tienen como campo de acción solo los **datos filtrados**; por ejemplo, la tabla de atributos solo mostrará las entidades que cumplen el filtro. Para eliminar un filtro se usa el botón de **borrar filtro**.

*Configurar un servicio de búsqueda*
- La barra de menú contiene un control para realizar búsquedas de ubicación mediante la base de datos **Nominatim** de OpenStreetMap. Además, permite **configurar esta búsqueda para una capa WFS** propia, de forma que los resultados se ofrezcan como alternativa adicional a los de OpenStreetMap.
- En la ventana de búsquedas de ubicación se hace clic en el icono de la herramienta (engranaje) y se selecciona **"configurar los servicios de Búsqueda"**, abriéndose la ventana "Crear/modificar un servicio de búsqueda". Se hace clic en **Añadir** y se completan los campos:
  - **Nombre** del buscador (ej. `Ciudades`).
  - **Url del servicio**: la URL del servicio WFS (ej. `http://localhost:8080/geoserver/wfs`).
  - **Capa**: la capa de GeoServer sobre la que se busca (ej. `earth:cities`).
  - **Atributos**: el atributo de la capa sobre el que se realiza la búsqueda (ej. `name`).
- En el paso siguiente ("Resultados de la visualización de las propiedades"): **Título** (ej. `properties.name`, la propiedad que contiene el nombre a buscar), **Descripción** (texto libre para identificar el tipo de búsqueda) y **Prioridad** (orden en que se muestran los resultados; a menor número, mayor prioridad; OpenStreetMap tiene prioridad 5 por defecto).
- En el último paso ("Propiedades opcionales"): **Ordenado por** (atributo por el que se ordenan los resultados), **Máximo de características** (número de resultados que muestra la búsqueda) y **Nivel máximo de zoom** (el que se establecerá al abrir el mapa desde un resultado de búsqueda personalizado). Se finaliza con **Guardar/actualizar**.
- A partir de ese momento, al escribir en el control de búsqueda el nombre de una ciudad, se autocompletará el texto ofreciendo el resultado de la búsqueda personalizada junto con los de Nominatim.

**5. Creación de *widget***
Esta herramienta permite obtener **gráficos** y añadir **textos** a partir de los datos de una capa.
- Sobre el **mapa WFS de las ciudades** se crea un filtro (**Filtro por atributo**): atributo `sov0name`, operador **igual**, valor `United States`, dejando visibles solo las ciudades de Estados Unidos. No hay que olvidar **validar y guardar** el filtro.
- Desde el menú de la tabla de contenidos, seleccionando la capa filtrada, se accede a la opción ***widget***, que ofrece cuatro tipos:

| Tipo de *widget* | Descripción |
|---|---|
| **Gráfico** | Agregar un gráfico (barras, líneas o circular) |
| **Texto** | Agregar un área de texto |
| **Tabla** | Agregar una tabla |
| **Contador** | Agregar un contador |

- **Widget Gráfico**: se elige **Gráfico de barras**. En **Atributo X** se elige `name`, en **Atributo Y** se elige `pop_max`, y en **Operación** se elige **SUM**. Se puede personalizar el gráfico (colores de relleno y contorno) desde la sección **Estilo de trace**. Con el botón de flecha se accede a la ventana de configuración de información del *widget*, donde se escribe un **título** (ej. `Población`) y una **descripción** (ej. `Población de Ciudades USA`), y se **agrega** al mapa. Los datos que muestran los *widgets* hacen referencia al **área del mapa visible**: si se hace zoom o se mueve el mapa, los datos del gráfico se sincronizan con el mapa.
- **Widget Contador**: sobre la capa `cities` se elige el tipo **Contador**, configurando los datos: **Utilizar** = `name`, **Operación** = **COUNT**. También se pueden definir prefijo, formato, sufijo, fórmula, color y familia de fuentes. Tras configurar el título y descripción, se **agrega el *widget*** al mapa, insertándose un botón para controlar la visibilidad de los distintos *widgets* creados.

**6. Modo escritorio, móvil y 3D**
MapStore utiliza OpenLayers, Leaflet y Cesium para la visualización de mapas, concretamente:

| Modo | Librería |
|---|---|
| Escritorio | OpenLayers |
| Móvil | Leaflet |
| 3D | Cesium |

- Por defecto, MapStore utiliza **OpenLayers** en modo escritorio y **Leaflet** cuando se trata de un dispositivo móvil.
- Para acceder al **modo 3D** se utiliza un botón específico (**3D**) situado en la barra lateral, que abre la vista con **Cesium**: se puede hacer zoom y girar la esfera terrestre con el ratón, además de girar la vista y modificar el norte actuando sobre el control de navegación (brújula). Para volver a la vista de escritorio 2D, se vuelve a hacer clic sobre **3D**.

**7. Exportar, guardar y compartir nuestros mapas**
- Todos los cambios realizados en un mapa o vista de MapStore deben **guardarse** (**Guardar** / **Guardar como**) para que no se pierdan. Estas opciones estarán disponibles en función de los **roles** del usuario con el que se trabaje.
- También se puede acceder desde la página de inicio a cada mapa para **editar las propiedades** (icono de "abrir propiedades"), donde se puede además **añadir una imagen** que identifique al mapa, seleccionándola y haciendo clic en **Aplicar**.

*Exportar un mapa*
- MapStore permite **exportar las capas y las anotaciones de un mapa a formato JSON**, formato de texto que adopta la estructura de un objeto JavaScript (alternativa a XML, con una adaptación a datos geográficos que es GeoJSON). Los archivos generados durante la exportación se pueden utilizar en las librerías **OpenLayers y Leaflet**.
- Para exportar una **anotación**: en el menú de anotaciones se selecciona la correspondiente (ej. el polígono "Plaza Mayor") y se hace clic en el botón de **descargas**, descargando un archivo JSON (ej. `Anotación Plaza Mayor.json`).
- Se abre el archivo con un editor de texto y se añade al inicio `var geojson = `. Se guarda con extensión `.js` (ej. `poligono.js`).
- Con este archivo se puede crear un mapa usando **Leaflet**: se incorpora el archivo `poligono.js` a la cabecera del documento HTML junto con la librería Leaflet (CSS y JS), y se escribe el código para dibujar la capa a partir de la exportación:

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>MapStore Leaflet</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<style>
    #map { width: 700px; height: 600px; }
</style>
</head>
<body>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="poligono.js"></script>

<div id="map"> </div>

<script>
    var map = L.map('map', {center: [40.965, -5.664], zoom: 15});
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

    function style(feature) {
        return {
            fillColor: 'red',
            weight: 2,
            opacity: 1,
            color: 'white',
            dashArray: '3',
            fillOpacity: 0.7
        };
    }

    function popup(feature, layer) {
        layer.bindPopup(geojson.features[0].properties.annotationLayerTitle);
    }

    geojson = L.geoJson(geojson, {
        style: style,
        onEachFeature: popup
    }).addTo(map);
</script>
</body>
</html>
```
- En el código anterior se define una función **`style`** para el estilo de la capa y una función **`popup`** para mostrar el título de la anotación. Se utiliza la clase de Leaflet **`L.geoJson`**, que permite usar el archivo GeoJSON exportado: como primer parámetro recibe la variable `geojson` (nombre asignado al crear `poligono.js`), y a continuación las opciones `style` y `onEachFeature`. El resultado es un mapa Leaflet que contiene la anotación exportada desde MapStore.

*Compartir mapas*
- Se accede a las opciones de compartir mapa desde el **Burger menú** (botón **Compartir**) o directamente desde la vista de mapas con el botón de compartir. MapStore permite compartir un mapa de **tres formas**:
  1. Mediante un **enlace directo** (con posibilidad de generar un **código QR**).
  2. Mediante **redes sociales** (Facebook, X, LinkedIn).
  3. Mediante **código embebido** (etiqueta `<iframe>`).
- **Nota**: al trabajar con un servidor local (`localhost`), el mapa no estará visible para usuarios fuera del propio sitio, salvo que se convierta el equipo en un servidor público (operación posible pero compleja y poco recomendable).
- **Nota importante**: solo se pueden compartir mapas que estén **autorizados previamente**. Si se intenta compartir un mapa sin permisos, se obtiene el aviso *"Mapa no accesible"*. En ese caso hay que ir a **"Editar propiedades"** → pestaña **Permisos** → **+Agregar permiso** → elegir el grupo **"everyone"** con permiso **"puede ver"** → **Guardar**, y entonces ya se puede compartir el mapa.
- Ejemplo de código **embebido** (copiando la etiqueta `<iframe>` que ofrece MapStore e insertándola en un documento HTML, modificando los atributos `height` y `width` para ajustar el área del mapa):
```html
<!DOCTYPE html>
<html>
<body>
<h2>HTML Iframes</h2>
<p>Mapa de MapStore</p>
<iframe style="border: none;" height="500" width="700"
src="http://localhost:8082/mapstore/embedded.html?forceDrawer=true#/78"></iframe>
</body>
</html>
```
- De esta forma no solo se comparte el mapa embebido, también se incorporan el **menú de capas**, el **menú lateral** y el **control de búsqueda de direcciones** de MapStore.

**8. Administrar contextos. Añadir extensiones**
El **Administrador de contexto** de MapStore es una herramienta administrativa diseñada para crear y configurar los visores de MapStore, permitiendo crear un **entorno personalizado** con las herramientas y extensiones que se deseen, más allá de las de la vista por defecto.
- Se crea un nuevo contexto desde **Agregar recurso → Crear contexto**. Se puede omitir el tutorial guiado que ofrece MapStore.
- La creación de un contexto tiene **4 pasos**:
  1. **Configuración general**: se asigna un **nombre** al contexto (ej. `nuevo_contexto`) y un **título de la ventana** (ej. `Contexto curso mappinggis`). MapStore permite también **importar y exportar** un contexto.
  2. **Configurar mapa**: se define una vista del mapa y/o se incorporan capas, mediante las herramientas de **catálogo, importar y exportar** disponibles en el menú de este paso. Se puede modificar el **mapa base**, seleccionando por ejemplo `Sentinel 2 Cloudless`.
  3. **Configurar complementos**: en dos ventanas (complementos disponibles / complementos habilitados) se seleccionan los **complementos (plugins)** a incluir en el contexto, pasándolos con los botones `>`, `>>`, `<`, `<<`. Ejemplos de complementos disponibles: 3D, About, Ajustes, Anotaciones, Barra de búsqueda, SearchByBookmark, Burger Menu, Catálogo, Exportación de mapas, **Geoprocesamiento**, Home, Importar, Map, Medida, Salvar, Zoom In, entre otros. Para el ejercicio se incluyen los complementos de **Geoprocesamiento** y **Catálogo**.
  4. **Tema**: se pueden asignar estilos a la vista del contexto, eligiendo entre varios temas predefinidos (ej. tema **Dark**), configurando colores de texto y de fondo principal/secundario.
- Al finalizar los 4 pasos se hace clic en **Guardar**, y el nuevo contexto aparece en el administrador de contextos, desde donde se puede **modificar** con el icono de edición.

*Complemento de Geoprocesamiento*
- La herramienta de **Geoprocesamiento** utiliza los procesos **WPS** para realizar operaciones de **buffer** e **intersección** sobre las geometrías del mapa. Esta herramienta no está disponible en la vista inicial de MapStore, por lo que debe utilizarse desde un contexto que la incluya (como el creado anteriormente).
- Al abrir el contexto se dispone de las herramientas de **Catálogo** y **Geoprocesamiento** en el menú lateral. Se utiliza el catálogo para definir la conexión al servicio WMS de GeoServer (`http://localhost:8080/geoserver/wms`) y se añade la capa con los **ríos** (`rivers`) al mapa.
- Para crear un **buffer** en torno a un río, se abre la herramienta de Geoprocesamiento (icono correspondiente) y se completa el formulario:
  1. **Proceso** a realizar: **Buffer** o intersección.
  2. **Capa de origen**: `rivers`.
  3. **Característica de origen**: la entidad concreta sobre la que se hace el buffer (se elige del control de selección, ej. `rivers.1`).
  4. **Distancia**: valor en **metros** o **kilómetros** (ej. 5 km).
  5. **Ajustes avanzados**: forma de los extremos del buffer — **Redonda**, **plana** o **cuadrada** — y segmentos de cuadrante.
- Por último, se pulsa **Ejecutar** y se obtiene el resultado de la operación representado sobre el mapa.

**9. Creación de paneles de control (*dashboards*)**
Un **panel de control** en MapStore es una presentación en la que se combinan diferentes elementos como **vistas del mapa, textos, leyendas y *widgets*** para crear un documento personalizado.
- Se crea desde la página de inicio con el botón **"Crear panel"** (Agregar recurso → Crear panel), abriéndose una nueva ventana con el panel de control vacío ("El panel de control está vacío").

*Añadir widgets: mapa, leyenda y texto*
- Se hace clic sobre el botón **+** situado en la esquina superior izquierda de la ventana. Para empezar, es necesario incorporar un **mapa**, eligiendo la opción **"agregar un mapa"**.
- Se muestra un selector con los diferentes mapas creados en MapStore (ej. `MappingGIS`, con los servicios WMS de GeoServer). Se hace clic sobre **"Usar este mapa"**, lo que permite configurar la vista del mapa (ocultando/mostrando capas o modificando su opacidad) mediante una **vista previa**. Se escribe un **título** y una **descripción**, y se **agrega** el recurso al panel.
- Para agregar un nuevo elemento se vuelve a pulsar sobre el signo **+**. Ahora aparece una nueva opción que antes estaba oculta: la **leyenda** (esta opción solo se muestra una vez que ya existe un mapa en el panel de control). Se ofrece una **vista previa** de la leyenda con las capas del mapa y sus símbolos, se escribe un título y descripción, y se **agrega el recurso**.
- De la misma forma se puede añadir un **texto**. Los elementos creados pueden **distribuirse por el panel**, adaptando su forma y tamaño según se desee (arrastrando y redimensionando cada bloque).
- Finalmente, hay que **guardar el panel de control** antes de salir.
