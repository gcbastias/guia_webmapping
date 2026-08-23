# Unidad 3-1. Servidores de datos espaciales. GeoServer

### Resumen estructurado

**1. Servidores web — conceptos básicos**
- Modelo **frontend / backend**: el cliente (frontend, estilo CSS + web HTML) envía una **petición** al servidor (backend, datos) vía **HTTP**, y este responde.
- Toda petición web adopta la forma de una **URL** (ej. `https://www.nasa.gov/`). Es posible solicitar por HTTP no solo páginas HTML sino cualquier tipo de archivo (jpg, zip, xml…); el navegador lo muestra si sabe interpretarlo o pide descargarlo.
- Servidores web más populares: **Apache HTTP Server**, **Jetty**, **Internet Information Services (IIS)**.

**2. Servidores de mapas web**
- Un servidor de mapas web es un **subconjunto especializado** del modelo de servidor web: interpreta y responde peticiones igual que un servidor web estándar.
- **Diferencia clave:** la respuesta de un servidor de mapas no es necesariamente un documento/archivo (.html, .zip…), sino **datos geográficos**.
- Esquema: petición → interpretación de la petición → consulta de datos geoespaciales → preparación de la respuesta → respuesta (imagen de mapa u otro dato geográfico).

**3. Servidores de mapas web libres (open source) más populares**

| Servidor | Característica destacada |
|---|---|
| **GeoServer** | Muy utilizado por su excelente integración con PostGIS |
| **MapServer** | Ligero y rápido |
| **Lizmap** | Frontend (interfaz web) para QGIS |
| **MapProxy** | Se integra con GeoServer y MapServer; actúa como proxy para acelerar servicios WMS |
| **QGIS Server** | Complemento/módulo servidor de QGIS |

**4. GeoServer**
- **GeoServer** es un servidor de código abierto escrito en **Java** que permite a los usuarios compartir y editar datos geoespaciales.
- Está empaquetado como un **servlet independiente** para usarse con servidores de aplicaciones como Apache Tomcat o Jetty.
  - *¿Qué es un Servlet?* Módulo escrito en Java que se utiliza en un servidor (sea o no servidor web) para extender sus capacidades de respuesta a los clientes aprovechando las potencialidades de Java.
- Diseñado para la **interoperabilidad**: publica datos de cualquier fuente utilizando **estándares abiertos**.
- Puntos fuertes: proyecto con comunidad muy activa y actualizaciones frecuentes; soporte para multitud de orígenes de datos; interfaz amigable; extensiones al estándar SLD y soporte de estilos CSS.

**5. Fuentes de datos soportadas por GeoServer** (lista no exhaustiva)

| Archivos | Bases de datos |
|---|---|
| Shapefile | PostGIS |
| GeoTIFF | ArcSDE |
| ArcGrid | Oracle Spatial |
| JPEG2000 | DB2 |
| GDAL formats | SQL Server |
| CSV | |
| GeoPackage | |

**6. Protocolos OGC soportados — comparativa GeoServer vs QGIS Server vs ArcGIS Server**

GeoServer implementa los protocolos *open web* del **OGC**; es servidor de alto rendimiento compatible con la certificación **WMS**, y es la **implementación de referencia** de las normas OGC **WFS** y **WCS**.

| Estándar OGC | QGIS Server | GeoServer | ArcGIS Server |
|---|---|---|---|
| WMS | 1.3.0 - 1.1.1 | 1.3.0 - 1.1.1 | 1.3.0 - 1.1.1 |
| WFS | 1.1.0 - 1.0.0 | 2.0.0 - 1.0.0 | 2.0.0 - 1.0.0 |
| OAPIF (WFS3) | 1.0.0 | Sí | No |
| WMTS | 1.0.0 | 1.0.0 | 1.0.0 |
| WCS | 1.0.0 | 2.0.1 - 1.0.0 | 2.0.1 - 1.0.0 |
| WPS | No | 1.0.0 | 1.0.0 |
| CSW | No | 2.0.2 | No |
| SLD | Sí | Sí | Sí |

| Prestación | QGIS Server | GeoServer | ArcGIS Server |
|---|---|---|---|
| Desde | 2006 | 2001 | 1999 |
| Licencia | GPL | GPL | comercial |
| Tecnología | C++/Python | Java | C++ |
| Caché de tesela | Sí | Sí (vía GeoWebCache) | Sí |
| 3D | No | No | Sí |
| Administración del servidor | vía terceros (LizMap, QWC2…) | web + API REST | web + API REST |

**Arquitectura típica con GeoServer:**
- Interfaz de usuario: Leaflet, OpenLayers, QGIS
- Servidor web: GeoServer ↔ GeoWebCache
- Base de datos: PostGIS

**7. Tipos de datos en GeoServer**
- **Espacio de trabajo (Workspace):** contenedor usado para agrupar capas similares; espacio aislado ligado a un proyecto. Permite reutilizar nombres de capa idénticos en distintos workspaces sin conflicto. Todas las capas y almacenes de datos deben tener un workspace asociado (excepto los grupos de capas). Consta de un **nombre** (máx. 10 caracteres, sin espacios) y un **URI** (identificador único, no necesita apuntar a una ubicación real; se recomienda usar una URL del proyecto).
- **Almacén de datos (Store):** contenedor de datos geográficos; se conecta a una fuente de datos raster o vectorial (un archivo/grupo de archivos, una tabla de BD o un directorio). Los parámetros de conexión se definen una vez en el store en lugar de repetirlos por cada dato. Cada almacén de datos está asociado a **un único** workspace.
- **Capas (Layers):** datos raster o vectoriales que contienen los elementos geográficos que se muestran en el mapa. Las capas vectoriales son análogas a los *featureTypes*; las capas raster, a las *coberturas*. GeoServer almacena info asociada (proyección, cuadro delimitador, estilo). Cada capa debe tener asociado un workspace.
- **Grupos de capas:** contenedor donde capas (y otros grupos) se organizan en una estructura jerárquica; se pueden referenciar por un nombre para simplificar peticiones WMS. Permiten combinar datos de distinta geometría/contenido. **No respetan** el concepto de workspace — solo son relevantes para peticiones WMS.
- *Ejemplo del curso:* workspace `usa` con un store PostGIS y un store de directorio de shapefiles; workspace `earth` con un store Oracle, un store CSV y un store ArcGrid; cada workspace agrupando sus propias capas (ciudades, imagen satélite, barrios…).

**8. Estilos (SLD)**
- Un **estilo** es una directiva de visualización para representar los datos geográficos: color, forma, tamaño, junto con reglas avanzadas según atributos y nivel de zoom.
- Cada capa debe estar asociada con al menos un estilo (GeoServer aplica uno predeterminado a cada capa nueva).
- GeoServer usa el lenguaje de marcado **Styled Layer Descriptor (SLD)**, estándar basado en XML creado por la OGC, para describir los datos geoespaciales.

*Ejemplo de estilo SLD para un punto (círculo rojo, tamaño 6):*
```xml
<FeatureTypeStyle>
  <Rule>
    <PointSymbolizer>
      <Graphic>
        <Mark>
          <WellKnownName>circle</WellKnownName>
          <Fill>
            <CssParameter name="fill">#FF0000</CssParameter>
          </Fill>
        </Mark>
        <Size>6</Size>
      </Graphic>
    </PointSymbolizer>
  </Rule>
</FeatureTypeStyle>
```

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

---

## Unidad 3. Estándares abiertos e interoperables del OGC

### Resumen estructurado

#### 1. Introducción a las IDE (Infraestructura de Datos Espaciales)
- **¿Qué es una IDE?** Sistema informático integrado por un conjunto de recursos que permite el acceso y la gestión de conjuntos de datos y servicios geográficos disponibles en Internet.
- Una IDE cumple normas, estándares y especificaciones que regulan y garantizan la **interoperabilidad** de la información geográfica; requiere además un **marco legal** que asegure que los datos producidos por las instituciones se comparten entre administraciones y se potencia su uso ciudadano.
- La puesta en práctica de un proyecto IDE se materializa mediante un **Geoportal**, que debe ofrecer como mínimo tres clientes:
  - **Localización:** búsqueda de conjuntos de datos y servicios a través de sus metadatos.
  - **Nomenclátor:** localización en un mapa a través de un nombre geográfico.
  - **Visualización:** visualización de los datos vía servicios web y, opcionalmente, su consulta.
- En Europa y España se siguen las especificaciones de interoperabilidad del **Open Geospatial Consortium (OGC)**. Para la comunidad hispanohablante y portuguesa existe el **Foro Ibérico y Latinoamericano de OGC (OGC ILAF)**.

**Categorías de estándares OGC según su función:**

| Función | Estándares |
|---|---|
| Visualizar datos | WMS, SLD, Georeferenced Table Join Service (TJS), WMTS |
| Acceder a datos | WFS, WCS, Sensor Observation Service (SOS) |
| Codificar datos | KML, GML, Sensor Web Enablement (SWE), Observations & Measurements (O&M), SensorML |
| Catálogos y registros | Catalogue Service for Web (CSW) |
| Procesado de datos | WPS, Coordinate Transformation Service (WCTS) |

---

#### 2. Web Map Service (WMS)
- **WMS ⇒ imagen del mapa.** Protocolo estándar OGC que sirve **imágenes** de mapas a partir de información geográfica: el mapa no son los datos, sino una imagen de los mismos. En resumen, WMS es la forma en que un cliente solicita imágenes de mapa a un servidor.
- Los mapas se dibujan como imágenes (PNG, GIF, JPEG) u ocasionalmente como vectores (SVG, WebCGM). Los formatos con fondo transparente (GIF, PNG) permiten ver las capas subyacentes.
- Se visualizan mediante **clientes ligeros** (navegador web) o **clientes pesados** (software de escritorio: gvSIG, QGIS, ArcGIS…), ambos con operaciones de visualización: activar/desactivar capas, cambiar orden/transparencia, zoom, desplazamiento…
- **Beneficios:** interfaz estándar que permite combinar imágenes de múltiples servidores WMS en una sola vista; capacidad de **reproyectar al vuelo** (los datos permanecen en su SRS original y el servidor genera la salida en otro SRS para que las capas se superpongan).

**Operaciones de WMS:**

| Operación | Descripción |
|---|---|
| Exceptions | Reporta si ocurre una excepción |
| **GetCapabilities** (obligatoria) | Metadatos del servicio: operaciones, parámetros admitidos y lista de capas disponibles |
| **GetMap** (obligatoria) | Devuelve una imagen de mapa de un área y contenido especificado |
| GetFeatureInfo (opcional) | Devuelve datos subyacentes (geometría + atributos) para una posición de píxel |
| DescribeLayer (opcional) | Indica el WFS/WCS para recuperar información adicional de la capa |
| GetLegendGraphic (opcional) | Recupera una leyenda generada para un mapa |

**Reglas de solicitud:** las operaciones se invocan por **HTTP GET** (URL del servicio + parámetros `name=value` separados por `&`, tras un `?` obligatorio: host, puerto opcional, ruta opcional) o por **HTTP POST** (URL completa + parámetros de la petición formulados en un **documento XML**).

*Ejemplo GET GetMap:*
```
https://mirame.chduero.es/geoserver/mirame/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=mirame:Limites_Demarcacion,mirame:Masas_Agua_Rio&SRS=EPSG:4326&BBOX=-7.7,40.1,-1.7,43.2&FORMAT=image/png&WIDTH=600&HEIGHT=255
```

*Ejemplo POST GetMap (documento XML):*
```xml
<?xml version="1.0" encoding="UTF-8"?>
<ogc:GetMap xmlns:ogc="http://www.opengis.net/ows"
xmlns:gml="http://www.opengis.net/gml" version="1.1.1" service="WMS">
 <StyledLayerDescriptor version="1.0.0">
   <NamedLayer>
     <Name>topp:states</Name>
     <NamedStyle><Name>population</Name></NamedStyle>
   </NamedLayer>
 </StyledLayerDescriptor>
 <BoundingBox srsName="http://www.opengis.net/gml/srs/epsg.xml#4326">
   <gml:coord><gml:X>-130</gml:X><gml:Y>24</gml:Y></gml:coord>
   <gml:coord><gml:X>-55</gml:X><gml:Y>50</gml:Y></gml:coord>
 </BoundingBox>
 <Output>
   <Format>image/png</Format>
   <Size><Width>550</Width><Height>250</Height></Size>
 </Output>
</ogc:GetMap>
```

**Operación GetCapabilities de WMS** (obligatoria): parámetros `service` (=WMS), `version` (1.0.0/1.1.0/1.1.1/1.3), `request` (=GetCapabilities). GeoServer relaja el requisito de `version`, estableciendo una por defecto si se omite, pero para cumplir el estándar siempre debe especificarse. La respuesta es un **documento XML de capacidades** con dos secciones principales: `Service` (metadatos de servicio: nombre, palabras clave, contacto) y `Capability` (contiene `Request`, `Exception` y `Layer` — esta última lista las capas y sistemas de coordenadas disponibles, con título/resumen/palabras clave por capa).

*Ejemplo:* `https://mirame.chduero.es/geoserver/mirame/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities`

**Operación GetMap de WMS** (obligatoria): solicita que el servidor genere un mapa. Parámetros básicos: capas y estilos a representar, cuadro delimitador, SRS de destino, ancho/alto, formato de salida.

| Parámetro | Requerido | Descripción |
|---|---|---|
| service | Sí | Valor: WMS |
| version | Sí | 1.0.0 / 1.1.0 / 1.1.1 / 1.3.0 |
| request | Sí | Valor: GetMap |
| layers | Sí | Lista de capas separadas por comas |
| styles | Sí | Lista de estilos (vacío = estilo por defecto) |
| srs / crs | Sí | SRS de salida (forma EPSG:nnn); `crs` es la clave usada en WMS 1.3.0 |
| bbox | Sí | minx,miny,maxx,maxy en unidades del SRS |
| width / height | Sí | Tamaño de salida en píxeles |
| format | Sí | png, jpg, tiff, svg, kml, PDF… |
| transparent | No | true/false (por defecto false) |
| bgcolor | No | RRGGBB (por defecto FFFFFF) |
| exceptions | No | Formato de excepciones (por defecto application/vnd.ogc.se_xml) |
| time | No | Valor o rango temporal |
| sld / sld_body | No | Referencia o documento XML SLD que controla/mejora el estilo de las capas |

**Operación GetFeatureInfo de WMS** (opcional): solicita datos espaciales y de atributos de los objetos geográficos en un lugar determinado del mapa. Es similar a GetFeature de WFS pero menos flexible (se recomienda usar GetFeature siempre que sea posible); su única ventaja es que trabaja con un valor de píxel (x,y) de una imagen WMS. Parámetros clave adicionales: `query_layers`, `info_format` (opcional), `feature_count` (opcional, por defecto 1), `x`/`i` e `y`/`j` (coordenadas de píxel; `i`/`j` son las claves en WMS 1.3.0).

**Operación DescribeLayer y GetLegendGraphic de WMS:** `DescribeLayer` se usa principalmente por clientes que entienden WMS basados en SLD — solo encamina al cliente hacia el servicio (WMS o WFS) adecuado para conocer la estructura de los datos. `GetLegendGraphic` genera gráficos de leyenda como imágenes, basados en el estilo del servidor o en un SLD suministrado por el usuario.

---

#### 3. Web Feature Service (WFS)
- **WFS ⇒ datos geográficos.** Estándar OGC para crear, modificar e intercambiar información geográfica **vectorial** en Internet mediante HTTP. Permite crear mapas/aplicaciones propias a partir de los datos de origen, convertir entre formatos y manipular geográficamente los datos en bruto.
- Codifica y transfiere información en **Geography Markup Language (GML)**, subconjunto de XML. Versión actual: 2.0.0; GeoServer soporta 2.0.0, 1.1.0 y 1.0.0.
- **Beneficios:** a través de descubrimiento, consulta, bloqueo y transacción, permite interrogar, dar estilo, editar (crear/actualizar/eliminar) y descargar objetos geográficos individuales, de forma independiente de la fuente de datos subyacente.

**Operaciones de WFS:**

| Operación | Descripción |
|---|---|
| **GetCapabilities** (obligatoria) | Metadatos del servicio WFS y sus operaciones/parámetros |
| **DescribeFeatureType** (obligatoria) | Descripción de los tipos de objetos geográficos soportados |
| **GetFeature** (obligatoria) | Selección de objetos geográficos con geometría y atributos |
| LockFeature (opcional) | Bloqueo persistente que evita que un objeto sea editado |
| Transaction (opcional) | Edición (crear/actualizar/eliminar) de tipos de entidad existentes |

**Reglas de solicitud:**
- Atributos en peticiones GET: `VERSION` (obligatorio), `SERVICE=WFS` (obligatorio, no exigido en GetCapabilities), `REQUEST` (obligatorio), `NAMESPACE` (opcional, formato `xmlns(prefix=EscapedNamespaceName)`), parámetros adicionales de cada operación, parámetros específicos de suministrador (opcional).
- Atributos en peticiones POST: `VERSION` y `SERVICE=WFS` (obligatorios), `HANDLE` (opcional, nombre nemotécnico para localizar errores).

**GetCapabilities de WFS** (obligatoria): parámetros `service`, `version`, `request`. Respuesta = documento XML de capacidades con componentes: `ServiceIdentification` (título, ServiceType/versiones soportadas), `ServiceProvider` (contacto), `OperationsMetadata` (operaciones y parámetros soportados), `FeatureTypeList` (tipos de objetos `namespace:featuretype`, proyección y bbox por tipo), `Filter_Capabilities` (filtros/expresiones disponibles: SpatialOperators como Equals/Touches, ComparisonOperators como LessThan/GreaterThan).

*Ejemplo:* `https://juntadeandalucia.es/medioambiente/mapwms/REDIAM_WFS_riesgos_naturales?SERVICE=WFS&VERSION=1.1.0&REQUEST=GetCapabilities`

**DescribeFeatureType de WFS** (obligatoria): solicita información sobre un tipo de objeto geográfico individual (lista de features y atributos, o lista de tipos disponibles) antes de pedir los datos reales. Parámetros: `service`, `version`, `request`, `typeNames` (`typeName` en 1.1.0 y anteriores), `exceptions` (opcional), `outputFormat` (opcional). La respuesta es un esquema XSD con la lista de tipos de entidades ordenados por espacio de nombres.

*Ejemplo (sobre un tipo concreto):* `...&REQUEST=DescribeFeatureType&typeName=zona_pel_incendios`

**GetFeature de WFS** (obligatoria): devuelve instancias de fenómenos (objetos individuales) en formato GML, permitiendo solicitar las propiedades deseadas y realizar consultas espaciales y no espaciales.
- *Ejemplo:* `...&REQUEST=GetFeature&typeName=zona_pel_incendios`
- Para restringir por **atributo** en vez de por elemento se usa la clave `propertyName` (o directamente el nombre del atributo como parámetro), pudiendo especificar uno o varios atributos separados por comas. *Ejemplo:* `...&REQUEST=GetFeature&TYPENAME=zona_pel_incendios&COD_INE=zona_pel_incendios.41041`

**LockFeature de WFS** (opcional): petición de bloqueo sobre uno o más tipos de fenómenos mientras se realiza su modificación con `Transaction`, asegurando transacciones de forma continuada.

**Transaction de WFS** (opcional): compuesta de operaciones que modifican instancias de fenómenos geográficos accesibles vía web; al terminar, el WFS genera un documento XML de respuesta. Puede realizarse directamente por el WFS (trasladando los cambios al almacén de datos) o traducirse al lenguaje del almacén de datos. Operaciones de modificación posibles: **crear** (Insert), **actualizar** (Update), **eliminar** (Delete). Un servidor WFS que soporta transacciones se conoce como **WFS-T**.

**GetGmlObject de WFS** (opcional): devuelve instancias de fenómenos expresadas en XML. El cliente puede especificar si desea todos los objetos anidados mediante Xlinks o solo hasta un nivel de anidamiento determinado. *Diferencia con GetFeature:* GetFeature devuelve todas las instancias del tipo solicitado, mientras que GetGmlObject solo obtiene las instancias solicitadas mediante su **identificador** (requiere que cada elemento tenga un ID XML único, codificado según la especificación OpenGIS Filter Encoding).

---

#### 4. Web Coverage Service (WCS)
- **WCS ⇒ acceso a datos ráster (cobertura).** Al igual que WMS y WFS, permite al cliente seleccionar parte de la información del servidor (p. ej. por restricciones espaciales). La diferencia principal con WMS es que WCS proporciona los datos **junto con su descripción detallada**, con una sintaxis de petición rica, y devuelve la información con su **semántica original** (interpretable/extrapolable, no solo representada de forma estática).
- En cierto sentido, **WCS es la analogía ráster de WFS**: acceso a los datos ráster almacenados en un servidor.

**Operaciones de WCS:**

| Operación | Descripción |
|---|---|
| **GetCapabilities** (obligatoria) | Lista de datos del servidor y operaciones/parámetros WCS válidos |
| **DescribeCoverage** (obligatoria) | Documento XML que describe completamente las coberturas solicitadas |
| **GetCoverage** (obligatoria) | Devuelve una cobertura en un formato conocido (similar a GetMap de WMS, con extensiones para coberturas) |

**GetCapabilities de WCS**: parámetros `service` (=WCS), `AcceptVersions` (opcional: 1.0.0/1.1.0/2.0), `request` (=GetCapabilities). La respuesta (**documento de capacidades**) consiste en una sección de metadatos del servicio (`ServiceMetadata`) y una sección opcional de contenidos (`Content`) con información sobre las coberturas ofrecidas.

*Ejemplo:* `https://servicios.idee.es/wcs-inspire/mdt?version=2.0.1&request=GetCapabilities&service=WCS`

**DescribeCoverage de WCS**: devuelve un documento XML con la descripción detallada de una o varias coberturas, que debe contener: `CoverageDescription` (lista de coberturas descritas), `coverageID` (identificador único), `domainSet` (dominio espacial/temporal de la información), `rangeType` (rango de valores y tipo de propiedades por localización), `serviceParameters` (parámetros específicos del servicio).

*Ejemplo:* `https://servicios.idee.es/wcs-inspire/mdt?REQUEST=DescribeCoverage&SERVICE=WCS&VERSION=2.0.1&COVERAGEID=Elevacion4258_1000`

**GetCoverage de WCS**: permite obtener una cobertura o parte de ella, indicando mediante coordenadas (bounding box) la porción deseada; el resultado es la intersección del cuadro solicitado con la cobertura ofrecida. Parámetros: `service`, `version`, `request` (=GetCoverage), `coverageid`, `extension` (opcional), `dimension` (opcional).

*Ejemplo:*
```
https://servicios.idee.es/wcs-inspire/mdt?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID=Elevacion4258_1000&FORMAT=image/png&BBOX=188325,3060650,653825,3255025&CRS=EPSG:25830&RESX=200&RESY=200
```

---

#### 5. Web Processing Service (WPS)
- **WPS** es un servicio para la **publicación de procesos geoespaciales, algoritmos y cálculos**. Un "proceso" es cualquier algoritmo, cálculo o modelo que opere sobre datos espacialmente referenciados (ráster o vectorial); gracias a su interfaz genérica, un WPS puede ofrecer cualquier funcionalidad SIG a través de una red, y puede contener otros servicios OGC existentes.
- WPS describe un interfaz de petición/respuesta que define cómo: codificar solicitudes y respuestas de ejecución de procesos, integrar datos y metadatos en entradas/salidas, referenciar vía web datos de entrada/salida, realizar procesos de larga duración, devolver el estado del proceso y errores, y solicitar el almacenamiento de resultados.

**Operaciones de WPS (todas obligatorias):**

| Operación | Descripción |
|---|---|
| GetCapabilities | Metadatos del servicio WPS y sus operaciones/parámetros válidos |
| DescribeProcess | Descripción de los procesos disponibles (parámetros y formatos de entrada/salida) |
| Execute | Ejecuta procesos específicos del WPS con los parámetros suministrados |

**GetCapabilities de WPS**: parámetros `service` (=WPS), `AcceptVersions` (opcional: 1.0.0/0.1.0/0.2.0), `request` (=GetCapabilities). El **documento de capacidades** da los nombres y una descripción general de cada proceso ofrecido (ej. un proceso "intersección" limitado a intersectar un polígono con otro).

*Ejemplo:* `https://www.ign.es/wps-transformacion/servicios?Service=WPS&Request=GetCapabilities`

**DescribeProcess de WPS**: ofrece información detallada de los procesos ejecutables por `Execute`: parámetros y formatos de entrada requeridos y formatos de salida resultantes. *Ejemplo:* proceso de intersección que requiere dos entradas (`PrimerPolígono`, `SegundoPolígono`) en GML 2.2 o 3.1, enviables como recurso accesible vía web.

*Ejemplo:* `https://www.ign.es/wps-transformacion/servicios?REQUEST=DescribeProcess&SERVICE=WPS&VERSION=1.0.0&Identifier=TransformCoordinates`

**Execute de WPS**: ejecuta procesos específicos usando como entrada los parámetros suministrados (integrados en la petición o vía una fuente de datos accesible por web) y devuelve los valores producidos en la salida, ya sea directamente o almacenados como recurso accesible vía web (respuesta = documento XML con una URL por salida almacenada). Normalmente la respuesta se devuelve al finalizar el proceso, pero el cliente puede solicitar una respuesta inmediata con una URL para recuperar el resultado más tarde, y pedir al servidor que actualice regularmente el progreso del proceso (procesamiento asíncrono).

---

#### 6. Styled Layer Descriptor (SLD)
- **SLD** es un **perfil del servicio WMS**: una codificación que permite al usuario personalizar la simbología y los colores de los componentes del mapa, mediante una norma que define un lenguaje común entendible por cliente y servidor.

**Operaciones del servicio SLD:**

| Operación | Descripción |
|---|---|
| **GetCapabilities** (obligatoria) | Solicitud de las características del servicio |
| **GetMap** (obligatoria) | Definida en el estándar WMS; solicitud de un área en un CRS determinado, permitiendo crear un *"user style"* para modificar el estilo de visualización |
| DescribeLayer (opcional) | Proporciona información sobre los fenómenos a simbolizar (necesaria para construir un SLD personalizado) |
| GetLegendGraphic (opcional) | Obtiene una imagen del estilo con el que el servicio representa la capa |

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

---

