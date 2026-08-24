# Ejercicios — Unidad 3

### Ejercicios prácticos Unidad 3-1 — GeoServer

Guía práctica paso a paso (instalación, configuración y publicación de datos en GeoServer 2.28.0):

**1. Instalación de GeoServer sobre Windows**
- GeoServer requiere un entorno **JDK 17** (no se recomienda usar versiones más recientes). Se instala con el paquete **Adoptium/Eclipse Temurin JDK 17-LTS** (https://adoptium.net/es/), eligiendo el sistema operativo correspondiente.
- Descarga de GeoServer desde http://geoserver.org/download/, eligiendo la versión estable (ej. **GeoServer 2.28.0**) en formato **Platform Independent Binary** — una aplicación web construida sobre **Jetty** (servidor de aplicaciones ligero y portátil), lo que la hace independiente del sistema operativo.
- Se descomprime en el directorio raíz (ej. `C:\Geoserver 2.28.0`), que contiene las carpetas: `bin`, `data_dir`, `etc`, `lib`, `license`, `licenses`, `logs`, `modules`, `resources`, `webapps`.
- **Variables de entorno** a configurar (Panel de control > Sistema > Configuración avanzada del sistema > Variables de entorno > Variables del sistema > Nueva):
  - `JAVA_HOME`: ruta al directorio JDK (ej. `C:\Program Files\Eclipse Adoptium\jdk-17.0.16.8-hotspot`).
  - `GEOSERVER_HOME`: directorio de instalación de GeoServer (ej. `C:\Geoserver 2.28.0`).
  - `GEOSERVER_DATA_DIR`: ubicación del **directorio de datos** de GeoServer si se desea usar una distinta a la predeterminada (ej. `C:\data_dir`).
- **Directorio de datos (`data_dir`)**: es el "corazón" de la configuración y los datos de GeoServer (workspaces, styles, layergroups, gwc, www, logs, etc.). Como el directorio de datos por defecto se crea dentro del propio directorio de instalación, **antes de actualizar o reinstalar GeoServer hay que copiar la carpeta `data_dir` fuera** (ej. a la raíz `C:\`), ya que al desinstalar se elimina todo el directorio de instalación junto con los datos.

| Carpeta/archivo de `data_dir` | Descripción |
|---|---|
| `workspaces/` | Configuración de todos los espacios de trabajo; dentro de cada uno se definen stores, layers, etc. |
| `styles/` | Archivos de estilo SLD (Styled Layer Descriptor) usados para representar visualmente las capas |
| `layergroups/` | Configuración de grupos de capas (layer groups), que permiten combinar varias capas en una sola vista |
| `gwc/` | Almacén de caché de teselas de GeoWebCache, si está activado |
| `www/` | Carpeta para contenido web estático (HTML, imágenes, etc.) servido directamente desde GeoServer |
| `logs/` | Archivos de registro (log) de GeoServer, útiles para depurar errores |

- **Ejecución/parada:** se ejecuta `startup.bat` (dentro de `bin`), dejando la ventana de línea de comandos abierta; para detener, se cierra esa ventana o se ejecuta `shutdown.bat`. La interfaz de administración web queda disponible en `http://localhost:8080/geoserver` (credenciales por defecto: `admin` / `geoserver`).
- **Desinstalar/actualizar:** detener GeoServer, eliminar el directorio de instalación y copiar el nuevo directorio de binarios (conservando aparte la copia de `data_dir`).
- **Cambiar el puerto:** editar el archivo `start.ini` (en el directorio de instalación) y modificar la línea `jetty.http.port=8080` al puerto deseado (ej. `8585`), reiniciando después con `startup.bat`.

**2. Descarga e instalación de extensiones**
GeoServer permite ampliar su funcionalidad con complementos descargados desde https://geoserver.org/release/stable/, cuyos `.jar` se copian en `<GEOSERVER_HOME>\webapps\geoserver\WEB-INF\lib` (requiere reiniciar el equipo para completar la instalación):
- **CSS Styling** (categoría *Cartography*): habilita un editor de estilos alternativo a SLD basado en sintaxis CSS.
- **Vector Tiles** (categoría *Output Formats*): habilita la generación de teselas vectoriales.
- **WPS** (categoría *OGC Services*): habilita el Servicio de Procesamiento Web (geoprocesamiento).
- Para verificar que las extensiones se instalaron correctamente: en el apartado **Demos** debe aparecer el enlace *Generador de consultas WPS*; al crear un nuevo estilo debe poder elegirse el formato **CSS**; y en **Cacheado de Teselas** de una capa deben aparecer los formatos `application/json;type=geojson`, `application/json;type=topojson` y `application/vnd.mapbox-vector-tile`.

**3. El directorio `www` como servidor web**
- La carpeta `www` dentro de `data_dir` sirve contenido estático (HTML, imágenes, CSS, JavaScript) directamente desde el servidor Jetty embebido de GeoServer, permitiendo alojar visores webmapping propios (se accede en `http://<host>:<puerto>/geoserver/www`).
- En este directorio se guardarán los archivos HTML creados durante el curso (ej. `web.html`, `ol-demo.html`, `wfs-t.html`).

**4. Interfaz de administración web de GeoServer**
- Página de bienvenida (`http://localhost:8080/geoserver`): resume los servicios publicados (WMS, WMTS, WFS, WCS, WPS) y sus versiones.
- Secciones de la columna izquierda: **Servidor**, **Datos**, **Servicios**, *Settings*, **Cacheado de Teselas**, **Seguridad**, **Demos**, **Herramientas**.
- **Servidor > Estado del servidor:** herramientas de diagnóstico/configuración (directorio de datos, memoria, versión JVM, tipografías disponibles, etc.).
- **Política de Seguridad de Contenido (CSP):** en `Seguridad > Content Security Policy` conviene comprobar que la opción "Enable Content-Security-Policy header" esté **deshabilitada** durante el desarrollo del curso, ya que de estar activa bloquea el acceso a recursos externos (como Leaflet u OpenStreetMap) referenciados por URL sin descargar.
- **Servicios:** páginas de configuración avanzada de WCS, WFS, WMS y WPS (metadatos, niveles de servicio, salidas GML, opciones raster/SVG).
- **Datos > Previsualización de capas** (*Layer Preview*): vistas previas de cada capa en varios formatos de salida (OpenLayers, KML, GML), útil para verificar visualmente la configuración.

**5. Crear un espacio de trabajo (workspace)**
Un *workspace* consiste en un **nombre** (máx. 10 caracteres, sin espacios) y un **URI del espacio de nombres** (identificador único, no necesita apuntar a una ubicación real). Ejemplo del curso: `Datos > Espacios de trabajo > Agregar un nuevo espacio de trabajo`, con Name: `earth`, URI: `http://geoserver.org/earth`, marcado como espacio de trabajo por defecto.

**6. Añadir un almacén de datos (store) y publicar una capa raster (GeoTIFF)**
1. `Datos > Almacenes de datos > Agregar nuevo almacén` → en *Orígenes de datos raster* seleccionar **GeoTIFF**.
2. Rellenar: Espacio de trabajo `earth`, Nombre del origen de datos `relieve`, Descripción `Relieve y sombreado del mundo`, Habilitado, y en Parámetros de conexión > URL la ruta al archivo (`file:C:\webmapping\Capas\relieve.tif`).
3. Al guardar, se muestra la lista de capas del almacén (una única capa por ser GeoTIFF) → clic en **Publicación**.
4. En *Editar capa > Información básica del recurso*, cambiar nombre/título a `relieve`.
5. En *Sistema de referencia de coordenadas*: ajustar el **SRS declarado** a `EPSG:4326`, la **Gestión de SRS** a *Forzar el declarado*, y en *Encuadres* usar los enlaces **Calcular desde los datos** y **Calcular desde el enlace nativo**.
6. Guardar. La capa `earth:relieve` queda publicada y visible en *Previsualización de capas* (OpenLayers, con valores RGB al hacer clic en el mapa).

**7. Importar una base de datos PostGIS completa**
GeoServer incluye una **herramienta de importación** que permite cargar varias tablas/capas de una base de datos PostGIS a la vez (en vez de repetir el flujo tabla a tabla):
1. `Datos > Almacenes de datos > Agregar nuevo almacén` → en *Orígenes de datos vectoriales* elegir **PostGIS**.
2. Parámetros de conexión de ejemplo (base de datos `world` del curso): Espacio de trabajo `earth`, Nombre del origen de datos `world`, Host `localhost`, Port `5432`, Database `world`, Schema `public`, Username `postgres`, Password `postgres`.
3. Al guardar, se listan todos los recursos disponibles en el almacén (`buffer`, `centroides`, `cities`, `countries`, `lugares`, `rivers`) con la acción **Publicación** para cada uno.
4. Para cada capa a publicar: clic en Publicación → en *Encuadres* usar **Calcular desde los datos** y **Calcular desde el encuadre nativo** → Guardar.
5. Las siguientes capas (a partir de la segunda) se agregan desde `Datos > Capas > Agregar nueva capa`, eligiendo el almacén `earth:world` en el desplegable.
6. Resultado del ejercicio: 4 capas publicadas — `earth:cities`, `earth:countries`, `earth:lugares`, `earth:rivers` — todas con SRS nativo `EPSG:4326`.

**8. Protocolos OGC servidos por GeoServer — peticiones de ejemplo**

*WMS — petición GetMap:*
```
http://localhost:8080/geoserver/wms?
SERVICE=WMS&
VERSION=1.3.0&
REQUEST=GetMap&
BBOX=-180,-90,180,90&
WIDTH=1000&
HEIGHT=500&
LAYERS=cities&
&FORMAT=image/png
```
(Se escribe sin espacios tras cada `&`. Devuelve una imagen con la capa de ciudades.)

*WFS — petición GetFeature (una entidad concreta, por `FEATUREID`):*
```
http://localhost:8080/geoserver/wfs?
SERVICE=wfs&
VERSION=1.1.0&
REQUEST=GetFeature&
TYPENAME=earth:countries&
FEATUREID=countries.34
```

*WFS — descarga de geometrías en formato shape-zip:*
```
http://localhost:8080/geoserver/earth/wfs?
service=wfs&
version=2.0.0&
request=getfeature&
typeName=earth:cities&
outputFormat=shape-zip
```

*WFS — petición GetCapabilities:*
```
http://localhost:8080/geoserver/earth/wfs?
service=wfs&
request=getcapabilities
```

- **Visualización en un cliente SIG (QGIS):** las capas `cities` y `countries` se cargan como WMS con la URL `http://localhost:8080/geoserver/wms?`; la capa `cities` se carga como WFS con `http://localhost:8080/geoserver/wfs?`; y la capa `relieve` como WCS con `http://localhost:8080/geoserver/wcs?` (comprobando antes que la capa esté marcada como *Habilitado* y *Anunciado*). Si el WCS no se muestra, puede solicitarse una petición `DescribeCoverage` directamente desde el navegador.

**9. Servicio de Procesamiento Web (WPS) — generador de consultas paso a paso**
- Desde `Demos > Generador de consultas WPS` se accede a un formulario que permite ejecutar cualquiera de los procesos disponibles (categorías: vector, ráster, geometría).
- Ejemplo del curso — geoproceso **`vec:Centroid`** (calcula el centroide geométrico de los elementos de una capa):
  - **Entrada del proceso** (`features`, tipo `VECTOR_LAYER`): capa `earth:countries`.
  - **Salida del proceso**: formato `application/zip` (descarga un ZIP con la nueva capa de puntos).
  - Si el servicio está restringido hay que indicar en *Identificación* el usuario/contraseña con permisos de geoprocesamiento (ej. `admin`).
  - Al pulsar **Ejecute el proceso** se descarga un ZIP con la capa de centroides resultante.

**10. Otros formatos de datos soportados**

| Orígenes de datos vectoriales | Orígenes de datos raster | Otros orígenes |
|---|---|---|
| CSV, Directory of spatial files (shapefiles), GeoPackage, PostGIS, PostGIS (JNDI), Properties, Shapefile, Web Feature Server (NG) | ArcGrid, GeoPackage (mosaic), GeoTIFF, ImageMosaic, WorldImage | WMS (en cascada), WMTS |

- **WMS en cascada:** permite servir desde el propio GeoServer un WMS externo, gestionándolo como si fuera local, aunque con la limitación de que no permite modificar su estilo.
- *Ejemplo práctico del curso — carga de un GeoPackage:* se crea un nuevo espacio de trabajo `hotdogs_proyect` (URI `http://geoserver.org/hotdogs_proyect`); se añade un almacén tipo **GeoPackage** con Nombre del origen de datos `hotdogs` y ruta `file://C:\webmapping\Capas\hotdogs.gpkg`; se publica la capa `hotdogs` calculando los encuadres.

**11. Creación de un grupo de capas (layer group)**
Un grupo de capas es un contenedor que organiza varias capas (y otros grupos) en una estructura jerárquica, referenciable por un solo nombre en peticiones WMS, permitiendo combinar datos de distinta geometría en una única capa "virtual".
- Ejemplo del curso — grupo `worldgroup` (sin espacio de trabajo asignado), añadiendo en este orden de dibujo: `earth:relieve`, `earth:countries`, `earth:cities`, `earth:rivers` (**el orden importa**: la capa superior de la lista se dibuja primero, la última se dibuja encima). Se marca *Estilo por defecto* para las cuatro capas y se pulsa **Generar límites** (usa `EPSG:4326` si no se detecta automáticamente) antes de Guardar.

**12. Estilos en GeoServer (SLD)**
- Cada capa debe tener asociado al menos un estilo (GeoServer aplica uno por defecto a cada capa nueva). GeoServer usa el lenguaje **SLD** (*Styled Layer Descriptor*), estándar XML de la OGC (documentación: https://docs.geoserver.org/latest/en/user/styling/sld/cookbook/index.html — *SLD Cookbook*, colección de recetas de estilo).
- **Estructura jerárquica de un SLD:** `Header` → `FeatureTypeStyle` (conjunto de reglas; el orden de los `FeatureTypeStyle` determina el orden de representación) → `Rule` (directiva de estilo, puede tener un filtro asociado según atributos o escala) → `Symbolizer` (instrucción de estilo concreta; hay 5 tipos: **PointSymbolizer, LineSymbolizer, PolygonSymbolizer, RasterSymbolizer, TextSymbolizer**).
- **Cargar un SLD desde archivo:** en `Datos > Estilos`, abrir el estilo a modificar (ej. `point`), pulsar **Seleccionar archivo** para elegir un `.sld` local (ej. `earth_cities.sld`) y luego **Cargar…**, confirmando sobrescribir; el contenido del editor se sustituye por el del archivo cargado. Tras **Validar, Guardar y Aplicar**, la definición se guarda en `C:\data_dir\styles`.

**13. Estilos CSS en GeoServer**
- La extensión **CSS Styling** añade un editor de estilos alternativo que usa una sintaxis derivada de CSS (basada en SVG); los estilos CSS se convierten internamente a SLD. Permite escribir en muchas menos líneas lo mismo que un SLD equivalente (ej. un estilo de puntos que en SLD ocupa 25+ líneas se reduce a menos de 10 en CSS).
- **Crear un estilo CSS:** `Datos > Estilos > Agregar un nuevo estilo` → asignar Nombre (ej. `lugares_css`), Espacio de trabajo (ej. `earth`) y Formato `CSS` → en *Generar un estilo por defecto* elegir `Point` y **Generar…**, lo que crea una plantilla base:
```css
/* @title violet point */
* {
    mark: symbol(square);
    mark-size: 6px;
    :mark {
        fill: #3300ff;
    }
}
```
- **Sintaxis CSS:** `selector { propiedad: valor; }`. El selector `*` indica que todos los datos usan esas propiedades. Las propiedades van entre llaves y se separan mediante `:` (nombre/valor).
- **Símbolos:** la función `symbol()` permite usar marcas predefinidas sin editor de imágenes: `circle`, `square`, `triangle`, `arrow`, `cross`, `star`…
- **Selectores de símbolos** (pseudoclases, ej. `:mark`): permiten definir propiedades adicionales de una marca ya definida:
```css
* {
  mark: symbol(square);
  mark-size: 6px;
}
:mark {
  fill: red;
}
```
- Tras crear el estilo, en la pestaña **Publishing** se asocia a una o varias capas (marcando *Default* o *Associated* según el caso), y en **Layer Preview**/**Layer Attributes** se puede previsualizar el resultado y consultar los campos de la capa.

**14. Filtros en GeoServer (CQL)**
Ejemplo del curso — estilo `cities_filter` con tres clases según población (atributo `pop_max`), usando **CQL** (*Common Query Language*) para expresar los filtros entre corchetes:
```css
* {
  mark: symbol(circle);
}
:mark {
  fill: #0033CC;
}

/* @title Small cities */
[pop_max < 1000000] {
  mark-size: 6;
}

/* @title Medium cities */
[pop_max >= 1000000] [pop_max < 10000000] {
  mark-size: 10;
}

/* @title Large cities */
[pop_max >= 10000000] {
  mark-size: 14;
}
```
- **Proporcionando metadatos:** los comentarios `/* @title ... */` (y `@abstract`) antes de cada regla generan automáticamente las imágenes de leyenda del estilo (ej. leyenda con "Small cities", "Medium cities", "Large cities").
- Tras **Validar** y **Enviar** (Submit), el estilo se aplica a la capa `cities` como *Estilo por defecto* desde `Datos > Capas > cities > Publicación`.

**15. Estilos basados en escalas**
Se usa el operador **`@scale`** para modificar el estilo según el nivel de zoom:
```css
* {
  fill: none;
}
[@scale < 1000000] {
  stroke-width: 6;
  label: [feature_na];
}
[@scale > 1000000] [@scale < 2000000] {
  stroke-width: 4;
}
[@scale > 2000000] {
  stroke-width: 2;
}
```
El **CSS Cookbook** incluye ejemplos equivalentes para puntos, líneas y polígonos, incluyendo etiquetado (`label`) y marcadores personalizados (ej. triángulo).

**16. Teselas vectoriales (Vector Tiles) y GeoWebCache**
- Una **tesela vectorial** contiene datos vectoriales georreferenciados recortados en teselas, a diferencia de las teselas de imagen (que son ráster). Es un **estándar abierto** (licencia *Creative Commons Attribution 3.0 US*).

| | WFS | Teselas vectoriales |
|---|---|---|
| Contenido | Datos subyacentes sin modificar (más detalle) | Objetos geográficos ya modificados/listos para representarse |
| Renderizado del estilo | — | En el navegador del cliente (ej. OpenLayers), no en el servidor |

- **Ventajas** de las teselas vectoriales frente a las de imagen: los estilos se renderizan en el cliente (varios mapas desde una única fuente de datos, sin volver a pedir al servidor); menor tamaño de transferencia; GeoWebCache solo necesita almacenar una tesela una vez para todos los estilos diferentes; permiten mapas de alta resolución sin más ancho de banda; el cliente tiene acceso nativo a atributos y geometría.
- **Desventajas:** las teselas de imagen son más fáciles de consumir; los datos vectoriales requieren pre-procesado para poder personalizar la simbología en cliente.
- Por el momento, **las teselas vectoriales son un formato de salida en GeoServer, no una fuente de datos**.
- **Formatos soportados por GeoServer** (los tres, mediante GeoWebCache):

| Formato | MIME type | Notas |
|---|---|---|
| **MapBox Vector (MVT)** | `application/vnd.mapbox-vector-tile` | Formato binario, el más recomendado en producción; ampliamente soportado |
| **GeoJSON** | `application/json;type=geojson` | Legible por humanos; pocas aplicaciones de Vector Tiles lo admiten (sí OpenLayers) |
| **TopoJSON** | `application/json;type=topojson` | Complejo, admite topología (bueno para polígonos); poco soportado (sí OpenLayers) |

- **Publicar teselas vectoriales con GeoWebCache:** `Datos > Capas > <capa> > pestaña Cacheado de Teselas` → sección *Cache image formats* → marcar la casilla del formato deseado (ej. `application/vnd.mapbox-vector-tile`) → Guardar.

### Ejercicios prácticos Unidad 3 — Conexiones a servicios OGC en QGIS

Guía práctica paso a paso para conectar QGIS a los principales servicios OGC (WMS, WFS, OGC API, WCS):

**1. Conexiones Web Map Service (WMS)**
- WMS es un **servicio** (no una página web), por lo que requiere un software SIG para visualizarlo. Define tres operaciones: **GetCapabilities** (metadatos del servicio), **GetMap** (devuelve un mapa con parámetros geográficos/dimensionales definidos) y **GetFeatureInfo** (información de características particulares mostradas en el mapa).
- *Flujo en QGIS:* `Capa/Añadir Capa WMS/WMTS` (o el botón correspondiente de la barra de herramientas) → **Nuevo** para crear una conexión → indicar **Nombre** y **URL** del servicio.
- *Ejemplo del curso — servicio PNOA del IGN:*
  - Nombre: `PNOA`
  - URL: `http://www.ign.es/wms-inspire/pnoa-ma?`
  - Tras **Conectar**, se listan las capas disponibles (ej. `OI.MosaicElement`, `OI.OrthoimageC…`, `fondo`) para seleccionar y **Añadir** a la Tabla de Contenidos.
- *Nota del curso:* si el servicio WMS no está operativo, se puede recurrir al directorio de servicios de la IDE de España (IDEE): `http://www.idee.es/web/guest/directorio-de-servicios`.

**2. Conexiones Web Feature Service (WFS)**
- Permite acceder a los datos vectoriales (no solo a su imagen). *Flujo en QGIS:* `Capa/Añadir Capa WFS` → **Nuevo** para crear conexión → indicar **Nombre** y **URL**.
- *Ejemplo del curso — Riesgos Naturales en la Junta de Andalucía (REDIAM):*
  - Nombre: `Riesgos Naturales en la Comunidad de Andalucía`
  - URL: `http://www.juntadeandalucia.es/medioambiente/mapwms/REDIAM_WFS_riesgos_naturales?`
  - Tras **Conectar**, se muestra la capa disponible (ej. `zona_pel_incendios` — "Zonas de peligro de incendio en Andalucía"), que se selecciona y se **Añade**.
  - Con la herramienta **Identificar objetos espaciales** se puede consultar la información asociada a cada entidad cargada (ej. atributos `COD_INE`, `MUNICIPIO`, `PROVINCIA`).

**3. Conexiones OGC API**
- **OGC API** es un nuevo estándar (aún en desarrollo) que supone una evolución del WFS: permite acceder a los datos en formato web (HTML y, opcionalmente, JSON), siguiendo un enfoque moderno de arquitectura web (mejores prácticas W3C/OGC) mediante **"puntos finales"** (*endpoints*) incorporados a la URL del recurso.
- El punto final genérico de acceso es `/`, conocido como ***Landing page***. Desde ahí se accede a los elementos principales de una OGC API:
  - **Collections** (`/collections`): los datos propiamente dichos.
  - **API definition**: descripción de los métodos y recursos soportados (documentación Swagger UI / ReDoc).
  - **Conformance declaration**: especificaciones que cumplen los enlaces del recurso.
- *Ejemplo del curso — OGC API del Instituto Geográfico Nacional (IGN):* `https://api-features.ign.es/` — colecciones disponibles: Unidades administrativas, Límites administrativos, Nombres geográficos, Red de Estaciones de Referencia GNSS (ERGNSS), Red de Nivelación de Alta Precisión (REDNAP), Red REGENTE, Red de Orden Inferior (ROI). Los datos se pueden consultar desde un mapa o desde una tabla, y pueden consumirse desde GIS de escritorio (QGIS) o librerías JavaScript (Leaflet, OpenLayers).
- **OGC API en QGIS:** se configura en la misma ubicación que las conexiones WFS (`WFS / OGC API - Funcionalidades`) → **Nuevo** → indicar Nombre (ej. `IGN OGC API`) y URL de la *landing page* (`https://api-features.ign.es/`) → **Conectar**, y elegir la colección deseada (ej. *Red de Estaciones de Referencia (ERGNSS)*, más ligera para pruebas) → **Añadir**.

**4. Conexiones Web Coverage Service (WCS)**
- WCS proporciona información **ráster** con su semántica original: no solo la imagen (como WMS), sino también los valores/propiedades del dato (ej. valores de altitud de un MDE). Operaciones: **GetCapabilities**, **DescribeCoverage** (descripción detallada de una o varias coberturas) y **GetCoverage** (obtener una cobertura o parte de ella).
- *Flujo en QGIS:* `Capa/Añadir capa WCS` → **Nuevo** → indicar **Nombre** y **URL**.
- *Ejemplo del curso — Modelos Meteorológicos REDIAM (Junta de Andalucía):*
  - Nombre: `Modelos Meteorológicos REDIAM`
  - URL: `http://www.juntadeandalucia.es/medioambiente/mapwms/REDIAM_WCS_modelos_meteorologicos_prealertas?`
  - Tras **Conectar**, se selecciona la cobertura (`modelos_meteo_prealertas`) y se **Añade**; puede cambiarse el sistema de coordenadas con el botón **Cambiar…**.
  - *Nota del curso:* la ejecución puede ser lenta o bloquear el equipo según el volumen de datos; como alternativa se propone el WCS de Cantabria: `https://geoservicios.cantabria.es/inspire/services/MDT/MapServer/WCSServer`.
