# Ejercicios — Unidad 5

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
