# Unidad 6. OpenLayers

### Resumen estructurado

**1. ¿Qué es OpenLayers?**
- **OpenLayers** es una librería JavaScript *open source* de alto nivel para la creación de mapas interactivos y aplicaciones webmapping, orientada a la programación orientada a objetos y a la máxima flexibilidad/personalización.
- A diferencia de Leaflet (pensada para la sencillez), OpenLayers ofrece muchas más clases, opciones y capacidades avanzadas (proyecciones, formatos, tipos de capas y fuentes), a costa de una curva de aprendizaje algo mayor.

*Historia de OpenLayers (hitos principales):*

| Año | Hito |
|---|---|
| **2006** | Nace el proyecto OpenLayers, impulsado originalmente por MetaCarta. |
| **2007** | Se convierte en proyecto de la **OSGeo** (Open Source Geospatial Foundation). |
| **2010–2013** | Consolidación de OpenLayers 2.x como una de las librerías de referencia del webmapping open source. |
| **2016** | Lanzamiento de **OpenLayers 3/4**, reescritura completa orientada a módulos, mejor rendimiento y soporte moderno de proyecciones y formatos. |
| **2018** | Se unifica la numeración como **OpenLayers 5**, con soporte de instalación vía npm y empaquetado con bundlers modernos (Webpack, Rollup, Vite). |
| **2020–2025** | Versiones 6.x a 9.x/10.x: mejoras continuas de rendimiento (WebGL), nuevas clases de capas (VectorTile, Heatmap), mejor integración con Node.js/npm y con frameworks modernos. |

*Versiones destacadas:*

| Versión | Aspecto clave |
|---|---|
| OpenLayers 2 | Basada en un único archivo `OpenLayers.js` monolítico; API orientada a objetos "clásica" |
| OpenLayers 3–4 | Reescritura modular en ES6, mejor rendimiento de renderizado |
| OpenLayers 5+ | Instalación y empaquetado moderno vía `npm`, soporte de *tree-shaking* (solo se incluye el código realmente usado) |

**Capacidades principales de OpenLayers:**
- Visualización de capas raster (teseladas y de imagen) y vectoriales.
- Soporte nativo de los principales estándares OGC como fuentes de datos: WMS, WMTS, WFS.
- Amplio soporte de formatos vectoriales: GeoJSON, KML, GML, MVT (teselas vectoriales), TopoJSON, entre otros.
- Reproyección de datos entre sistemas de referencia (vía `ol/proj`, apoyada en Proj4js para proyecciones no incluidas por defecto).
- Motores de renderizado intercambiables: DOM, Canvas y WebGL.
- Sistema de estilos altamente configurable, incluyendo funciones de estilo dinámicas.
- Controles e interacciones de usuario extensibles y personalizables.

*Documentación y enlaces de interés:*
- Sitio oficial: https://openlayers.org/
- Documentación de la API: https://openlayers.org/en/latest/apidoc/
- Ejemplos oficiales: https://openlayers.org/en/latest/examples/
- Repositorio: https://github.com/openlayers/openlayers

**2. Programación orientada a objetos (POO) en OpenLayers**
- OpenLayers está construido siguiendo el paradigma de la **programación orientada a objetos (POO)**: define **clases** (plantillas que describen propiedades y métodos comunes) de las que se crean **instancias** (objetos concretos, cada uno con sus propios valores).
- *Analogía del curso:* la clase `ol.View` (o `View` en la sintaxis de módulos) define qué propiedades tiene una "vista" de mapa (centro, zoom, proyección...) y qué métodos permite ejecutar (`setCenter()`, `getZoom()`...); cada vez que se escribe `new ol.View({...})` (o `new View({...})`) se crea una **instancia** concreta de esa clase, con sus propios valores de centro y zoom.
- Del mismo modo, `ol.Map`, `ol.layer.Tile`, `ol.source.OSM`, `ol.style.Style`, etc., son todas clases; los objetos concretos que se crean a partir de ellas (`new ol.Map({...})`, etc.) son sus instancias, y se combinan entre sí para construir la aplicación de mapas.

**3. Carga de la librería: CDN vs npm**
OpenLayers puede utilizarse de dos formas principales:

| Modo | Descripción |
|---|---|
| **CDN / descarga directa** | Se enlaza `ol.js` y `ol.css` en la cabecera del HTML (o se descargan localmente); se accede a todas las clases bajo el espacio de nombres global **`ol.*`** (ej. `ol.Map`, `ol.layer.Tile`). Es la forma más sencilla para empezar, sin necesidad de herramientas de compilación. |
| **npm (módulos ES6)** | Se instala OpenLayers como dependencia de un proyecto Node.js (`npm install ol`) y se importan solo las clases necesarias mediante `import {Map, View} from 'ol';`, `import TileLayer from 'ol/layer/Tile';`, etc. Requiere un *bundler* (Vite, Webpack) para compilar la aplicación, pero permite *tree-shaking* (el resultado final solo incluye el código de las clases realmente usadas, reduciendo el tamaño de la aplicación) y una arquitectura de proyecto más profesional/escalable. |

*Ejemplo CDN:*
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@latest/ol.css">
<script src="https://cdn.jsdelivr.net/npm/ol@latest/dist/ol.js"></script>
```

*Ejemplo módulos (npm):*
```javascript
import { Map, View } from 'ol';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
```

**4. El mapa — ol.Map**
- **`ol.Map`** (o la clase `Map` en la sintaxis de módulos) es el objeto central de una aplicación OpenLayers: representa el mapa en sí y agrupa el resto de componentes (capas, vista, controles, interacciones).

*Propiedades principales del constructor:*

| Propiedad | Descripción |
|---|---|
| `target` | Identificador (`id`) del elemento `<div>` del DOM donde se renderiza el mapa |
| `layers` | Array de capas (`ol.layer.*`) que se muestran en el mapa, ordenadas de fondo a primer plano |
| `view` | Instancia de `ol.View` que define centro, zoom y proyección |
| `controls` | Array de controles de interfaz asociados al mapa |
| `interactions` | Array de interacciones de usuario asociadas al mapa |

*Código básico de un mapa OpenLayers:*
```javascript
var map = new ol.Map({
    target: 'map',
    layers: [
        new ol.layer.Tile({
            source: new ol.source.OSM()
        })
    ],
    view: new ol.View({
        center: ol.proj.fromLonLat([-4.72, 41.66]),
        zoom: 15
    })
});
```

*Algunos métodos de `ol.Map`:* `getView()` / `setView()`, `getLayers()`, `addLayer()` / `removeLayer()`, `getTarget()` / `setTarget()`, `addControl()` / `removeControl()`, `addInteraction()` / `removeInteraction()`, `forEachFeatureAtPixel()`, `getFeaturesAtPixel()`, `updateSize()`.

**5. Motores de renderizado**
OpenLayers puede dibujar el mapa mediante distintos **motores de renderizado** (*renderers*), configurables (avanzado) mediante la propiedad `renderer` del mapa:

| Motor | Descripción |
|---|---|
| **Canvas** | Motor por defecto; dibuja todo el contenido (capas raster y vectoriales) sobre uno o varios elementos `<canvas>` del DOM. Buen equilibrio entre rendimiento y compatibilidad. |
| **DOM** | Cada tesela o elemento se representa como un elemento HTML independiente. Más lento con grandes volúmenes de datos, heredado de versiones antiguas. |
| **WebGL** | Aprovecha la GPU para renderizar grandes volúmenes de datos vectoriales o teselas con alto rendimiento (ej. capas de puntos masivas). |

- El orden de preferencia por defecto que usa OpenLayers para elegir el motor disponible es: `['canvas', 'dom', 'webgl']`.

**6. La vista — ol.View**
- **`ol.View`** define el estado de visualización del mapa: centro, nivel de zoom, rotación y proyección. Es un objeto independiente del mapa, lo que permite reutilizar o compartir vistas entre varios mapas, o guardarla como variable para manipularla directamente.

*Propiedades principales:*

| Propiedad | Descripción |
|---|---|
| `center` | Coordenadas del centro del mapa, en las unidades de la proyección indicada |
| `zoom` | Nivel de zoom inicial |
| `projection` | Sistema de referencia de coordenadas de la vista (por defecto `EPSG:3857`, Web Mercator) |
| `minZoom` / `maxZoom` | Límites del nivel de zoom |
| `maxResolution` | Resolución máxima (en unidades de mapa por píxel) permitida; alternativa a fijar el zoom máximo |
| `zoomFactor` | Factor multiplicador de resolución entre niveles de zoom consecutivos (por defecto 2) |
| `rotation` | Rotación inicial de la vista, en radianes |

*Ejemplo — vista como variable independiente (patrón usado en los ejercicios del curso):*
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
Mivista.setRotation(Math.PI / 4);
```

*Algunos métodos de `ol.View`:* `getCenter()` / `setCenter()`, `getZoom()` / `setZoom()`, `getRotation()` / `setRotation()`, `getProjection()`, `fit()` (encuadra la vista a una extensión o geometría), `animate()`.

**7. Concepto capa / fuente (layer / source)**
- En OpenLayers, una **capa** (`ol.layer.*`) es responsable de **cómo se representa** un dato en el mapa (estilo, opacidad, orden), mientras que una **fuente** (`ol.source.*`) es responsable de **de dónde procede y cómo se obtiene** el dato (URL de un servicio, archivo local, formato...).
- Toda capa necesita asociarse a una fuente mediante la propiedad `source`. Esta separación permite, por ejemplo, cambiar la fuente de datos de una capa sin tener que recrear la capa completa.

**8. ol.layer.Tile — capas de teselas raster**
- **`ol.layer.Tile`** muestra datos raster organizados en teselas (tiles), cargadas y combinadas progresivamente según el nivel de zoom y el área visible.

*Fuentes habituales usadas con `ol.layer.Tile`:*
- **`ol.source.OSM`**: capa base de OpenStreetMap, sin necesidad de configuración adicional.
- **`ol.source.TileWMS`**: consume un servicio WMS de forma teselada (peticiones `GetMap` recortadas en teselas), mejorando el rendimiento en el cliente frente a una única imagen WMS.
- **`ol.source.BingMaps`**: consume las capas base de Bing Maps (requiere una clave de API).

*Ejemplo — capa Tile con TileWMS (GeoServer):*
```javascript
var capaWMS = new ol.layer.Tile({
    source: new ol.source.TileWMS({
        url: 'http://localhost:8080/geoserver/wms',
        params: { 'LAYERS': 'earth:countries', 'TILED': true },
        serverType: 'geoserver'
    })
});
```

*Ejemplo — capa Tile con ImageWMS (equivalente no teselado, ver siguiente punto) o BingMaps:*
```javascript
var capaBing = new ol.layer.Tile({
    source: new ol.source.BingMaps({
        key: 'TU_CLAVE_DE_API',
        imagerySet: 'Aerial'
    })
});
```

**9. ol.layer.Image — capas de imagen**
- **`ol.layer.Image`** muestra una única imagen completa que cubre toda la extensión visible, en lugar de dividirla en teselas. Es útil cuando no interesa (o no es posible) teselar el dato, o cuando el servicio no soporta peticiones WMS teseladas.

*Fuentes habituales:*
- **`ol.source.ImageStatic`**: muestra una imagen estática ya georreferenciada mediante su extensión (bounding box) y proyección.
- **`ol.source.ImageWMS`**: consume un servicio WMS solicitando una única imagen (petición `GetMap` no teselada) que se recalcula al desplazar o hacer zoom en el mapa.

*Ejemplo — ImageWMS:*
```javascript
var capaImagenWMS = new ol.layer.Image({
    source: new ol.source.ImageWMS({
        url: 'http://localhost:8080/geoserver/wms',
        params: { 'LAYERS': 'earth:relieve' },
        serverType: 'geoserver'
    })
});
```

*Ejemplo — ImageStatic:*
```javascript
var capaImagenEstatica = new ol.layer.Image({
    source: new ol.source.ImageStatic({
        url: 'imagenes/mapa_historico.jpg',
        imageExtent: [-4.8, 41.6, -4.6, 41.7],
        projection: 'EPSG:4326'
    })
});
```

**10. ol.layer.Vector — capas vectoriales**
- **`ol.layer.Vector`** muestra objetos geográficos vectoriales (puntos, líneas, polígonos) leídos por su fuente asociada, **`ol.source.Vector`**, y estilizados en el propio cliente (a diferencia de una capa WMS, donde el estilo lo aplica el servidor).
- `ol.source.Vector` puede leer datos desde una URL o desde datos ya cargados en memoria, especificando el **formato** con la propiedad `format` (clases del paquete `ol.format`, ej. `ol.format.GeoJSON`, `ol.format.KML`, `ol.format.GML`, `ol.format.WFS`, `ol.format.MVT`).

*Ejemplo — capa vectorial desde GeoJSON:*
```javascript
var capaVectorial = new ol.layer.Vector({
    source: new ol.source.Vector({
        url: 'datos/countries.geojson',
        format: new ol.format.GeoJSON()
    })
});
```

**11. ol.layer.VectorTile — teselas vectoriales**
- **`ol.layer.VectorTile`** combina las ventajas de las teselas (carga progresiva, buen rendimiento con grandes volúmenes de datos) con las de las capas vectoriales (estilo aplicado en cliente, acceso a atributos). Se usa habitualmente para consumir teselas en formato **MVT** (MapBox Vector Tile) generadas, por ejemplo, por GeoWebCache.

*Ejemplo — VectorTile consumiendo MVT desde GeoWebCache/GeoServer:*
```javascript
var capaVectorTile = new ol.layer.VectorTile({
    source: new ol.source.VectorTile({
        format: new ol.format.MVT(),
        url: 'http://localhost:8080/geoserver/gwc/service/tms/1.0.0/earth:cities@EPSG:900913@pbf/{z}/{x}/{-y}.pbf'
    })
});
```

**12. ol.layer.Heatmap — mapas de calor**
- **`ol.layer.Heatmap`** representa una capa vectorial de puntos como un **mapa de calor** (visualización de densidad), en lugar de mostrar cada punto individualmente.

*Propiedades específicas de estilo del heatmap:*

| Propiedad | Descripción |
|---|---|
| `gradient` | Array de colores CSS que forman la rampa de color del mapa de calor |
| `weight` | Nombre del atributo (o función) que determina el peso/intensidad de cada punto |
| `radius` | Radio (en píxeles) de cada punto en el mapa de calor |
| `blur` | Cantidad de difuminado (blur) aplicado a cada punto |
| `shadow` | Tamaño de la sombra extra alrededor del radio, para suavizar el degradado |

*Ejemplo:*
```javascript
var capaCalor = new ol.layer.Heatmap({
    source: new ol.source.Vector({
        url: 'datos/cities.js',
        format: new ol.format.GeoJSON()
    }),
    gradient: ['#00f', '#0ff', '#0f0', '#ff0', '#f00'],
    weight: 'pop_max',
    radius: 8,
    blur: 15
});
```

**13. El sistema de estilos — ol.style.Style**
- OpenLayers separa completamente la geometría del estilo: una capa vectorial puede tener un estilo estático (el mismo para todos los objetos) o dinámico (calculado por una función).
- **`ol.style.Style`** agrupa varios componentes de estilo, cada uno con su propia clase:

| Componente de estilo | Clase | Se aplica a |
|---|---|---|
| Relleno | `ol.style.Fill` | Interior de polígonos y de marcadores tipo círculo |
| Trazo/borde | `ol.style.Stroke` | Contorno de líneas y de polígonos |
| Símbolo puntual (círculo) | `ol.style.Circle` | Puntos, con `fill` y `stroke` propios |
| Icono | `ol.style.Icon` | Puntos, mediante una imagen externa |
| Texto/etiqueta | `ol.style.Text` | Etiquetas de texto asociadas a cualquier geometría |

*Ejemplo — estilo por defecto para puntos, líneas y polígonos:*
```javascript
var estilo = new ol.style.Style({
    fill: new ol.style.Fill({ color: 'rgba(255,255,255,0.4)' }),
    stroke: new ol.style.Stroke({ color: '#3399CC', width: 1.25 }),
    image: new ol.style.Circle({
        radius: 5,
        fill: new ol.style.Fill({ color: '#3399CC' })
    })
});
```

*Ejemplo — estilo de texto/etiqueta:*
```javascript
var estiloTexto = new ol.style.Style({
    text: new ol.style.Text({
        text: 'Mi etiqueta',
        font: '14px Arial, sans-serif',
        fill: new ol.style.Fill({ color: '#000' }),
        stroke: new ol.style.Stroke({ color: '#fff', width: 3 })
    })
});
```

**14. Funciones de estilo (StyleFunction)**
- En lugar de un estilo fijo, `ol.layer.Vector` (y otras capas de estilo) admiten una **función de estilo** (`StyleFunction`), que recibe cada `feature` (y la resolución actual del mapa) y devuelve el `ol.style.Style` (o array de estilos) a aplicar. Esto permite estilos **condicionados por atributos** o por el **nivel de zoom** (resolución).

*Firma típica de una función de estilo:*
```javascript
function estiloFuncion(feature, resolution) {
    // lógica según feature.get('atributo') o resolution
    return new ol.style.Style({ ... });
}

var capa = new ol.layer.Vector({
    source: miFuente,
    style: estiloFuncion
});
```

**15. Gestión de features (objetos geográficos) en el cliente**
`ol.source.Vector` ofrece métodos para manipular directamente los objetos geográficos (`ol.Feature`) que contiene, sin necesidad de recargar la fuente completa:

| Método | Descripción |
|---|---|
| `addFeature(feature)` | Añade un único objeto geográfico a la fuente |
| `clear()` | Elimina todos los objetos geográficos de la fuente |
| `getFeatures()` | Devuelve un array con todos los objetos geográficos de la fuente |
| `getFeaturesAtCoordinate(coord)` | Devuelve los objetos geográficos que existen en una coordenada concreta |
| `removeFeature(feature)` | Elimina un objeto geográfico concreto de la fuente |
| `getExtent()` | Devuelve la extensión (bounding box) que engloba todos los objetos de la fuente |
| `forEachFeature(callback)` | Ejecuta una función para cada objeto geográfico de la fuente |

**16. Controles — ol.control**
- Los **controles** son elementos de interfaz de usuario (widgets) superpuestos al mapa, con los que el usuario interactúa mediante clic (a diferencia de las interacciones, que normalmente responden a gestos sobre el propio mapa).
- Por defecto, si no se especifica la propiedad `controls` del mapa, OpenLayers añade automáticamente los **controles por defecto**: **`ol.control.Zoom`** (botones de acercar/alejar) y **`ol.control.Attribution`** (cuadro de atribuciones), junto con **`ol.control.Rotate`** (botón para restablecer la rotación, visible solo cuando el mapa está rotado).
- Cada control tiene una clase CSS asociada que permite personalizar su apariencia (ej. `.ol-zoom`, `.ol-attribution`, `.ol-rotate`).
- **Patrón `ol.control.defaults().extend([...])`**: permite partir de los controles por defecto y añadir otros controles adicionales, en lugar de sustituir la lista completa:
```javascript
var map = new ol.Map({
    target: 'map',
    controls: ol.control.defaults().extend([
        new ol.control.FullScreen(),
        new ol.control.ScaleLine()
    ]),
    layers: [ new ol.layer.Tile({ source: new ol.source.OSM() }) ],
    view: new ol.View({ center: [0, 0], zoom: 2 })
});
```

*Otras clases de control disponibles:*

| Control | Descripción |
|---|---|
| `ol.control.FullScreen` | Botón para mostrar el mapa en pantalla completa |
| `ol.control.MousePosition` | Muestra la coordenada del ratón sobre el mapa en tiempo real |
| `ol.control.OverviewMap` | Mapa de situación en miniatura (minimapa) |
| `ol.control.ScaleLine` | Barra de escala gráfica |
| `ol.control.ZoomSlider` | Control deslizante (slider) para el zoom, alternativo a los botones |
| `ol.control.ZoomToExtent` | Botón que restablece la vista a una extensión predefinida |

**17. Interacciones — ol.interaction**
- Las **interacciones** gestionan el comportamiento del mapa en respuesta a los gestos del usuario directamente sobre el lienzo del mapa (arrastrar, rueda del ratón, pellizco en móvil...), a diferencia de los controles, que son botones/widgets de interfaz.
- **`ol.interaction.Interaction`** es la clase base abstracta de la que heredan todas las interacciones.
- Al igual que con los controles, si no se especifica la propiedad `interactions` del mapa, se añaden las **interacciones por defecto**, entre ellas:

| Interacción por defecto | Descripción |
|---|---|
| `DoubleClickZoom` | Acerca el zoom al hacer doble clic |
| `DragPan` | Permite desplazar el mapa arrastrando con el ratón |
| `DragZoom` | Zoom sobre un rectángulo dibujado arrastrando con una tecla modificadora |
| `DragRotate` | Rota el mapa arrastrando con una tecla modificadora |
| `KeyboardPan` / `KeyboardZoom` | Desplazamiento/zoom mediante el teclado |
| `MouseWheelZoom` | Zoom mediante la rueda del ratón |
| `PinchRotate` / `PinchZoom` | Rotación/zoom mediante gestos de pellizco en pantallas táctiles |

*Otras interacciones destacadas (no incluidas por defecto):*

| Interacción | Descripción |
|---|---|
| `ol.interaction.DragBox` | Permite dibujar un rectángulo de selección arrastrando el ratón |
| `ol.interaction.DragRotateAndZoom` | Combina rotación y zoom en un único gesto de arrastre |
| `ol.interaction.DragAndDrop` | Permite cargar archivos (ej. GeoJSON, KML) arrastrándolos sobre el mapa |
| **`ol.interaction.Select`** | Selecciona objetos geográficos al hacer clic (u otro evento) sobre ellos. Propiedades clave: `style` (estilo aplicado a los objetos seleccionados), `layers` (capas sobre las que aplica), `condition` (evento que dispara la selección), `toggleCondition` (evento para alternar selección múltiple), `addCondition` / `removeCondition` (eventos para añadir/quitar de la selección) |
| **`ol.interaction.Draw`** | Permite dibujar nuevas geometrías sobre el mapa. Propiedades clave: `type` (tipo de geometría a dibujar: `'Point'`, `'LineString'`, `'Polygon'`, `'Circle'`...), `source` (fuente vectorial donde se añaden las geometrías dibujadas) |
| **`ol.interaction.Modify`** | Permite modificar (editar vértices de) geometrías existentes. Propiedad clave: `features` (colección de objetos geográficos editables); habitualmente se combina con `ol.interaction.Select`, usando la colección de objetos seleccionados como `features` de `Modify` |

---

## Ejercicios prácticos Unidad 6 — OpenLayers

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

---

