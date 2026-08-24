# Ejercicios — Unidad 6

Guía práctica paso a paso: instalación de OpenLayers (CDN y arquitectura Node.js/npm), publicación en GeoServer, y construcción progresiva de un visor OpenLayers a través de 16 ejercicios (archivos `ol_map1.js` a `ol_map16.js`).

**1. Dos arquitecturas de trabajo con OpenLayers**
El curso presenta dos formas de trabajar con OpenLayers, con implicaciones distintas para el desarrollo y la publicación final:

| Arquitectura | Descripción | Uso recomendado |
|---|---|---|
| **CDN / archivo único** | Se enlaza `ol.js`/`ol.css` en el HTML (o se referencian desde un CDN) y se escribe JavaScript "clásico" con el espacio de nombres global `ol.*`. No requiere Node.js ni herramientas de compilación. | Aprendizaje, prototipos rápidos, ejercicios sencillos |
| **Proyecto Node.js / npm (Vite)** | Se crea un proyecto con `npm create ol-app`, se importan módulos ES6 (`import {Map, View} from 'ol'`), se ejecuta un servidor de desarrollo (`npm start`) y se genera una versión de producción optimizada (`npm run build`). | Aplicaciones profesionales, proyectos que se van a mantener/escalar en el tiempo |

**2. Primer mapa con OpenLayers vía CDN (`ol_basicMap.html`)**
- Se crea un documento HTML básico (`<!DOCTYPE html>`, `<head>`, `<body>`), con un `<div id="map">` y su estilo (dimensiones a pantalla completa).
- En la cabecera se enlazan la hoja de estilos `ol.css` y el script `ol.js` mediante CDN (ej. jsdelivr o unpkg).
- Se crea el mapa reutilizando el patrón visto en la teoría (`ol.Map` + `ol.layer.Tile` con `ol.source.OSM` + `ol.View` con `ol.proj.fromLonLat` para convertir coordenadas lon/lat a la proyección del mapa, EPSG:3857 por defecto):
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Mi primer mapa OpenLayers</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@latest/ol.css">
    <script src="https://cdn.jsdelivr.net/npm/ol@latest/dist/ol.js"></script>
    <style>
        html, body, #map { margin: 0; padding: 0; height: 100%; width: 100%; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script type="text/javascript">
        var map = new ol.Map({
            target: 'map',
            layers: [
                new ol.layer.Tile({ source: new ol.source.OSM() })
            ],
            view: new ol.View({
                center: ol.proj.fromLonLat([-4.72, 41.66]),
                zoom: 15
            })
        });
    </script>
</body>
</html>
```
- El archivo se guarda como `ol_basicMap.html` dentro del directorio `www` de GeoServer (`\data_dir\www\`), y se visualiza escribiendo la URL en el navegador: `http://localhost:8080/geoserver/www/ol_basicMap.html` (igual que en Leaflet, no se debe abrir con doble clic).

**3. Corrección CORS en GeoServer (`web.xml`)**
- Al desarrollar aplicaciones OpenLayers que consultan capas WMS/WFS de un GeoServer distinto del origen de la propia página, el navegador puede bloquear las peticiones por la política de mismo origen (**CORS**, *Cross-Origin Resource Sharing*).
- **Solución del curso:** habilitar CORS en GeoServer editando el archivo `web.xml`, ubicado en `<GEOSERVER_HOME>\webapps\geoserver\WEB-INF\web.xml`, **descomentando** el bloque de filtro CORS ya incluido por defecto en GeoServer (el filtro `CorsFilter`, normalmente comentado con `<!-- -->`), de forma que quede activo. Tras el cambio es necesario reiniciar GeoServer (`shutdown.bat` y `startup.bat`) para que surta efecto.

**4. Instalación de Node.js y Git (prerrequisitos para `npm create ol-app`)**
- Para trabajar con la arquitectura de proyecto Node.js/npm es necesario tener instalados **Node.js** (que incluye `npm`, su gestor de paquetes) y **Git** (necesario porque algunas plantillas y dependencias de `npm create ol-app` se descargan/gestionan mediante repositorios Git).
- **Instalación de Node.js:** se descarga el instalador desde nodejs.org (versión LTS recomendada) y se instala con las opciones por defecto; se verifica la instalación abriendo una terminal y ejecutando:
```
node -v
npm -v
```
- **Instalación de Git en Windows** (procedimiento detallado en la guía anexa del curso, *Instalar_GIT.pdf*):
  1. Descargar el instalador desde **git-scm.com/downloads**, eligiendo la versión para Windows.
  2. Ejecutar el instalador y avanzar por el asistente aceptando las opciones recomendadas por defecto en cada pantalla (licencia, carpeta de destino, componentes a instalar —incluyendo *Git Bash* y la integración con el explorador de archivos—, editor de texto por defecto, nombre de la rama inicial, PATH del entorno, cliente SSH, librería OpenSSL, terminal a usar con Git Bash, comportamiento de `git pull`, y demás ajustes avanzados).
  3. Una vez instalado, se abre **Git Bash** (terminal incluida con Git) para comprobar la instalación:
```
git --version
```
  4. Se cierra la terminal con el comando `exit`.
- Con Node.js y Git instalados, ya se puede proceder a crear el proyecto OpenLayers con `npm`.

**5. Creación del proyecto con `npm create ol-app`**
- Desde una terminal, situados en el directorio donde se quiera crear el proyecto, se ejecuta:
```
npm create ol-app@latest mi-mapa-ol
cd mi-mapa-ol
npm install
```
- El asistente genera una estructura de proyecto basada en **Vite** (empaquetador/servidor de desarrollo moderno), con, entre otros, los archivos: `index.html`, `main.js`, `style.css`, `package.json` y la carpeta `node_modules` (dependencias).
- **Servidor de desarrollo:** `npm start` levanta un servidor local (por defecto en `http://localhost:5173`) con recarga automática al modificar el código.
- **Generar versión de producción:** `npm run build` compila y optimiza el proyecto (aplicando *tree-shaking* y minificación) en una carpeta `/dist`, lista para desplegarse en cualquier servidor web (incluido el directorio `www` de GeoServer).

**6. Contenido de los archivos generados por `npm create ol-app`**

| Archivo | Contenido |
|---|---|
| `index.html` | Documento HTML mínimo con un `<div id="map">` y la referencia al script principal `main.js` mediante `<script type="module" src="./main.js"></script>` |
| `main.js` | Código JavaScript del mapa, escrito con **imports de módulos ES6** (`import {Map, View} from 'ol';`, `import TileLayer from 'ol/layer/Tile';`, `import OSM from 'ol/source/OSM';`, etc.) en lugar del espacio de nombres global `ol.*` |
| `style.css` | Estilos CSS del contenedor del mapa (equivalente al `<style>` usado en la versión CDN) |

*Comparativa de nombres de clase — CDN (`ol.*`) vs módulos (npm):*

| Uso con CDN (global `ol.*`) | Uso con npm (módulos ES6) |
|---|---|
| `ol.Map` | `import { Map } from 'ol';` |
| `ol.View` | `import { View } from 'ol';` |
| `ol.layer.Tile` | `import TileLayer from 'ol/layer/Tile';` |
| `ol.source.OSM` | `import OSM from 'ol/source/OSM';` |
| `ol.proj.fromLonLat` | `import { fromLonLat } from 'ol/proj';` |

**7. Publicación del proyecto Node.js en GeoServer**
- Tras ejecutar `npm run build`, el contenido generado en la carpeta `/dist` (archivos HTML, JS y CSS ya optimizados) se copia dentro del directorio `www` de GeoServer (ej. `\data_dir\www\dist\`), de forma que quede accesible como cualquier otro contenido estático servido por GeoServer, en una URL del tipo `http://localhost:8080/geoserver/www/dist/index.html`.

**8. Recapitulación de la arquitectura**
- En la versión **CDN**, el navegador descarga la librería OpenLayers completa desde un servidor externo cada vez que se carga la página, y todo el código de la aplicación se escribe en un único archivo (o pocos archivos) sin proceso de compilación.
- En la versión **Node.js/npm**, el desarrollo se realiza de forma modular (import/export de ES6), con un servidor de desarrollo local que facilita la depuración, y el resultado final es una versión **compilada y optimizada** (solo incluye el código realmente utilizado) que se publica como contenido estático en cualquier servidor web, incluido GeoServer.

A partir de aquí, los ejercicios progresivos se desarrollan copiando y ampliando sucesivamente un mismo archivo JavaScript (`ol_map1.js`, `ol_map2.js`... `ol_map16.js`), vinculado desde un HTML común similar al de `ol_basicMap.html`.

**Ejercicio n°1 — Proyección de coordenadas (`ol_map1.js`)**
- Se parte del mapa básico y se practica el uso de **`ol.proj.fromLonLat([lon, lat])`**, que convierte coordenadas geográficas (longitud/latitud, EPSG:4326) a la proyección por defecto del mapa (EPSG:3857, Web Mercator), necesaria para posicionar correctamente el `center` de la vista.
```javascript
var map = new ol.Map({
    target: 'map',
    layers: [ new ol.layer.Tile({ source: new ol.source.OSM() }) ],
    view: new ol.View({
        center: ol.proj.fromLonLat([-4.72, 41.66]),
        zoom: 15
    })
});
```

**Ejercicio n°2 — La vista como objeto independiente (`ol_map2.js`)**
- Se extrae la vista del mapa a una variable propia, `Mivista`, y se practican sus métodos `setZoom()` y `setRotation()`:
```javascript
var Mivista = new ol.View({
    center: ol.proj.fromLonLat([-4.72, 41.66]),
    zoom: 6
});

var map = new ol.Map({
    target: 'map',
    layers: [ new ol.layer.Tile({ source: new ol.source.OSM() }) ],
    view: Mivista
});

Mivista.setZoom(10);
Mivista.setRotation(Math.PI / 6);
```

**Ejercicio n°3 — Capas WMS de imagen y varias capas en el mapa (`ol_map3.js`)**
- Se añade una capa `ol.layer.Image` con `ol.source.ImageWMS` apuntando a GeoServer, y se practica el uso de un **array de capas** con más de un elemento (orden de dibujo: la primera del array se dibuja primero, quedando debajo de las siguientes):
```javascript
var capaPaises = new ol.layer.Image({
    source: new ol.source.ImageWMS({
        url: 'http://localhost:8080/geoserver/wms',
        params: { 'LAYERS': 'earth:countries' },
        serverType: 'geoserver'
    })
});

var map = new ol.Map({
    target: 'map',
    layers: [
        new ol.layer.Tile({ source: new ol.source.OSM() }),
        capaPaises
    ],
    view: Mivista
});
```

**Ejercicio n°4 — Filtros CQL (`ol_map4.js`)**
- Se filtran los objetos mostrados por la capa WMS añadiendo el parámetro `CQL_FILTER` (equivalente al `cql_filter` usado en peticiones WMS/WFS directas) dentro de `params`:
```javascript
var capaPaisesFiltrada = new ol.layer.Image({
    source: new ol.source.ImageWMS({
        url: 'http://localhost:8080/geoserver/wms',
        params: {
            'LAYERS': 'earth:countries',
            'CQL_FILTER': "pop_est > 50000000"
        },
        serverType: 'geoserver'
    })
});
```

**Ejercicio n°5 — Capas WMS teseladas (`ol_map5.js`)**
- Se sustituye la capa de imagen por una capa **`ol.layer.Tile`** con **`ol.source.TileWMS`**, comparando el comportamiento (peticiones más pequeñas y cacheables por tesela) frente al `ImageWMS` del ejercicio 3. Se practica con la capa PNOA del IGN como ejemplo adicional:
```javascript
var capaPNOA = new ol.layer.Tile({
    source: new ol.source.TileWMS({
        url: 'http://www.ign.es/wms-inspire/pnoa-ma',
        params: { 'LAYERS': 'OI.OrthoimageCoverage' }
    })
});
```

**Ejercicio n°6 — Capas base alternativas: OSM, Bing Maps, OpenTopoMap (`ol_map6.js`)**
- Se añaden varias capas base intercambiables (todas de tipo `ol.layer.Tile`), cada una con su fuente correspondiente: `ol.source.OSM`, `ol.source.BingMaps` (requiere clave de API) y `ol.source.XYZ` apuntando a las teselas de **OpenTopoMap** (`https://{a-c}.tile.opentopomap.org/{z}/{x}/{y}.png`).

**Ejercicio n°7 — Capas vectoriales WFS (`ol_map7.js`)**
- Se añade una capa `ol.layer.Vector` cuya fuente (`ol.source.Vector`) apunta a una petición **WFS** de GeoServer en formato GeoJSON, usando `ol.format.GeoJSON` como formato de lectura:
```javascript
var capaWFS = new ol.layer.Vector({
    source: new ol.source.Vector({
        url: 'http://localhost:8080/geoserver/wfs?service=WFS&version=2.0.0&request=GetFeature&typeName=earth:countries&outputFormat=application/json',
        format: new ol.format.GeoJSON()
    })
});
```

**Ejercicio n°8 — Teselas vectoriales / MVT vía GeoWebCache (`ol_map8.js` / `.html`)**
- Se sustituye la capa vectorial por una capa **`ol.layer.VectorTile`** que consume las teselas vectoriales MVT publicadas por GeoWebCache (configuradas en la Unidad 4), practicando el patrón de URL con plantillas `{z}/{x}/{-y}` visto en la teoría.

**Ejercicio n°9 — Datos GeoJSON estáticos como módulo JS y Heatmap (`ol_map9.js`, `cities.js`)**
- Se exporta un archivo GeoJSON de ciudades como módulo JavaScript, siguiendo el mismo patrón usado en Leaflet (`Unidad 5-1`): se cambia la extensión a `.js` y se antepone `export const cities = ` (o `var cities =`, según el modo CDN/npm) al contenido GeoJSON.
- Se crea una capa **`ol.layer.Heatmap`** a partir de esos datos, configurando `weight` con el atributo de población (`pop_max`), y ajustando `radius` y `blur` para el efecto visual del mapa de calor.

**Ejercicio n°10 — Simbología de capas vectoriales: Fill, Stroke, Circle (`ol_map10.js`)**
- Se aplica un estilo estático a la capa `countries` (o `cities`) mediante `ol.style.Style`, combinando `ol.style.Fill` (color de relleno), `ol.style.Stroke` (color/grosor de borde) y, para capas de puntos, `ol.style.Circle`:
```javascript
var estiloPaises = new ol.style.Style({
    fill: new ol.style.Fill({ color: 'rgba(255, 200, 0, 0.4)' }),
    stroke: new ol.style.Stroke({ color: '#663300', width: 1 })
});
capaWFS.setStyle(estiloPaises);
```

**Ejercicio n°11 — Etiquetas de texto mediante función de estilo y `declutter` (`ol_map11.js`)**
- Se añade una **función de estilo** que, para cada `feature`, añade un `ol.style.Text` con el nombre del país/ciudad (`feature.get('name')`) junto al estilo base de relleno/borde.
- Se activa la propiedad **`declutter: true`** en la capa vectorial (o en el propio mapa, según versión) para evitar la superposición/colisión de etiquetas cuando hay muchos objetos próximos entre sí, ocultando automáticamente las etiquetas que no caben sin solaparse.

**Ejercicio n°12 — Estilos condicionados por atributos (`ol_map12.js`)**
- Se amplía la función de estilo del ejercicio anterior para que el color de relleno (o el tamaño del símbolo) varíe **según el valor de un atributo** del feature (por ejemplo, distintos colores de país según su población, replicando en cliente la lógica de los filtros CQL vistos en GeoServer/CSS en la Unidad 3-1), mediante condicionales dentro de la propia función de estilo.

**Ejercicio n°13 — Controles del mapa (`ol_map13.js`)**
- Se personaliza la lista de controles del mapa con el patrón `ol.control.defaults().extend([...])`, añadiendo: `ol.control.FullScreen`, `ol.control.OverviewMap`, `ol.control.ZoomSlider`, `ol.control.MousePosition` (formateando las coordenadas mostradas) y `ol.control.ScaleLine`.
- Se practica la personalización visual de los controles mediante CSS, sobrescribiendo las clases por defecto (ej. `.ol-zoom`, `.ol-scale-line`, `.ol-mouse-position`).

**Ejercicio n°14 — Selector de capas con el plugin `ol-layerswitcher` (`ol_map14.js`)**
- Se incorpora el plugin de terceros **`ol-layerswitcher`** (de Matt Walker), que añade un control de tipo árbol de capas para activar/desactivar visibilidad, similar al `L.control.layers` de Leaflet pero con soporte de agrupación jerárquica.
- Requiere agrupar las capas base y superpuestas mediante **`ol.layer.Group`** (o `ol/layer/Group` en npm), asignando la propiedad `title` a cada capa/grupo (usada por el plugin como etiqueta) y `type: 'base'` para las capas base (mutuamente excluyentes):
```javascript
var capasBase = new ol.layer.Group({
    title: 'Mapas base',
    layers: [
        new ol.layer.Tile({ title: 'OSM', type: 'base', visible: true, source: new ol.source.OSM() }),
        new ol.layer.Tile({ title: 'OpenTopoMap', type: 'base', visible: false, source: new ol.source.XYZ({ url: 'https://{a-c}.tile.opentopomap.org/{z}/{x}/{y}.png' }) })
    ]
});

var capasDatos = new ol.layer.Group({
    title: 'Capas de datos',
    layers: [ capaWFS, capaCalor ]
});

var map = new ol.Map({
    target: 'map',
    layers: [ capasBase, capasDatos ],
    view: Mivista
});

var layerSwitcher = new ol.control.LayerSwitcher();
map.addControl(layerSwitcher);
```

**Ejercicio n°15 — Interacción de selección (`ol_map15.js`)**
- Se añade la interacción **`ol.interaction.Select`**, definiendo un `style` propio para resaltar el objeto seleccionado y restringiendo la selección a una o varias capas concretas mediante la propiedad `layers`:
```javascript
var seleccion = new ol.interaction.Select({
    style: new ol.style.Style({
        stroke: new ol.style.Stroke({ color: '#ff0000', width: 3 }),
        fill: new ol.style.Fill({ color: 'rgba(255,0,0,0.3)' })
    }),
    layers: [capaWFS]
});
map.addInteraction(seleccion);
```

**Ejercicio n°16 — Interacción de dibujo (`ol_map16.js`)**
- Se añade la interacción **`ol.interaction.Draw`** sobre una fuente vectorial vacía, permitiendo al usuario dibujar nuevas geometrías (puntos, líneas o polígonos, según la propiedad `type`) directamente sobre el mapa:
```javascript
var fuenteDibujo = new ol.source.Vector();
var capaDibujo = new ol.layer.Vector({ source: fuenteDibujo });
map.addLayer(capaDibujo);

var dibujar = new ol.interaction.Draw({
    source: fuenteDibujo,
    type: 'Polygon'
});
map.addInteraction(dibujar);
```
- Como ampliación opcional se sugiere combinar `Draw` con `ol.interaction.Modify` (apoyada en `ol.interaction.Select`) para permitir editar las geometrías recién dibujadas.
