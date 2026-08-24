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

**Ejercicios prácticos de esta unidad:** [ver ejercicios →](../ejercicios/ejercicio-6.md)

---

