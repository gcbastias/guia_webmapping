# Unidad 5. Personalización de aplicaciones web de mapas

### Resumen estructurado

**1. Contenido de la unidad**
- Aplicaciones web.
- Lenguajes de programación para la web: HTML, CSS y JavaScript.

**2. ¿Qué es una aplicación web?**
Una **aplicación Web** es una aplicación ejecutable en un navegador. Se construye combinando tres lenguajes con roles complementarios:

| Lenguaje | Rol |
|---|---|
| **HTML** | Lenguaje de marcado de páginas web; define la **estructura** del contenido de una página web. |
| **CSS** (*Cascading Style Sheets*) | Define los **estilos** (apariencia) de una página web. |
| **JavaScript** | Lenguaje de **programación** web para crear aplicaciones que se ejecutan en el navegador y le dan **funcionalidad**. |

*Ejemplo de aplicación webmapping mínima* (estructura HTML con cabecera CSS y JavaScript):
```html
<!DOCTYPE html>
<html>
    <meta charset="utf-8" />
    <head>
        <script src="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js"></script>
        <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css" />
        <style>
            #map {
                width: 100%;
                height: 600px;
            }
        </style>
    </head>
    <body>
        <div id="map"></div>
        <script>
            var OSM = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a>'
                +'contributors',
                maxZoom: 18
            });

            var map = L.map('map', {
                center: [41.66, -4.72],
                zoom: 13,
                layers: OSM
            });
        </script>
    </body>
</html>
```
- **HTML** define la estructura (`<html>`, `<head>`, `<body>`, `<div id="map">`).
- **CSS** define el estilo (`<style>` con las dimensiones del `<div>` del mapa).
- **JavaScript** aporta la funcionalidad (creación de la capa base y del objeto mapa con Leaflet).

**3. HTML5**
- **HTML** (*HyperText Markup Language*, lenguaje de marcado de hipertexto) tiene su propia **sintaxis** (reglas para la comunicación).
- Un **navegador web** transforma el texto escrito en HTML en una página web reconocible, siguiendo la sintaxis HTML.
- Un **lenguaje de marcado** es un lenguaje de programación usado para que el texto haga más que solamente aparecer en una página; puede convertir el texto en imágenes, enlaces, tablas, listas, etc.

**4. CSS**
- **CSS** (*Cascading StyleSheets*, Hojas de Estilo en Cascada): lenguaje usado para describir la apariencia y el formato de un HTML.
- Una **hoja de estilo** es un archivo que describe cómo debería verse un archivo HTML.
- CSS es un lenguaje muy utilizado por los diseñadores web y en los últimos años se ha incorporado al mundo GIS. La edición de estilos en MapBox Studio Classic o en CartoDB se realiza utilizando **CartoCSS**.

**5. JavaScript**
- **JavaScript**: lenguaje para programar aplicaciones para internet y la web.
- La última versión estable es **ECMAScript 2016 (ES6)**, aunque ya existen ES7, ES8...
- *¿Para qué podemos usar JavaScript?*
  - Crear sitios web que respondan a las interacciones del usuario.
  - Crear aplicaciones webmapping (por ejemplo, con OpenLayers).
  - Acceder a información en internet (ej. encontrar las palabras más populares en Twitter según el tema).
  - Organizar y presentar datos (ej. automatizar el trabajo de las hojas de cálculo, o la visualización de datos).

**6. Librerías JavaScript para mapas**
La utilización de librerías JavaScript para crear mapas proporciona una serie de **ventajas** frente a las soluciones empaquetadas (como CartoDB o MapBox):
- Más personalización.
- Más control sobre las capas.
- Posibilidad de incluir nuevas herramientas y botones.

- El estándar de la industria para las librerías de JavaScript ha sido la **API de Google Maps**.
- Las bibliotecas JavaScript abiertas (**OpenLayers** o **Leaflet**) no están sujetas a los cambios de los planes de pago de soluciones comerciales.

**Arquitectura típica (posición de las librerías JS en la arquitectura general):**
- Interfaz de usuario: **Leaflet** / OpenLayers
- Servidor web: GeoServer ↔ GeoWebCache
- Base de datos: PostGIS

---

## Unidad 5-1. Leaflet

### Resumen estructurado

**1. Contenido de la unidad**
- ¿Qué es Leaflet?
- El mapa
- Capas
- Controles
- Eventos
- Plugins

**2. ¿Qué es Leaflet?**
- **Leaflet** es una librería JavaScript *open source* para crear mapas interactivos en un entorno móvil.
- Es la elección utilizada por Flickr, Wikimedia, foursquare, OSM, CARTO, GIS Cloud, Washington Post, Wall Street Journal, Geocaching.com, etc.

*Historia de Leaflet:*

| Año | Hito |
|---|---|
| **2011** | Surge a principios de año. Creado por **Vladimir Agafonkin**, ingeniero de Mapbox, con un equipo de +8000 colaboradores especializados. |
| **2012** | OpenStreetMap adopta Leaflet. |
| **2013** | Aparecen plugins clave como: leaflet.draw, leaflet.markercluster, leaflet.fullscreen… |
| **2017–2020** | Integración con frameworks: React, Vue, Angular. Uso en apps web de QGIS (como qgis2web). |
| **2024–2025** | La comunidad mantiene vivo el proyecto. Plugins modernos, integraciones con Svelte, React y compatibilidad con OGC APIs. |

*Leaflet = Sencillez:*
- Muy ligero (39 KB).
- Sencillo y rápido de aprender.
- API bien documentada y fácil de usar.
- Características básicas pero que funcionan a la perfección.
- Soporte móvil.
- Funciona tanto en los navegadores modernos como en los antiguos.
- Ampliable con plugins para extender su funcionalidad.

*Documentación:*
- Documentación de la API: http://leafletjs.com/reference.html
- Ejemplos y tutoriales: http://leafletjs.com/examples.html
- Código: https://github.com/Leaflet/Leaflet
- Leaflet Tips and Tricks: https://leanpub.com/leaflet-tips-and-tricks/read

**3. Comenzando con Leaflet. Carga de la librería**
El encabezado del documento carga necesariamente los archivos JavaScript y CSS que serán incluidos con el mapa: la librería JavaScript **leaflet.js** y la hoja de estilo **leaflet.css**. Leaflet se puede utilizar descargando la librería (https://leafletjs.com/download.html) o mediante un enlace **CDN**:

```html
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
```

**4. El mapa — L.map()**
`L.map` → crear y manipular el mapa. Tiene activadas por defecto las interacciones del ratón sobre el mapa y el control de zoom y atribución.

*Sintaxis:*
```
L.map( <HTMLElement|String> id, <Map options> opciones )
```
`L.map` crea una instancia de un objeto mapa definido por un elemento `<div>`:
```javascript
var map = new L.map('map', {
    center: ...
    zoom: ..
    layers :...
});
```
Primero se crea un `<div>` que albergará el mapa, y se le da estilo (dimensiones):
```html
<div id="map"></div>
<style>
    #map { width: 700px; height: 600px; }
</style>
```

*Mi primer mapa* — un mapa básico = `L.map` + `L.tileLayer`:
```javascript
var map = L.map('map', {
    center: [40.965, -5.664],
    zoom: 16
});
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
```

*Opciones de la clase L.map():*

| Tipo | Opción | Descripción |
|---|---|---|
| Principales | `center` | Centro geográfico inicial del mapa (coordenadas geográficas). |
| Principales | `zoom` | Zoom inicial del mapa. |
| Principales | `layers` | Capas que se añadirán al mapa inicialmente. |
| Secundarias | `minZoom` / `maxZoom` | Mínimo / máximo nivel de zoom. |
| Secundarias | `maxBounds` | Restringe la vista a las coordenadas geográficas establecidas, devolviendo al usuario a ellas si intenta desplazarse fuera. |
| Secundarias | `crs` | Sistema de referencia de coordenadas. Por defecto EPSG:3857 (proyección basada en WGS84). |

*Métodos para modificar el estado del mapa:*
- **`setView(<LatLng> center, <Number> zoom?, <zoom/pan options> options?)`**: define la vista del mapa (centro geográfico y zoom). Ejemplo: `var map = L.map('map').setView([-41.2858, 174.78682], 14);`
- Otros métodos: `setZoom()`, `zoomIn()`, `zoomOut()`, `setZoomAround()`, `fitBounds()`, `fitWorld()`, `panTo()`, `panInsideBounds()`, `panBy()`, `invalidateSize()`, `setMaxBounds()`, `locate()`, `stopLocate()`, `remove()`, `flyTo()`.

*Métodos para recuperar el estado del mapa (métodos Get):*
- **`getCenter()`**: retorna las coordenadas del centro geográfico de la vista del mapa. Ejemplo: `var center = map.getCenter(); document.write(center);` → `LatLng(41.66, -4.72)`.
- `getZoom()` → nivel de zoom de la vista actual.
- `getMinZoom()` / `getMaxZoom()` → mínimo / máximo nivel de zoom del mapa.
- `getBounds()` → retorna `LatLngBound` de la vista actual (coordenadas de las esquinas suroeste y noreste).
- Otros métodos: `getBoundsZoom()`, `getSize()`, `getPixelBounds()`, `getPixelOrigin()`.

*Métodos para trabajar con capas y controles:*
- **`addLayer(<ILayer> layer, <Boolean> insertAtTheBottom?)`** ↔ **`removeLayer()`**: añadir / eliminar una capa del mapa. Ejemplo:
```javascript
var ggl = L.gridLayer.googleMutant({ type: 'roadmap' });
map.addLayer(ggl);
```
- Otros métodos: `hasLayer`, `eachLayer`, `openPopup`, `closePopup`, `addControl`, `removeControl`.

**5. Las capas — ILayer**
Leaflet organiza las capas en **4 grupos**:

| Capas raster | Capas vectoriales | Capas de interfaz de usuario | Otras capas |
|---|---|---|---|
| TileLayer | Path | Markers | LayerGroup |
| TileLayer.WMS | Polyline | Popups | FeatureGroup |
| VideoOverlay | Polygon | Tooltip | GeoJSON |
| ImageOverlay | Rectangle, Circle, CircleMarker, SVGOverlay, SVG, Canvas | | GridLayer |

*5.1 Capas raster*

Leaflet tiene 4 clases para capas raster: capas teseladas (`tileLayer`), capas teseladas WMS (`tileLayer.WMS`), capas de imágenes (`imageOverlay`) y capas de vídeo (`VideoOverlay`).

**Capas teseladas — L.tileLayer**: carga y visualiza capas teseladas en el mapa.
```
L.tileLayer( <String> urlTemplate, <TileLayer options> opciones? )
```
La `urlTemplate` es una cadena con el formato `http://{s}.mapdomain.org/{z}/{x}/{y}.png`, donde `{s}` permite usar uno de los subdominios (para peticiones paralelas más rápidas), `{z}` declara el nivel de zoom, y `{x}`/`{y}` definen las coordenadas de las teselas. Ejemplo: `L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);`

*Opciones*: `minZoom`, `maxZoom`, `tileSize`, `attribution`, `detectRetina`, `opacity`, `bounds`... La **atribución** es la colocación de una referencia adecuada a la fuente de los datos, para asegurar que se reconocen los créditos y derechos de autor del proveedor de teselas. Ejemplo:
```javascript
var OpenStreetMap_Mapnik = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});
```
*Métodos*: `addTo`, `bringToFront`, `bringToBack`, `setOpacity`, `setZIndex`, `redraw`, `setUrl`, `getContainer`.

**Capas teseladas WMS — L.tileLayer.WMS**: se utiliza para visualizar servicios WMS como capa de teselas en el mapa. Extiende la clase `L.TileLayer`.
```
L.tileLayer.wms( <String> baseUrl, <TileLayer.WMS options> opciones )
```
Incluye todas las opciones de `L.TileLayer` y además: `layers` (requerido, lista de capas WMS separadas por comas), `styles` (lista de estilos WMS), `format` (formato de las imágenes; usar `image/png` para transparencia), `transparent` (por defecto `false`), `version` (por defecto 1.1.1), `crs` (por defecto el CRS del mapa). Ejemplo:
```javascript
var cities = L.tileLayer.wms("http://localhost:8080/geoserver/wms", {
    layers: 'cities', // obligatorio
    format: 'image/png',
    transparent: true,
    attribution: "Natural Earth",
    styles: "cities_label"
});
```

**Capas de imágenes — L.imageOverlay**: añade una imagen georreferenciada al mapa (requisito: georreferenciar la imagen indicando las coordenadas de las esquinas).
```
L.ImageOverlay( <String> imageUrl, <LatLngBounds> bounds, <ImageOverlay options> opciones? )
```
*Opciones*: `opacity`, `attribution`... *Métodos*: `addTo`, `bringToFront`, `bringToBack`, `setOpacity`, `setUrl`. Ejemplo:
```javascript
var imageUrl = 'http://www.lib.utexas.edu/maps/historical/newark_nj_1922.jpg',
    imageBounds = [[40.712216, -74.22655], [40.773941, -74.12544]];
L.imageOverlay(imageUrl, imageBounds).addTo(map);
```

*5.2 Capas de interfaz de usuario*

Comprenden marcadores (`Markers`), ventanas emergentes (`Popups`) y etiquetas (`Tooltip`).

**Marcadores — L.marker**: muestra un marcador/icono sobre el mapa.
```
L.marker( <LatLng> latlng, <Marker options> opciones? )
```
Ejemplo: `L.marker([41.66, -4.71]).addTo(map)`

*Opciones*: `icon` (`L.Icon`, para seleccionar el icono), `clickable` (por defecto `true`), `draggable` (por defecto `false`; si es `true`, el marcador se puede arrastrar), `keyboard` (por defecto `true`, controlable con el tabulador del teclado), `title` (texto tipo tooltip al pasar el ratón, sin valor por defecto), `alt` (texto del atributo `alt` de la imagen del icono, útil para accesibilidad), `zIndexOffset`, `opacity`, `riseOnHover` (el marcador se pone encima de los demás al pasar el ratón), `riseOffset`.

*Métodos*: `addTo`, `getLatLng`, `setLatLng`, `setIcon`, `setZIndexOffset`, `setOpacity`, `bindPopup`, `unbindPopup`, `openPopup`, `getPopup`, `closePopup`, `togglePopup`, `setPopupContent`, `toGeoJSON`. `bindPopup` lanza una ventana emergente con contenido HTML al hacer clic sobre el marcador; `openPopup()` la abre directamente. Ejemplo:
```javascript
L.marker([41.65246, -4.6982], {icon: myIcon})
    .addTo(map)
    .bindPopup("Localización de <b>MappingGIS.com</b>");
```
*Icono personalizado — L.Icon*: un icono marcador se define con un objeto `L.Icon`, pasado como opción al crear el marcador:
```javascript
var myIcon = L.icon({
    iconUrl: 'https://openlayers.org/assets/theme/img/logo70.png',
    iconSize: [30, 30],
    popupAnchor: [-1, -10]
});
```

**Ventanas emergentes — L.popup**: abre ventanas emergentes en ciertos lugares del mapa.
```
L.popup( <Popup options> options?, <ILayer> source? )
```
Ejemplo (forma más compleja que `bindPopup`, útil para popups no asociados a una capa):
```javascript
var popup = L.popup()
    .setLatLng([41.65, -4.70])
    .setContent('<p>Hola!<br/>Soy un bonito popup.</p>')
    .openOn(map);
```

**Etiquetas — L.tooltip**: se usa para visualizar pequeños textos sobre capas.
```
L.tooltip( <Tooltip options> options?, <Layer> source? )
```
Ejemplo:
```javascript
var marker = L.marker([41.66, -4.71]).addTo(map);
marker.bindTooltip("León - España", {permanent: true}).openTooltip();
```
*Opciones*: `pane` (panel HTML donde se agrega la etiqueta), `offset` (desplazamiento, por defecto `Point(0,0)`), `direction` (`right`, `left`, `top`, `bottom`, `center`, `auto`; por defecto `auto`), `permanent` (abierta de forma permanente o solo al pasar el ratón; por defecto `false`), `sticky` (si es `true`, la etiqueta sigue al ratón en vez de estar fija en el centro del objeto; por defecto `false`), `interactive` (por defecto `false`), `opacity` (por defecto `0.9`).

*5.3 Capas vectoriales*

**Path**: clase abstracta que contiene opciones y constantes compartidas por las capas vectoriales `Polygon`, `Polyline` y `Circle`. No se usa directamente.
- *Opciones*: `stroke`, `color`, `weight`, `opacity`, `fill`, `fillcolor`, `fillOpacity`, `dashArray`, `lineCap`, `lineJoin`, `clickable`, `pointerEvents`, `classname`.
- *Eventos*: `click`, `dblclick`, `mousedown`, `mouseover`, `mouseout`, `contextmenu`, `add`, `remove`, `popupopen`, `popupclose`.
- *Métodos*: `addTo`, `bindPopup`, `unbindPopup`, `openPopup`, `closePopup`, `setStyle`, `getBounds`, `bringToFront`, `bringToBack`, `redraw`.

**Polyline — L.polyline**: línea. Extiende `Path`. Requiere las coordenadas de los vértices.
```
L.polyline( <LatLng[]> latlngs, <Polyline options> options? )
```
```javascript
var pointA = new L.LatLng(41.65925, -4.70404);
var pointB = new L.LatLng(41.65166, -4.70421);
var latlngs = [pointA, pointB];
var polyline = L.polyline(latlngs, {color: 'blue'}).addTo(map).bindPopup('Avda. Juan Carlos I');
```

**Polygon — L.polygon**: polígono. Extiende `Polyline`. Requiere las coordenadas de los vértices.
```
L.polygon( <LatLng> latlngs, <Polyline options> options? )
```
```javascript
var polygon = L.polygon([
    [41.67778, -4.72163],
    [41.67349, -4.71511],
    [41.66958, -4.72017],
    [41.67169, -4.72515]
]).addTo(map).bindPopup('Mercaolid');
```

**Rectangle — L.rectangle**: rectángulo. Extiende `Polygon`. Requiere los límites geográficos.
```
L.rectangle( <LatLngBounds> bounds, <Path options> options? )
```
```javascript
var bounds = [[41.71, -4.72], [41.70, -4.74]];
L.rectangle(bounds, {color: "brown", weight: 1}).addTo(map);
```

**Circle — L.circle**: círculo. Extiende `Path`.
```
L.circle( <LatLng> coordenadas del centro, <Number> radio, <Path options> opciones )
```
```javascript
var circle = L.circle([41.658, -4.725], 700, {
    color: 'red', fillColor: '#f03', fillOpacity: 0.5
}).addTo(map);
```

**CircleMarker — L.circleMarker**: circunferencias. Extiende `Circle`. El radio se especifica en **píxeles**: al modificar el zoom del mapa, el tamaño de la circunferencia se mantiene siempre igual.
```
L.circleMarker( <LatLng> latlng, <Path options> options? )
```
```javascript
var circleMarker = L.circleMarker([41.63, -4.775], {radius: 20}).addTo(map);
```

**SVG y Canvas**: son métodos de renderización del mapa (no capas de datos), que heredan de la clase base `Renderer`. Debido a limitaciones técnicas, SVG no está disponible en todos los navegadores (ej. IE7 e IE8).
```javascript
var map = L.map('map', { renderer: L.svg() });
var map = L.map('map', { renderer: L.canvas() });
```

*5.4 Otras capas*

**Grupo de capas — L.layerGroup()**: se utiliza para agrupar varias capas y manejarlas como una sola. Extiende la clase `Layer`. Si se agrega el grupo al mapa, cualquier capa que se añada o elimine del grupo también se añade o elimina del mapa.
```
L.layerGroup( <ILayer[]> layers? )
```
```javascript
var littleton = L.marker([39.61, -105.02]).bindPopup('Littleton, CO.'),
    denver    = L.marker([39.74, -104.99]).bindPopup('Denver, CO.'),
    aurora    = L.marker([39.73, -104.8]).bindPopup('Aurora, CO.'),
    golden    = L.marker([39.77, -105.23]).bindPopup('Golden, CO.');
var cities = L.layerGroup([littleton, denver, aurora, golden]);
```

**Grupo de objetos geográficos — L.featureGroup()**: extiende `LayerGroup`, pero además tiene eventos de ratón y comparte el método `bindPopup`.
```
L.featureGroup( <ILayer[]> layers? )
```
```javascript
L.featureGroup([marker1, marker2, polyline])
    .bindPopup('Hello world!')
    .on('click', function() { alert('Clicked on a group!'); })
    .addTo(map);
```

**GeoJSON — L.geoJson()**: representa un objeto GeoJSON o un listado de objetos GeoJSON. Extiende `FeatureGroup`. Permite utilizar datos GeoJSON y visualizarlos en el mapa.
```
L.geoJson( <Object> geojson?, <GeoJSON options> options? )
```
```javascript
L.geoJSON(data, {
    style: function (feature) { return {color: feature.properties.color}; }
}).bindPopup(function (layer) {
    return layer.feature.properties.description;
}).addTo(map);
```
*Opciones*: `pointToLayer` (función para crear capas de puntos GeoJSON; si no se especifica, se crean marcadores simples), `style` (función para los estilos de las capas de tipo línea y polígono), `onEachFeature` (para llamar a eventos y desplegar popups de los *features*), `filter` (decide si un objeto geográfico se muestra en el mapa o no), `coordsToLatLng` (convierte las coordenadas GeoJSON en puntos LatLng).

**GridLayer — L.gridLayer()**: clase genérica para el manejo de una malla teselada de elementos HTML (`<canvas>`, `<img>` o `<div>`). Es la clase base para todas las capas teseladas y sustituye a la antigua clase `TileLayer.Canvas`. Se encarga de crear y animar estos elementos DOM automáticamente.
```
L.gridLayer( <GridLayer options> options? )
```
```javascript
var CanvasLayer = L.GridLayer.extend({
    createTile: function(coords){
        var tile = L.DomUtil.create('canvas', 'leaflet-tile');
        var size = this.getTileSize();
        tile.width = size.x;
        tile.height = size.y;
        var ctx = tile.getContext('2d');
        return tile;
    }
});
```

**6. Controles**
Los controles permiten a los usuarios navegar con movimientos del ratón (arrastrar para moverse, doble clic para ampliar, botones de acercar/alejar). **Por defecto** solo están habilitados los controles de **zoom** y **atribución**. Leaflet tiene **4 controles**: Zoom, Attribution, Layers, Scale.

**Añadir control — L.control()**: implementa la interfaz `IControl`. Se puede agregar al mapa de dos formas equivalentes: `control.addTo(map);` o `map.addControl(control);`
```
L.control( <Control options> opciones )
```
*Opciones*: `position` — posición inicial del control en el mapa: `topleft`, `topright`, `bottomleft`, `bottomright` (por defecto `topright`). *Métodos*: `setPosition`, `getPosition`, `addTo`, `removeFrom`, `getContainer`.

- **Control de zoom — L.control.zoom**: añade un control de zoom básico (dos botones, acercar/alejar). Se añade al mapa por defecto (a menos que se establezca la opción `zoomControl` a `false`). Extiende `L.control`. Posición por defecto: `topleft`.
- **Control de atribución — L.control.attribution**: muestra los datos de atribución en un pequeño cuadro de texto dentro del mapa. Se añade por defecto (a menos que `attributionControl` se establezca a `false`). Extiende `L.control`. Posición por defecto: `bottomright`.
- **Control de capas — L.control.layers**: crea un control de capas que da al usuario la posibilidad de alternar la visibilidad de las capas (mostrándolas u ocultándolas). Extiende `L.control`. Posición por defecto: `topright`. Distingue entre `baseLayers` (capas base, mutuamente excluyentes) y `overlays` (capas superpuestas). Opción `collapsed` (por defecto `true`; con `false` se ve el control expandido): `L.control.layers(baseLayers, overlays, {collapsed:false}).addTo(map);`
- **Control de escala — L.control.scale**: muestra la escala del centro actual de la pantalla en el sistema métrico (m/km) e imperial (millas/pies). Extiende `L.control`. Posición por defecto: `bottomleft`. Las opciones `metric` e `imperial` vienen habilitadas por defecto, pero se pueden cambiar a `false`: `L.control.scale({imperial: false}).addTo(map);`

**7. Eventos**
Cada vez que algo ocurre en Leaflet (ej. el usuario hace clic en un marcador o el mapa cambia de zoom), el objeto correspondiente envía un **evento** que se puede suscribir a una función, permitiendo reaccionar a la interacción del usuario.
```javascript
map.on('click', function(e) {
    alert(e.latlng);
});
```
Leaflet trabaja con detectores de eventos de referencia, por lo que si se quiere agregar un oyente y luego quitarlo, se debe definir como una **función**:
```javascript
function onClick(e) { ... }
map.on('click', onClick);
map.off('click', onClick);
```
Un **objeto de evento** es el objeto que se recibe como argumento en una función de escucha cuando algún evento se activa, y contiene información útil sobre ese evento (ej. `e.latlng` es el punto geográfico donde ocurre el evento del ratón).

**8. Plugins**
Leaflet es una librería JavaScript *open source* que se centra en un conjunto básico de características, para mantenerse lo más ligera posible. Si se necesita más funcionalidad hay que recurrir a **plugins**. Uno de los aspectos clave de Leaflet es que ofrece un buen código base sobre el que desarrollar complementos.

*¿Cómo incorporo los plugins a mi mapa de Leaflet?*
1. Acceder al repositorio oficial de plugins.
2. Descargar el plugin (botón *Download ZIP*) y descomprimir el archivo.
3. Añadir la librería en la cabecera del HTML, por ejemplo: `<script src="leaflet-master\layer\tile\ejemplo.js"></script>`
4. Utilizar la nueva librería, por ejemplo: `L.control.mousePosition().addTo(map);`

---

## Ejercicios prácticos Unidad 5 — HTML5, CSS y JavaScript. Depuración de errores

Guía práctica paso a paso — fundamentos de HTML, CSS y JavaScript, y depuración de errores en el navegador (necesarios como base antes de programar con Leaflet):

**1. Estructura de un documento HTML**
- Un documento HTML tiene tres etiquetas que describen su estructura general: `<html>`, `<head>` y `<body>`.
- Dentro de un HTML se debe escribir siempre `<!doctype html>` en la primera línea, para indicar al navegador el lenguaje que está leyendo (en este caso, HTML5). *Doctype* comenzó a utilizarse en HTML4.01 y XHTML.
- **La cabecera `<head>`**: incluye información importante, como el título de la página (`<title>`, aparece en la pestaña del navegador y en los buscadores). La etiqueta `<meta>` define metadatos: `<meta charset="UTF-8">` especifica la codificación (UTF-8 = *Unicode Transformation Format* 8-bit, compatible con ASCII y con todos los idiomas); otras etiquetas meta como `description` o `keywords` dan información sobre el contenido no visible para el usuario pero relevante para las búsquedas. La etiqueta `<link rel="stylesheet" href="...">` incorpora archivos externos (ej. una hoja de estilos CSS).
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="description" content="Mi primer HTML">
        <meta name="keywords" content="HTML, MappinGIS, Leaflet">
        <link rel="stylesheet" type="text/css" href="mihojadeestilos.css">
        <title> MappingGIS.com </title>
    </head>
</html>
```
- **El cuerpo `<body>`**: contiene el contenido visible en la página web (párrafos, imágenes, encabezados, listas, etc.).
- *Codificación*: si al abrir el navegador aparecen caracteres extraños (tildes, ñ, etc.), hay que revisar la codificación del archivo y establecerla en UTF-8 con el editor de texto (Notepad++ o Sublime Text).

**2. Etiquetas de HTML**
- Lo que va dentro de `<` y `>` son **etiquetas**, que casi siempre vienen en pares (una de inicio y una de cierre, ej. `<html>` ... `</html>`). El texto entre ambas es el **contenido** del elemento. Las etiquetas pueden anidarse, pero deben cerrarse en el orden correcto (la última abierta debe ser la primera cerrada).
- **Párrafos y encabezados**: cada párrafo requiere `<p>` ... `</p>`. HTML permite seis tamaños de encabezado, de `<h1>` (más importante) a `<h6>` (menos importante).
- **Listas**: se crean con `<ul>` (lista sin orden definido) combinada con `<li>` para cada elemento.
```html
<h2>Lista de capas base</h2>
<ul>
    <li>Stamen</li>
    <li>OpenStreetMap</li>
    <li>Google Maps</li>
</ul>
```
- **Atributos de las etiquetas**: proveen información adicional a los elementos HTML, con la estructura `nombre="valor"`, siempre en la etiqueta de apertura y con el valor entre comillas. Ejemplo: `<body bgcolor="#FFFF00">` (fondo amarillo).
- **Imágenes**: se añaden con la etiqueta `<img src="URL">`, donde `src` (*source*) indica la URL de la imagen.

**3. La indentación**
Es el espaciado desde el margen en cada línea; cuando se anidan etiquetas, se indentan aún más para facilitar la lectura del código. JavaScript no requiere indentación (es recomendable pero no necesaria), pero es una buena práctica en HTML.

**4. Comentarios**
- En HTML comienzan con `<!--` y terminan con `-->`: `<!-- ¡Este es un ejemplo de un comentario en HTML! -->`
- En CSS lucen así: `/* ¡Soy un comentario! */`

**5. Estilos en línea**
Es posible aplicar CSS directamente en las etiquetas mediante el atributo `style`, sin necesidad de un archivo CSS aparte:
- Tamaño de fuente: `<p style="font-size: 12px"></p>`
- Color de fuente: `<p style="color:red"></p>`
- Familia tipográfica: `<p style="font-family:Futura"></p>`
- Color de fondo: `<body style="background-color: blue">`
- Combinando propiedades con `;`: `<p style="color: red; font-size:8px"></p>`

**6. Etiqueta iframe**
La etiqueta `<iframe>` crea un espacio dentro de la página donde se puede incrustar otra página web, con sus propios contenidos y estilos, y perfectamente funcional (enlaces, scripts, etc. de manera autónoma).
```html
<iframe style="border: none;" height="400" width="600"
    src="http://localhost:8080/geoserver/www/web.html"></iframe>
```

**7. CSS — sintaxis**
El formato general de una regla CSS es:
```css
selector {
    propiedad: valor;
}
```
Un **selector** puede ser cualquier elemento de HTML (`<p>`, `<img>`, `<table>`...), omitiendo los `<>`. Una **propiedad** es un aspecto del selector (ej. `font-family`, `color`, `font-size`). Un **valor** es una posible configuración de esa propiedad. Cada par propiedad-valor debe terminar con `;`.
```css
p {
    font-family: Arial;
    color: blue;
    font-size: 24px;
}
```
Para incluir CSS dentro del HTML se añaden las etiquetas `<style>` y `</style>` **dentro de `<head>`**. Para incluir un archivo CSS externo, se usa `<link>` en la cabecera con tres atributos: `type="text/css"`, `rel="stylesheet"` y `href` (ruta del archivo CSS).

**8. Selectores CSS: elementos, clases e identificadores**
- **Todos los elementos de HTML** son selectores posibles (`h1`, `p`, etc.).
- **Las clases** son útiles cuando varios elementos deben compartir el mismo estilo. Se asignan con `class="nombre"` en HTML, y en CSS se identifican con un punto (`.`):
```css
.cuadrado { height: 100px; width: 100px; }
```
```html
<span class="nota">texto destacado</span>
```
- **Los identificadores** son la mejor opción cuando se quiere aplicar un estilo a un único elemento. Se asignan con `id="nombre"` en HTML, y en CSS se identifican con `#`:
```css
#intro { color: #FF0000; }
```
```html
<p id="intro">Texto de introducción</p>
```

**9. Introducción a JavaScript**
JavaScript es uno de los lenguajes de programación más importantes, porque en él se programan las aplicaciones para internet y la web. Los navegadores modernos soportan la versión JavaScript 1.5 (diciembre de 2009).

*Valores (tipos de JavaScript):*
- **number**: cantidades, permiten operaciones matemáticas (`1`, `2`, `10.5`).
- **strings**: secuencias de caracteres entre comillas (`"¿Cuál es tu nombre?"`).
- **booleanos**: `true` (verdadero) o `false` (falso); resultan de sentencias de comparación (`10 > 3` es `true`).
- **undefined / null**: valores "sin definir".

Todos los valores en JavaScript tienen **propiedades** (clave-valor, accesibles con el operador punto `.`). Ejemplo: `'texto'.length` → `5`.

*Objetos*: representan agregaciones estructuradas de valores. Se agrupan en clases: `Object`, `Array`, `Date`. Todos los valores que no son primitivos son *objetos*:
- **Objetos planos** (tipo `object`), creados por objetos literales: `{ Nombre: 'Felipe', Apellidos: 'González' }`
- **Matrices** (tipo `Array`), creadas por literales de matriz: `['cities', 'countries', 'ocean']` (se accede a sus elementos por índice numérico, empezando en 0).
- **Expresiones regulares** (tipo `RegExp`), creadas por literales de expresión regular: `/^a+b+$/`
- **Objeto nulo**.

*Operadores y expresiones*: con los tipos y objetos se pueden crear expresiones utilizando operadores, ej. operaciones matemáticas (`+`, `-`, `*`, `/`): `5 + 5 => 10`

**10. Programa, sentencias, comentarios y variables**
- Un **programa** es una secuencia de sentencias que se ejecutan en el orden en que han sido definidas.
- Las **sentencias** realizan tareas al ejecutarse (ej. `var x = 5`).
- Comentarios de una sola línea: `// comentario`. Comentarios multilínea: `/* comentario */`. Es recomendable usar comentarios monolínea `//`.
- **Variables**: se declaran con la palabra reservada **`var`**, seguida del nombre (sensible a mayúsculas/minúsculas: `MiMapa` y `mimapa` son variables distintas). Se pueden crear varias variables en una sentencia separando las definiciones por comas.
```javascript
var nombre; // declara la variable 'nombre' (valor undefined)
var x = 1; // declara y asigna el valor 1 a x
var osm = L.tileLayer(); // declara y asigna el valor de una capa de teselas
```
Si se intenta usar una variable no declarada, se produce un error, ej.: `ReferenceError: y is not defined`.

**11. Sintaxis de JavaScript**
- **Delimitación de sentencias**: los `;` delimitan el final de una sentencia. Son opcionales, pero se recomienda utilizarlos siempre (más legibilidad y seguridad).
- **Nombre de variables**: debe comenzar por letra, `_` o `$` (ej. `x`, `map`, `map1`, `_map`, `&f`); no puede comenzar por números ni ser una palabra reservada.
- **Orden en la creación de variables**: JavaScript es un lenguaje de procedimientos, que lee el código de arriba hacia abajo; no se puede utilizar una variable que aún no haya sido creada, aunque se defina más adelante. Ejemplo de error típico: usar una capa (`OSM`) como `layers` del mapa antes de haberla creado con `var OSM = new L.tileLayer(...)`, generando `ReferenceError: OSM is not defined`. La solución es reordenar el código, declarando primero la variable y usándola después.
- **Declaraciones y expresiones**: las **declaraciones** "hacen cosas" (ej. `var foo;` declara/crea una variable). Las **expresiones** producen valores, y son el lado derecho de una asignación o los argumentos de funciones (ej. `2 + 1`).

**12. Funciones útiles**
- Un **script** es un programa JavaScript insertado en una página HTML, delimitado por `<script type="text/javascript">`.
- `document.write("Texto")` inserta un texto en la página web.
- `alert("Texto")` muestra un mensaje al usuario en una ventana emergente.
- `confirm()` presenta un mensaje y pide confirmación o rechazo.
- `prompt(msj)` presenta un mensaje y pide un dato de entrada.

**13. Funciones**
Una función se puede definir mediante una **declaración de función**:
```javascript
function add(param1, param2) {
    return param1 + param2;
}
```
Se llama así: `add(6, 1)` → `7`; `add('a', 'b')` → `'ab'`. También puede definirse mediante una **expresión de función**:
```javascript
var add = function(param1, param2) {
    return param1 + param2;
};
```
Partes de una función: (1) se declara con `var` y se le asigna un nombre; (2) se usa `function` para indicar que se va a definir una función; (3) el contenido entre paréntesis son los **parámetros**; (4) el código reusable se escribe entre `{ }`, y cada línea debe terminar con `;`.

**14. Condicionales y bucles**
Las principales declaraciones para establecer condiciones son **if, switch, for y while**.
- **IF**: controla la expresión entre paréntesis y procesa las instrucciones entre llaves si la condición es verdadera.
```javascript
var mivariable = 9;
if (mivariable < 10) {
    alert("El valor es menor que 10");
}
```
- **SWITCH**: se utiliza para comprobar múltiples condiciones; evalúa una expresión, compara el resultado con las opciones `case` y devuelve el resultado correspondiente (con `break` al final de cada caso), o el valor por `default` si ninguna coincide.
```javascript
var mivariable = 3;
switch(mivariable) {
    case 5: alert("El valor es cinco"); break;
    case 8: alert("El valor es ocho"); break;
    case 10: alert("El valor es diez"); break;
    default: alert("El valor es " + mivariable);
}
```
- **FOR**: ejecuta el código entre llaves mientras la condición indicada en el segundo parámetro sea verdadera. Sintaxis: `for (inicialización; condición, incremento)`.
```javascript
var mivariable = 9;
for(var f = 0; f < mivariable; f++) {
    alert("El valor actual es " + f);
}
```
- **WHILE / DO-WHILE**: la declaración `while` requiere la condición entre paréntesis y el código a ejecutar entre llaves; el bucle se ejecuta hasta que la condición es falsa. Con `do { ... } while(condición)` el código se ejecuta **al menos una vez** antes de evaluar la condición.
```javascript
var mivariable = 9;
do {
    mivariable++;
} while (mivariable > 100);
alert("El valor de mivariable es " + mivariable); // 10
```

**15. Depuración de JavaScript**
Hasta hace unos años, la depuración de JavaScript en sitios web consistía en escribir código en un editor de texto, añadir declaraciones `alert` para inspeccionar valores, y repetir hasta que las cosas funcionasen. Hoy los principales navegadores incluyen herramientas de depuración para desarrolladores.

- **Corrección de errores con Firefox**: se accede a la opción **Consola de errores** dentro del menú **Herramientas** (o botón derecho → **Inspeccionar elemento** → pestaña **Consola**). La consola diferencia mensajes de información, aviso y error; por cada error se indica la posible solución en inglés y el fragmento de código donde se produjo, con un enlace a la línea concreta del archivo.
  - *Ejemplo práctico*: un mapa de OpenLayers no aparece. La consola muestra `ReferenceError: Ol is not defined` en la línea correspondiente. Al inspeccionar el código se detecta que se escribió `Ol.layer.Tile` en vez de `ol.layer.Tile` (JavaScript distingue mayúsculas/minúsculas). Se corrige en el editor de texto, se guarda y se actualiza el navegador.
- **Depuración de errores con Chrome**: botón derecho → **Inspeccionar**, para abrir las **Herramientas de desarrollo**. La pestaña **Elements** permite inspeccionar el estado del DOM y los estilos aplicados (los cambios en esta pestaña son solo temporales, no se guardan en el archivo de origen). La pestaña **Console** muestra los errores (ej. `Uncaught ReferenceError: Ol is not defined`); al hacer clic sobre la línea del error se accede a la pestaña **Sources**, donde se resalta la línea exacta del problema.

**16. Ejercicios propuestos**
- **Ejercicio n°1**: modificar el título de la página y el texto del cuerpo; captura de pantalla del resultado.
- **Ejercicio n°2**: crear una lista HTML con libros/películas favoritas, con marcador cuadrado, primer elemento en negrita y color de fondo elegido.
- **Ejercicio n°3**: sustituir un párrafo por el mismo texto convertido en comentario HTML.
- **Ejercicio n°4**: añadir un párrafo "Mapa de Leaflet" en azul, tamaño 18 y fuente Tahoma, mediante estilos en línea.
- **Ejercicio n°5**: incluir propiedades y valores dentro de las etiquetas `<style>` de la cabecera.
- **Ejercicio n°6**: escribir un texto con encabezado y varios párrafos, destacando partes mediante clases CSS (`<span class="...">`).
- **Ejercicio n°7**: escribir dos textos con estilos diferentes mediante dos identificadores `id`.
- **Ejercicio n°8**: insertar y ejecutar un bucle `for` en un HTML, describiendo el resultado.
- **Ejercicio n°9**: depurar una web con varios errores (etiqueta `<html>` sin cerrar, selector CSS `.p` en vez de `p`, nombre de variable inválido `#x`, referencia a variable no definida `y` en `document.write(y)`), utilizando el depurador del navegador hasta lograr visualizar correctamente la página (título "Mapa de Leaflet", imagen y el comentario "Insertando una imagen").

---

## Ejercicios prácticos Unidad 5-1 — Leaflet

Guía práctica paso a paso: construcción progresiva de un visor Leaflet, desde el mapa básico hasta capas GeoJSON, servicios WFS y plugins (archivos `L_map1.html` a `L_map12.html`).

**1. Creación de un mapa sencillo con la API de Leaflet (`L_map1.html`)**
- Se crea el marco HTML básico, con las etiquetas `<meta>` para codificación y visualización responsive (`viewport`), y un `<div id="map">` en el `<body>`. Se guarda en `\data_dir\www\L_map1.html`.
- Se incluye en la cabecera la librería `leaflet.js` y la hoja de estilo `leaflet.css` mediante CDN.
- Se fija el estilo del contenedor del mapa a pantalla completa (`html, body, #map { height: 100%; }`).
- Código de inicialización: se crea el mapa centrado en Valladolid con `L.map('map', {center: [41.66, -4.72], zoom: 15});` y se añade la capa base OSM como variable `OSM = L.tileLayer(...)` referenciada en la opción `layers` del mapa (en lugar de usar `.addTo(map)` directamente).
- Se desactiva el zoom con la rueda del ratón en entornos móviles: `scrollWheelZoom: false`.
- Se añade un control de escala: `L.control.scale().addTo(map);`
- **Importante**: para evitar errores, los visores deben abrirse escribiendo la URL en el navegador (`http://localhost:8080/geoserver/www/L_map1.html`), no con doble clic sobre el archivo.
- **Ejercicio n°1**: pegar el resultado del primer mapa Leaflet en la plantilla de resultados.

**2. Capas teseladas WMS (`L_map2.html`)**
- Copia de `L_map1.html`, cambiando el zoom inicial a 4.
- Se añade, debajo de la capa OSM, una capa WMS de GeoServer mediante `L.tileLayer.wms("http://localhost:8080/geoserver/wms", {layers: 'cities', format: 'image/png', transparent: true, tiled: true, attribution: "Natural Earth"});` (el parámetro `tiled: true` fuerza el uso de capas teseladas).
- Se agrega al mapa con `layers: [osm, cities]`.
- **Ejercicio n°2**: añadir al mapa las capas *rivers*, *countries* y *cities* (con el estilo `cities_filter` en la propiedad `styles` de la capa `cities`), jugando con el orden y la transparencia de las capas.

**3. Añadiendo capas de interfaz de usuario al mapa (`L_map3.html`)**
- **Insertar un marcador**: `var marker = L.marker([41.66, -4.71]).addTo(map)`, con opciones `draggable` y `title`, y un popup asociado mediante `.bindPopup('Universidad de Valladolid').openPopup();`
- **Insertar un icono**: se crea un objeto `L.icon` (`iconUrl`, `iconSize`, `popupAnchor`) y se pasa como opción `icon` al crear el marcador.
- **Capas vectoriales**: agregar un círculo (`L.circle`, con centro, radio en metros y opciones de color), un polígono (`L.polygon`, con array de vértices), etiquetas (`polygon.bindTooltip("Soy una etiqueta", {permanent: true})`) y una línea (`L.polyline`, con array de puntos `L.LatLng`).
- **Ejercicio n°3**: añadir además un marcador circular (`L.circleMarker`) a las geometrías anteriores.

**4. Trabajando con grupos de capas (`L_map4.html`)**
- Se comentan todos los métodos `.addTo(map)` de las geometrías creadas (polyline, polygon, circle, circleMarker, marker, marker2), de forma que al abrir el mapa no se vea ninguna geometría.
- Se crea un grupo de capas que las incluye a todas y se añade al mapa: `var geometrias = L.layerGroup([polyline, polygon, circle, circleMarker, marker, marker2]).addTo(map);`
- Con el método `eachLayer` se itera sobre cada capa del grupo para asignarle un popup común: `geometrias.eachLayer(function(layer) { layer.bindPopup('Pertenezco a un grupo de geometrías'); });`
- **Ejercicio n°4**: captura de pantalla del mapa y del mensaje al hacer clic sobre un elemento.

**5. Trabajando con eventos (`L_map5.html`)**
```javascript
function onMapClick(e) {
    alert("Has hecho clic en " + e.latlng);
}
map.on('click', onMapClick);
```
- **Ejercicio n°5**: captura de pantalla del resultado.

**6. Controles**

*Control de escala (`L_map6.html`)*: copia de `L_map2.html`. Por defecto la posición del control es `bottomleft`. Se modifica la posición a `bottomright` y se desactiva la escala imperial: `L.control.scale({position: 'bottomright', imperial: false}).addTo(map);`
- **Ejercicio n°6**: cambiar el ancho máximo del control de escala a 75 píxeles.

*Control de capas (`L_map7.html`)*: copia de `L_map2.html`. Se crean las variables de las capas (`osm`, `paises`, `ciudades` con `L.tileLayer.wms`), y dos objetos clave/valor: `baseMaps` (capas base) y `overlayMaps` (capas superpuestas). Se añaden al mapa inicial (`layers: [osm, paises, ciudades]`) y se crea el control: `L.control.layers(baseMaps, overlayMaps).addTo(map);` Se puede omitir cualquiera de los dos argumentos pasando `null`. Con la opción `{collapsed:false}` el control se muestra siempre desplegado. Es posible añadir un icono antes del nombre de cada capa incluyendo código HTML `<img>` como clave del objeto.
- **Ejercicio n°7**: captura de pantalla del resultado.

*Control de títulos y subtítulos (`L_map8.html`)*: copia de `L_map2.html`. Se crea un nuevo control `var title = L.control();` con un método `onAdd` que crea un bloque `<div>` (mediante `L.DomUtil.create('div', 'info')`) con contenido HTML (`<h2>` y párrafo), y se añade al mapa con `title.addTo(map);`. El estilo se define en CSS mediante la clase `.info`.
- **Ejercicio n°8**: añadir el título al mapa y captura de pantalla.

*Control de leyenda (`L_map9.html`)*: copia de `L_map2.html`. Se crea un control `legend` (posición `bottomright`) cuyo `onAdd` crea un `<div>` con una imagen (`<img>`). En lugar de apuntar a un archivo PNG estático, se recomienda usar la respuesta del servicio WMS de GeoServer **`GetLegendGraphic`**, que devuelve la leyenda de una capa (o grupo de capas) como PNG:
```
http://localhost:8080/geoserver/wms?REQUEST=GetLegendGraphic&VERSION=1.0.0&FORMAT=image/png&WIDTH=20&HEIGHT=20&LAYER=earth:cities
```
Se puede forzar un estilo concreto con el parámetro `&Style=cities_filter`, y mostrar varias capas WMS pasando el nombre de un grupo de capas como `LAYER`. El estilo de la leyenda se puede personalizar con CSS (ej. clase `.legend { opacity: 0.7; }`).
- **Ejercicio n°9**: añadir la leyenda de la capa *cities* con el estilo *cities_filter*.

**7. Capas vectoriales — el formato GeoJSON (`L_map10.html`)**
- Se crea un mapa de cloropletas interactivo de los países del mundo. Se modifica el código para que el objeto `map` no tenga la opción `layers`, con zoom inicial 4.
- Se sustituyen los *tiles* de OSM por *tiles* de **MapBox** con escala de grises (`L.tileLayer` apuntando a `api.mapbox.com`, con `access_token`, `id: 'mapbox/streets-v11'`, `tileSize: 512`, `zoomOffset: -1`).
- Se convierte la capa `countries.shp` a formato **GeoJSON**, mediante alguna de estas vías: la librería *open source* **ogr2ogr**; un conversor online (*HTML5 Shapefile to GeoJSON Converter*, *MyGeodata Converter*); o un cliente SIG como **QGIS** (`Capa > Guardar como...` → formato GeoJSON).
- Se cambia la extensión del archivo generado de `.geojson` a **`.js`**, y con un editor de texto se añade `var countries = ` justo antes del contenido existente, de modo que el archivo completo asigna el GeoJSON a la variable `countries`.
- Se vincula el archivo `countries.js` en la cabecera del HTML: `<script type="text/javascript" src="countries.js"></script>`
- Se añaden los objetos GeoJSON al mapa mediante una capa GeoJSON: `L.geoJson(countries).addTo(map);`
- **Un poco de color**: se define un objeto de estilo (`countryStyle`, con `color`, `weight`, `opacity`) y se aplica: `L.geoJson(countries, {style: countryStyle}).addTo(map);`
- Se da color a los países según su población, con ayuda de la herramienta **ColorBrewer** para elegir colores agradables. Se crea una función `getColor(d)` que devuelve un color hexadecimal según rangos de población, y una función `style(feature)` que aplica `fillColor: getColor(feature.properties.pop_est)`, junto con un borde blanco discontinuo (`color: 'white', dashArray: '3'`).
- **Interactuando con el mapa**: se define una función `popup(feature, layer)` que comprueba si existe `feature.properties.name` y, si es así, vincula un popup con `layer.bindPopup(feature.properties.name)`. Se pasa como propiedad `onEachFeature` de `L.geoJson`: `geojson = L.geoJson(countries, {style: style, onEachFeature: popup}).addTo(map);`
- **Ejercicio n°10**: captura de pantalla del resultado.

**8. Añadir una capa WFS de GeoServer y mostrar en una ventana emergente sus atributos mediante AJAX (`L_map11.html`)**
- Copia de `L_map1.html`, sin la opción `layers`, con zoom inicial 2.
- Se añade la librería **jQuery**: `<script src="https://code.jquery.com/jquery-3.5.1.js"></script>` — librería JavaScript de código abierto que simplifica la programación y permite agregar interactividad sin conocimientos avanzados del lenguaje.
- Se construye la URL de la petición **WFS** con GeoServer mediante un objeto de parámetros por defecto (`service: 'WFS'`, `version: '1.0.0'`, `request: 'GetFeature'`, `typeName: 'earth:countries'`, `outputFormat: 'application/json'`) y las utilidades `L.Util.extend` y `L.Util.getParamString`.
- **AJAX** (*Asynchronous JavaScript and XML*) permite hacer peticiones al servidor (intercambiar datos) sin recargar la página. Se usa el método `$.ajax()` de jQuery, con la URL construida y una función `success` que crea la capa GeoJSON al recibir la respuesta, con estilo propio y un popup mostrando el nombre del país (`feature.properties.name`) al hacer clic:
```javascript
$.ajax({
    url: URL,
    success: function(data) {
        var geojson = new L.geoJson(data, {
            style: {"color":"#2ECCFA","weight":2},
            onEachFeature: function(feature, layer){
                layer.bindPopup("Has hecho click en " + feature.properties.name);
            }
        }).addTo(map);
    }
});
```
- **Ejercicio n°11**: captura de pantalla del resultado.

**9. Extendiendo la funcionalidad de Leaflet mediante plugins (`L_map12.html`)**
*Insertando un control de búsqueda de atributos en una capa estática GeoJSON:*
- Copia de `L_map10.html` (con la capa `countries` en GeoJSON).
- Se accede a la página de plugins de Leaflet (leafletjs.com/plugins.html), sección *Overlay interaction* → *Search & popups* → plugin **Leaflet Search** (de Stefano Cudini).
- Se puede incorporar de dos formas: (1) descargando el plugin (*Download ZIP*) y colocándolo en el mismo directorio que el HTML, vinculando el `.js` y el `.css` locales; o (2) mediante un **enlace CDN** (ej. desde jsdelivr.com), sin necesidad de descargar archivos.
- Se crea una variable `countriesJS = L.geoJson(countries, {onEachFeature: popup, style: style}).addTo(map);` y un control de búsqueda mediante la clase **`L.Control.Search`**, indicando la capa (`layer`) y el campo de búsqueda (`propertyName: 'name'`): `var searchControl = new L.Control.Search({layer: countriesJS, propertyName: 'name'});` Se añade al mapa con `map.addControl(searchControl);`
- Por defecto, al hacer clic en un resultado aparece una circunferencia roja (opción `circleLocation`, `true` por defecto); en una capa de polígonos interesa más resaltar el polígono con otro color, por lo que se desactiva: `marker: false`.
- Se define un estilo para el resultado de la búsqueda mediante el evento `search:locationfound`: `searchControl.on('search:locationfound', function(e) { e.layer.setStyle({fillColor: '#3f0', color: '#0f0'}); });`
- Para restaurar el color original al limpiar la búsqueda, se usa el evento `search:collapsed`, iterando con `eachLayer` y `resetStyle`: `.on('search:collapsed', function(e) { countriesJS.eachLayer(function(layer) { countriesJS.resetStyle(layer); }); });`
- **Ejercicio n°12**: captura de pantalla del resultado.

---

