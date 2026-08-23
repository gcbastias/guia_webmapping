# Glosario acumulativo

| Término | Definición |
|---|---|
| **Webmapping / SIG web** | Aplicación que permite visualizar e interactuar con cartografía y datos geográficos a través de un navegador web. |
| **Shapefile (.shp)** | Formato vectorial clásico de ESRI (años 90), muy extendido pero con limitaciones (multifile, sin definición de CRS, límite de 2GB, sin topología). |
| **GeoJSON** | Formato vectorial basado en JSON, ligero y transmisible, ideal para intercambio web; no es consultable ni soporta raster. |
| **PostGIS** | Extensión espacial de PostgreSQL que añade tipos de datos y funciones geométricas/geográficas a la base de datos. |
| **PostgreSQL** | Sistema gestor de bases de datos objeto-relacional, open source (licencia BSD), sobre el que se instala PostGIS. |
| **GeoPackage (.gpkg)** | Formato de base de datos SQLite espacial, consultable, que puede contener vector y raster. |
| **MBTiles** | Especificación de MapBox para almacenar teselas (tiles) en una única base de datos SQLite. |
| **WMS (Web Map Service)** | Estándar OGC para servir mapas como imágenes ráster a través de la web. |
| **WFS (Web Feature Service)** | Estándar OGC para servir entidades vectoriales (features) con sus atributos. |
| **SRID** | Identificador del sistema de referencia espacial (ej. 4326 = WGS84 lat/lon). |
| **GeoServer / MapServer** | Servidores de mapas open source que exponen datos vectoriales/raster mediante estándares OGC (WMS, WFS...). |
| **GeoWebCache** | Servicio de teselado/caché que trabaja junto a GeoServer en la arquitectura de servidor web. |
| **OpenLayers / Leaflet** | Librerías JavaScript open source para construir visores de mapas web. |
| **pgAdmin** | Cliente gráfico (front-end) oficial de PostgreSQL para administrar bases de datos; más amigable que psql. |
| **psql** | Cliente de línea de comandos (cliente de texto) de PostgreSQL. |
| **Bounding box** | Rectángulo de tamaño más pequeño capaz de contener un elemento geográfico dado; usado por los índices espaciales para el procesamiento eficiente. |
| **Índice espacial (GiST / R-Tree)** | Estructura de índice multidimensional que permite el procesamiento eficiente de operaciones espaciales, a diferencia de un B-tree tradicional. |
| **ST_Geometry** | Superclase de la jerarquía de tipos espaciales de la que derivan ST_Point, ST_Curve, ST_Surface, ST_GeometryCollection, etc. |
| **spatial_ref_sys** | Tabla de metadatos de PostGIS (conforme a OGC) que define ~3.000 sistemas de referencia espacial conocidos y los detalles para transformar/reproyectar entre ellos. |
| **geometry_columns / geography_columns** | Vistas de PostGIS que documentan qué tablas/columnas tienen geometría/geografía y con qué SRID. |
| **auth_name / auth_srid** | Columnas de `spatial_ref_sys`: nombre del organismo que define el sistema de referencia (ej. "EPSG") y el código de ese organismo para dicho sistema. |
| **srtext** | Columna de `spatial_ref_sys` con la representación WKT del sistema de referencia espacial. |
| **proj4text** | Columna de `spatial_ref_sys` con la cadena de definición Proj4 de un SRID; PostGIS usa la biblioteca Proj4 para transformar coordenadas. |
| **Proj4** | Biblioteca/formato de cadenas para definir y transformar sistemas de referencia espacial, usada internamente por PostGIS. |
| **UTM (Universal Transverse Mercator)** | Sistema de proyección dividido en zonas que cubren 6 grados de longitud cada una; es de los más idóneos para mediciones precisas. |
| **OpenGIS / OGC** | Open Geospatial Consortium; organismo que define estándares para interoperabilidad de datos geoespaciales (ej. la especificación SFSQL, WMS, WFS). |
| **SFSQL (Simple Features Specification for SQL)** | Norma de OpenGIS que define los tipos estándar de objetos GIS, las funciones para manipularlos y las tablas de metadatos asociadas. Solo maneja geometrías en 2D. PostGIS se apoya principalmente en la versión SFS1.1 (1999). |
| **SQL-MM (SQL Multimedia Applications Spatial)** | Especificación (documento ISO "SQL/MM Part 3: Spatial") que amplía SFSQL definiendo curvas circularmente interpoladas (CIRCULARSTRING, COMPOUNDCURVE, CURVEPOLYGON, etc.); incluye coordenadas 3dm/3dz/4d pero no SRID. |
| **WKT (Well-Known Text)** | Representación de texto plano de una geometría, ej. `POINT(-3.68 40.40)`. Sigue SFSQL; no maneja geometrías de 3-4 dimensiones. |
| **WKB (Well-Known Binary)** | Representación binaria de una geometría (equivalente binario del WKT); la mayoría de procesos reales la utilizan por eficiencia. |
| **EWKT (Extended Well-Known Text)** | Extensión de PostGIS al formato WKT que añade metadatos SRID y soporta geometrías de 3-4 dimensiones. |
| **EWKB (Extended Well-Known Binary)** | Extensión de PostGIS al formato WKB equivalente a EWKT, con metadatos SRID. |
| **GML (Geographic Markup Language)** | Formato de intercambio de geometrías basado en XML, soportado por PostGIS para emisión y consumo. |
| **KML (Keyhole Markup Language)** | Formato de intercambio de geometrías basado en XML (usado por Google Maps y Google Earth, entre otros), soportado por PostGIS y generado de forma nativa por GeoServer. |
| **SVG (Scalable Vector Graphics)** | Formato vectorial gráfico; PostGIS puede exportar una geometría como ruta de datos SVG. |
| **geography (tipo)** | Tipo de dato de PostGIS (desde v1.5) que trabaja con coordenadas esféricas reales, útil para datos dispersos globalmente; complementa al tipo `geometry`, que trabaja en el plano cartesiano. |
| **ST_GeometryType()** | Devuelve el tipo de geometría (POINT, POLYGON, etc.) de un valor. |
| **ST_NDims()** | Devuelve la dimensión de las coordenadas de una geometría (2, 3 o 4). |
| **ST_SRID()** | Devuelve el identificador de referencia espacial (SRID) de una geometría, según `spatial_ref_sys`. |
| **ST_AsText()** | Función PostGIS que convierte una geometría binaria en texto WKT legible, sin metadatos SRID. |
| **ST_AsBinary()** | Devuelve la representación WKB de una geometría/geografía, sin metadatos SRID. |
| **ST_AsEWKT() / ST_AsEWKB()** | Devuelven la representación WKT/WKB extendida (con metadatos SRID) de una geometría. |
| **ST_GeomFromText()** | Crea una geometría a partir de su representación WKT. |
| **ST_GeomFromWKB()** | Crea una geometría a partir de su representación WKB (y opcionalmente el SRID). |
| **ST_GeomFromGML() / ST_GeomFromKML()** | Crean una geometría PostGIS a partir de una representación GML/KML de entrada. |
| **ST_AsGeoJSON()** | Devuelve una geometría como elemento GeoJSON (texto). |
| **ST_AsGML() / ST_AsKML() / ST_AsSVG()** | Devuelven una geometría en formato GML / KML / SVG respectivamente. |
| **ST_GeographyFromText()** | Devuelve un valor `geography` a partir de su representación WKT/WKT extendida. |
| **ST_Area()** | Devuelve el área de un polígono o multipolígono (en unidades del SRID para `geometry`, en m² para `geography`). |
| **ST_Length()** | Devuelve la longitud 2D de una geometría lineal (unidades del SRID en `geometry`, metros en `geography`). |
| **ST_Perimeter()** | Devuelve la longitud de los límites de una superficie (polígono/multipolígono). |
| **ST_NPoints()** | Devuelve el número de vértices de una geometría. |
| **ST_NRings()** | Devuelve el número de anillos de un polígono o multipolígono. |
| **ST_NumGeometries()** | Devuelve el número de geometrías de una GEOMETRYCOLLECTION o tipo MULTI*. |
| **ST_GeometryN()** | Devuelve la geometría n-ésima (1 a N) de una colección o tipo MULTI*. |
| **ST_ExteriorRing()** | Devuelve el anillo exterior (linestring) de un POLYGON. |
| **ST_InteriorRingN()** | Devuelve el n-ésimo anillo interior de un POLYGON. |
| **ST_StartPoint() / ST_EndPoint()** | Devuelven el primer/último punto de una geometría LINESTRING como POINT. |
| **ST_X() / ST_Y()** | Devuelven la coordenada X / Y de un punto. |
| **ST_Transform()** | Devuelve una nueva geometría con sus coordenadas reproyectadas a otro SRID. |
| **AddGeometryColumn()** | Función de administración que crea una nueva columna de geometría en una tabla. |
| **Populate_Geometry_Columns()** | Función que asegura que las columnas geométricas tengan las restricciones espaciales correctas y estén registradas en `geometry_columns`. |
| **ST_Equals()** | Comprueba si dos geometrías representan la misma geometría espacial (ignora direccionalidad). |
| **ST_Disjoint()** | Comprueba si dos geometrías no comparten ningún espacio entre sí. |
| **ST_Crosses()** | Comprueba si dos geometrías comparten algunos puntos interiores, pero no todos. |
| **ST_Overlaps()** | Comprueba si dos geometrías de la misma dimensión comparten espacio sin que una contenga completamente a la otra. |
| **ST_Touches()** | Comprueba si dos geometrías comparten al menos un punto pero sus interiores no se intersectan. |
| **ST_Within() / ST_Contains()** | Comprueban si una geometría está completamente dentro de otra (relación inversa entre ambas). |
| **ST_Intersects()** | Comprueba si dos geometrías comparten cualquier porción de espacio (no son disjuntas). |
| **ST_DWithin()** | Comprueba si dos geometrías están a una distancia menor o igual a un radio dado. |
| **ST_Distance()** | Calcula la distancia mínima entre dos geometrías; cartesiana 2D en `geometry` (en unidades del SRID), esferoidal en metros por defecto en `geography`. |
| **ST_Centroid()** | Función PostGIS que calcula el centroide (punto central) de una geometría. |
| **ST_PointOnSurface()** | Devuelve un punto garantizado dentro de la superficie de una geometría (útil en formas cóncavas, a diferencia de `ST_Centroid`). |
| **ST_Buffer()** | Función PostGIS que genera una zona de influencia (área) alrededor de una geometría; el parámetro `quad_segs` controla la suavidad de las curvas. |
| **ST_Intersection()** | Devuelve la geometría que representa la porción compartida (intersección) entre dos geometrías. |
| **ST_Union()** | Devuelve la geometría que representa la unión de puntos de dos o más geometrías. |
| **IDE (Infraestructura de Datos Espaciales)** | Conjunto de tecnologías, políticas y estándares que permiten descubrir, visualizar y compartir datos geoespaciales. |
| **Dashboard** | Panel de mando o de control que combina mapas con tablas, gráficos y KPIs. |

*(Ampliación — Unidad 3: Servidores de datos espaciales, GeoServer y estándares OGC)*

| **Servlet** | Módulo escrito en Java que se utiliza en un servidor (sea o no servidor web) para extender sus capacidades de respuesta a los clientes. GeoServer está empaquetado como un servlet independiente. |
| **MapServer** | Servidor de mapas web open source, ligero y rápido; alternativa a GeoServer. |
| **Lizmap** | Servidor de mapas web open source que actúa como frontend (interfaz web) para QGIS. |
| **MapProxy** | Servidor de mapas web open source que actúa como proxy para acelerar servicios WMS; se integra con GeoServer y MapServer. |
| **QGIS Server** | Servidor de mapas web open source, complemento de QGIS que publica proyectos QGIS como servicios OGC (WMS, WFS, WCS, WMTS...). |
| **Workspace (espacio de trabajo)** | En GeoServer, contenedor usado para agrupar capas similares, aislado y ligado a un proyecto; formado por un nombre (máx. 10 caracteres) y un URI único. Toda capa/almacén de datos debe tener un workspace asociado. |
| **Store (almacén de datos)** | En GeoServer, contenedor de datos geográficos que se conecta a una fuente de datos raster o vectorial; está asociado a un único workspace. |
| **Grupo de capas** | En GeoServer, contenedor que organiza capas y otros grupos en una estructura jerárquica, referenciable por nombre; no respeta el concepto de workspace y solo es relevante para peticiones WMS. |
| **Geoportal** | Materialización práctica de una IDE; ofrece como mínimo tres clientes: localización, nomenclátor y visualización. |
| **OGC ILAF** | Foro Ibérico y Latinoamericano del OGC, para la comunidad de habla hispana y portuguesa interesada en sus desarrollos y objetivos. |
| **WMS (Web Map Service)** | Estándar OGC que sirve imágenes de mapas (no los datos en sí) a partir de información geográfica; permite reproyección al vuelo. Operaciones: GetCapabilities, GetMap (obligatorias), GetFeatureInfo, DescribeLayer, GetLegendGraphic (opcionales). |
| **GetMap** | Operación obligatoria de WMS/SLD que devuelve una imagen de mapa de un área, capas, estilo y formato especificados. |
| **GetFeatureInfo** | Operación opcional de WMS que devuelve los datos (geometría y atributos) subyacentes a una posición de píxel en un mapa. |
| **WFS (Web Feature Service)** | Estándar OGC para crear, modificar e intercambiar información geográfica vectorial vía HTTP, codificada en GML. Operaciones: GetCapabilities, DescribeFeatureType, GetFeature (obligatorias), LockFeature, Transaction (opcionales). |
| **DescribeFeatureType** | Operación obligatoria de WFS que devuelve la descripción (esquema) de los tipos de objetos geográficos soportados. |
| **GetFeature** | Operación obligatoria de WFS que devuelve instancias de objetos geográficos (geometría + atributos) en formato GML. |
| **LockFeature** | Operación opcional de WFS que bloquea uno o más tipos de fenómenos mientras se edita con Transaction. |
| **Transaction (WFS-T)** | Operación opcional de WFS que permite crear, actualizar y eliminar instancias de objetos geográficos; un servidor WFS que la soporta se llama WFS-T. |
| **GetGmlObject** | Operación opcional de WFS que devuelve instancias de fenómenos identificadas por su ID XML (a diferencia de GetFeature, que devuelve todas las instancias de un tipo). |
| **WCS (Web Coverage Service)** | Estándar OGC, analogía ráster de WFS: da acceso a datos ráster (coberturas) junto con su descripción detallada y semántica original. Operaciones (todas obligatorias): GetCapabilities, DescribeCoverage, GetCoverage. |
| **DescribeCoverage** | Operación de WCS que devuelve un documento XML con la descripción detallada de una o varias coberturas (CoverageDescription, coverageID, domainSet, rangeType, serviceParameters). |
| **GetCoverage** | Operación de WCS que devuelve una cobertura (o parte de ella, según un bounding box) en un formato conocido. |
| **WPS (Web Processing Service)** | Estándar OGC para publicar procesos geoespaciales, algoritmos y cálculos sobre datos ráster o vectoriales. Operaciones (todas obligatorias): GetCapabilities, DescribeProcess, Execute. |
| **DescribeProcess** | Operación de WPS que describe los parámetros y formatos de entrada/salida de los procesos ejecutables. |
| **Execute** | Operación de WPS que ejecuta un proceso específico con los parámetros suministrados, devolviendo el resultado directamente o como recurso accesible vía web. |
| **SLD (Styled Layer Descriptor)** | Perfil del servicio WMS, estándar OGC basado en XML que permite personalizar la simbología y los colores de un mapa. Operaciones: GetCapabilities, GetMap (obligatorias), DescribeLayer, GetLegendGraphic (opcionales). |
| **DescribeLayer** | Operación de WMS/SLD que encamina al cliente hacia el servicio (WMS o WFS) adecuado para conocer la estructura de los datos a simbolizar. |
| **GetLegendGraphic** | Operación de WMS/SLD que genera un gráfico de leyenda como imagen, según el estilo del servidor o un SLD suministrado por el usuario. |
| **WMTS (Web Map Tile Service)** | Estándar OGC para visualizar datos mediante teselas (tiles) pre-generadas. |
| **TJS (Georeferenced Table Join Service)** | Estándar OGC para visualizar datos uniendo tablas georreferenciadas. |
| **SOS (Sensor Observation Service)** | Estándar OGC para acceder a datos de sensores. |
| **SWE (Sensor Web Enablement)** | Estándar OGC para codificar datos relacionados con sensores. |
| **O&M (Observations & Measurements)** | Estándar OGC para codificar observaciones y mediciones de sensores. |
| **SensorML** | Estándar OGC para codificar modelos y metadatos de sensores. |
| **CSW (Catalogue Service for the Web)** | Estándar OGC de descubrimiento de datos para catálogos y registros geoespaciales. |
| **WCTS (Coordinate Transformation Service)** | Estándar OGC para el procesado/transformación de coordenadas. |

*(Ampliación — Ejercicios prácticos Unidad 3-1 GeoServer y Unidad 3 conexiones QGIS)*

| **OGC API** | Nuevo estándar OGC (en desarrollo), evolución del WFS, que permite acceder a datos geoespaciales en formato web (HTML y/o JSON) mediante "puntos finales" (endpoints) añadidos a la URL, siguiendo las mejores prácticas W3C/OGC. |
| **Landing page** | Punto final genérico (`/`) de acceso a una OGC API, desde el que se enlaza a las colecciones de datos, la definición de la API y la declaración de conformidad. |
| **Collections (OGC API)** | Punto final (`/collections`) de una OGC API que da acceso a los datos propiamente dichos, organizados por colecciones temáticas. |
| **JDK (Java Development Kit)** | Entorno de desarrollo Java requerido para ejecutar GeoServer; las versiones recientes de GeoServer (desde la 2.25) requieren JDK 17. |
| **Jetty** | Servidor de aplicaciones Java ligero y portátil sobre el que está construida la versión binaria independiente de plataforma de GeoServer. |
| **GEOSERVER_HOME** | Variable de entorno que apunta al directorio de instalación de GeoServer. |
| **GEOSERVER_DATA_DIR** | Variable de entorno que apunta al directorio de datos de GeoServer (`data_dir`), donde se almacena toda la configuración: workspaces, estilos, capas, caché de teselas, etc. |
| **data_dir** | Directorio de datos de GeoServer; contiene, entre otras, las carpetas `workspaces/`, `styles/`, `layergroups/`, `gwc/`, `www/` y `logs/`. Debe copiarse fuera del directorio de instalación antes de actualizar o reinstalar GeoServer para no perder la configuración. |
| **Content Security Policy (CSP)** | Página de configuración de GeoServer que controla las cabeceras HTTP de política de seguridad de contenido; conviene deshabilitarla en entornos de desarrollo para poder referenciar librerías externas (Leaflet, OpenStreetMap) por URL sin bloqueos. |
| **CSS Styling (extensión GeoServer)** | Complemento de GeoServer que añade un editor de estilos alternativo al SLD, basado en una sintaxis derivada de CSS; los estilos CSS se convierten internamente a SLD. |
| **symbol()** | Función de la sintaxis CSS de GeoServer que permite usar marcas predefinidas (circle, square, triangle, arrow, cross, star…) sin necesidad de un editor de imágenes. |
| **CQL (Common Query Language)** | Lenguaje de consulta usado en los filtros de estilos de GeoServer (ej. en CSS, expresiones entre corchetes como `[pop_max < 1000000]`) para condicionar reglas de estilo según atributos. |
| **@scale** | Operador de la sintaxis CSS de GeoServer que permite condicionar un estilo según el nivel de escala/zoom del mapa. |
| **SLD Cookbook / CSS Cookbook** | Colecciones de recetas de estilo (SLD y CSS respectivamente) publicadas en la documentación de GeoServer, con ejemplos para puntos, líneas y polígonos. |
| **Teselas vectoriales (Vector Tiles)** | Formato de salida (no de origen) que contiene datos vectoriales georreferenciados recortados en teselas; a diferencia de las teselas de imagen, el estilo se renderiza en el cliente y no en el servidor. Estándar abierto bajo licencia Creative Commons Attribution 3.0 US. |
| **MVT (MapBox Vector Tile)** | Formato binario de teselas vectoriales (`application/vnd.mapbox-vector-tile`), el más recomendado en producción y ampliamente soportado. |
| **TopoJSON** | Formato JSON de teselas vectoriales (`application/json;type=topojson`) que admite topología, útil para coberturas de tipo polígono; poco soportado fuera de OpenLayers. |
| **GeoWebCache (teselas vectoriales)** | Módulo integrado con GeoServer que gestiona la generación y publicación de teselas (de imagen y vectoriales); para teselas vectoriales solo necesita almacenar una tesela una vez para todos los estilos diferentes. |
| **WMS en cascada** | Almacén de datos de GeoServer que permite servir un servicio WMS externo como si fuera local, con la limitación de no poder modificar su estilo. |

*(Ampliación — Unidad 4: El caché de mapas, GeoWebCache)*

| **Tile Proxying** | Modo de funcionamiento de GeoWebCache: actúa como proxy entre los clientes y uno o varios servidores WMS, interceptando las peticiones para servir la imagen desde caché si ya existe, o solicitarla al WMS y cachearla si no existe. |
| **Map tiling (generación de teselas)** | Forma en que las imágenes de un mapa son pre-renderizadas y guardadas en la memoria caché: en lugar de almacenar la imagen entera, se guarda como pequeñas imágenes rectangulares del mismo tamaño (teselas) que se combinan para formar el mapa completo, en varios niveles de resolución/zoom. |
| **Seeding / Pregeneración de teselas** | Estrategia de generación de teselas en la que se generan y almacenan en caché todas las teselas deseadas antes de que el cliente realice una solicitud; evita tiempos de espera para el usuario a costa de tiempo de planificación, computación y espacio en disco. |
| **Bajo demanda (creación de teselas)** | Estrategia de generación de teselas en la que las teselas se almacenan en caché a medida que son solicitadas durante la navegación por el mapa; no requiere proceso previo pero la velocidad de visualización es variable para el primer usuario que solicita cada área. |
| **Reseed** | Tipo de operación de una tarea de GeoWebCache que genera (o regenera) todos los *tiles* del área y niveles de zoom especificados. |
| **Seeds (operación)** | Tipo de operación de una tarea de GeoWebCache que llena únicamente los huecos donde no existen *tiles*, sin regenerar los ya existentes. |
| **Truncate** | Tipo de operación de una tarea de GeoWebCache que vacía la memoria caché de una capa. |
| **Cuota de disco (Disk Quota)** | Configuración de GeoServer/GeoWebCache que permite habilitar límites de almacenamiento para la caché de teselas y definir la política de invalidación (ej. eliminar primero las teselas menos frecuentemente utilizadas) cuando se supera el tamaño máximo establecido. |
| **Google Earth** | Visor de mapas 3D de Google; GeoServer se integra con él proporcionando salida nativa en KML, permitiendo cargar cualquier capa servida por GeoServer (incluyendo grupos de capas cacheados) dentro de Google Earth. |
| **Enlace de red (Network Link)** | Mecanismo de Google Earth que conecta la aplicación a un recurso KML remoto (por ejemplo, servido por GeoWebCache/GeoServer), permitiendo que la vista se actualice dinámicamente en lugar de cargar un archivo KML estático. |

*(Ampliación — Unidad 5 y 5-1: Personalización de aplicaciones web de mapas y Leaflet)*

| **HTML (HyperText Markup Language)** | Lenguaje de marcado que define la estructura y el contenido de una página web mediante etiquetas (tags); es el "esqueleto" de una aplicación web de mapas. |
| **HTML5** | Última versión mayor de HTML; incorpora nuevas etiquetas semánticas y elimina la necesidad de declarar tipo/versión en el doctype. |
| **CSS (Cascading Style Sheets)** | Lenguaje de hojas de estilo que define la presentación visual (colores, tamaños, posiciones) de los elementos HTML; puede aplicarse en línea, embebido en el `<head>` o en archivo externo enlazado. |
| **JavaScript (JS)** | Lenguaje de programación interpretado que añade comportamiento e interactividad a una página web; es el lenguaje sobre el que se construyen las librerías de mapas web como Leaflet y OpenLayers. |
| **DOM (Document Object Model)** | Representación en forma de árbol de los elementos de una página HTML que JavaScript puede leer y modificar dinámicamente. |
| **Etiqueta `<iframe>`** | Elemento HTML que permite embeber una página o documento web dentro de otra página. |
| **CDN (Content Delivery Network)** | Red de servidores distribuida desde la que se puede enlazar directamente una librería (como Leaflet) sin necesidad de descargarla, mediante una etiqueta `<link>` (CSS) o `<script>` (JS) con su URL. |
| **AJAX (Asynchronous JavaScript And XML)** | Técnica que permite a una página web solicitar datos a un servidor de forma asíncrona (sin recargar la página), usada habitualmente para consumir servicios WFS/GetFeature desde Leaflet. |
| **jQuery** | Librería de JavaScript que simplifica la manipulación del DOM, el manejo de eventos y las peticiones AJAX. |
| **Consola de errores / DevTools** | Herramientas de depuración integradas en el navegador (Firefox: Consola de errores; Chrome: DevTools, con pestañas Elements/Console/Sources) que permiten identificar errores de sintaxis o de ejecución en HTML/CSS/JS, incluyendo errores por sensibilidad a mayúsculas/minúsculas (ej. `Ol.layer.Tile` vs `ol.layer.Tile`). |
| **Leaflet** | Librería JavaScript open source (desde 2011) para construir mapas interactivos en la web, orientada a la sencillez, el buen rendimiento en móviles y la extensibilidad mediante plugins. |
| **L.map()** | Método de Leaflet que crea el objeto mapa, asociándolo a un `<div>` del DOM y a un conjunto de opciones (centro, zoom, capas, controles, etc.). |
| **L.tileLayer()** | Método de Leaflet que añade una capa de teselas ráster (ej. OpenStreetMap, MapBox) al mapa a partir de una plantilla de URL. |
| **L.tileLayer.wms()** | Método de Leaflet que añade una capa de teselas generadas dinámicamente por un servicio WMS externo (ej. GeoServer). |
| **L.imageOverlay()** | Método de Leaflet que superpone una imagen estática georreferenciada (por sus esquinas) sobre el mapa. |
| **L.marker()** | Método de Leaflet que añade un marcador puntual al mapa en una coordenada dada. |
| **L.icon()** | Método de Leaflet que define un icono personalizado (imagen, tamaño, anclaje) para asignar a un `L.marker`. |
| **L.popup()** | Método de Leaflet que muestra una ventana emergente de contenido (HTML) anclada a una coordenada o a una capa, normalmente al hacer clic. |
| **L.tooltip()** | Método de Leaflet que muestra una etiqueta de texto asociada a una capa, normalmente al pasar el cursor (hover). |
| **Path (Leaflet)** | Clase abstracta base de Leaflet de la que heredan las capas vectoriales (`Polyline`, `Polygon`, `Rectangle`, `Circle`, `CircleMarker`), con opciones comunes de estilo (color, weight, opacity, fill) y eventos. |
| **L.polyline()** | Método de Leaflet que dibuja una línea a partir de una serie de coordenadas. |
| **L.polygon()** | Método de Leaflet que dibuja un polígono cerrado a partir de una serie de coordenadas. |
| **L.rectangle()** | Método de Leaflet que dibuja un rectángulo a partir de sus esquinas (bounding box). |
| **L.circle()** | Método de Leaflet que dibuja un círculo con radio en metros, definido geográficamente (se deforma con el zoom en proyecciones no equidistantes). |
| **L.circleMarker()** | Método de Leaflet que dibuja un círculo con radio en píxeles, de tamaño constante independiente del zoom. |
| **SVG / Canvas (renderers de Leaflet)** | Motores de renderizado de las capas vectoriales de Leaflet; SVG ofrece mejor interactividad y calidad, Canvas mejor rendimiento con grandes volúmenes de datos. |
| **L.layerGroup()** | Método de Leaflet que agrupa varias capas para manipularlas (añadir/quitar del mapa) como un conjunto único, sin gestión de eventos propia. |
| **L.featureGroup()** | Método de Leaflet similar a `L.layerGroup` pero que además propaga eventos del grupo y permite aplicar estilos comunes con `setStyle()`. |
| **L.geoJson()** | Método de Leaflet que crea una capa a partir de datos en formato GeoJSON, con opciones como `pointToLayer`, `style`, `onEachFeature`, `filter` y `coordsToLatLng` para personalizar su representación (ej. mapas de coropletas). |
| **Mapa de coropletas (choropleth)** | Mapa temático que colorea polígonos según el valor de un atributo, típicamente construido en Leaflet combinando `L.geoJson()` con una función de estilo basada en rangos de color. |
| **ColorBrewer** | Herramienta/paleta de esquemas de color diseñados para cartografía temática (secuenciales, divergentes, cualitativos), usada habitualmente para definir los colores de un mapa de coropletas. |
| **L.gridLayer()** | Clase base de Leaflet para crear capas de teselas personalizadas (de la que hereda `L.tileLayer`). |
| **L.control()** | Método base de Leaflet para crear controles de interfaz de usuario sobre el mapa (zoom, atribución, capas, escala), posicionables en las esquinas del contenedor. |
| **L.control.zoom()** | Control de Leaflet que añade los botones de acercar/alejar zoom al mapa. |
| **L.control.attribution()** | Control de Leaflet que muestra el texto de atribución/copyright de las fuentes de datos. |
| **L.control.layers()** | Control de Leaflet que permite alternar entre capas base y activar/desactivar capas superpuestas (overlays). |
| **L.control.scale()** | Control de Leaflet que muestra una barra de escala gráfica (métrica y/o imperial). |
| **Eventos (Leaflet)** | Mecanismo mediante `map.on()`/`layer.on()` (y `off()` para eliminarlos) que permite ejecutar funciones en respuesta a interacciones del usuario (click, zoom, moveend, etc.), recibiendo un objeto evento (ej. `e.latlng`). |
| **Plugin (Leaflet)** | Extensión de funcionalidad de Leaflet desarrollada por la comunidad, incorporable vía CDN o descarga (ej. `Leaflet.Search` para añadir un buscador de lugares/capas al mapa). |
| **MapBox** | Plataforma de mapas que ofrece, entre otros servicios, estilos de teselas (tile styles) personalizables consumibles en Leaflet/OpenLayers mediante un token de acceso. |

*(Ampliación — Unidad 6: OpenLayers)*

| **OpenLayers** | Librería JavaScript open source de alto nivel (desde 2006, proyecto OSGeo) para construir mapas interactivos y aplicaciones webmapping, con gran flexibilidad de capas, formatos, estilos y proyecciones. |
| **POO (Programación orientada a objetos)** | Paradigma de programación en el que se definen clases (plantillas de propiedades/métodos) de las que se crean instancias (objetos concretos); OpenLayers está construido íntegramente sobre este paradigma (`ol.Map`, `ol.View`, `ol.layer.*`, etc.). |
| **npm (Node Package Manager)** | Gestor de paquetes de Node.js, usado para instalar OpenLayers como dependencia de un proyecto (`npm install ol`) y para ejecutar los scripts de desarrollo/compilación del proyecto. |
| **Node.js** | Entorno de ejecución de JavaScript fuera del navegador, necesario para usar `npm` y herramientas de compilación como Vite; prerrequisito para crear un proyecto OpenLayers con `npm create ol-app`. |
| **Vite** | Herramienta moderna de compilación y servidor de desarrollo usada por `npm create ol-app` para los proyectos OpenLayers basados en npm; ofrece recarga en caliente y generación de una versión de producción optimizada (`npm run build`). |
| **Tree-shaking** | Técnica de optimización de los bundlers (como Vite/Webpack) que elimina del resultado final el código de las clases/módulos importados que no se llegan a usar realmente en la aplicación. |
| **ol.Map** | Clase central de OpenLayers que representa el mapa; agrupa las capas, la vista, los controles y las interacciones, y se asocia a un `<div>` del DOM mediante la propiedad `target`. |
| **ol.View** | Clase de OpenLayers que define el estado de visualización del mapa: centro, zoom, proyección y rotación; puede manejarse como un objeto independiente del mapa. |
| **ol.proj.fromLonLat()** | Función de utilidad de OpenLayers que convierte coordenadas geográficas (longitud/latitud, EPSG:4326) a la proyección del mapa (por defecto EPSG:3857, Web Mercator). |
| **Motor de renderizado (Canvas / DOM / WebGL)** | Mecanismo interno que usa OpenLayers para dibujar el mapa en el navegador; Canvas es el motor por defecto, DOM es el heredado de versiones antiguas y WebGL aprovecha la GPU para grandes volúmenes de datos. |
| **ol.layer.Tile** | Clase de capa de OpenLayers que muestra datos raster organizados en teselas (tiles), habitualmente asociada a fuentes como `ol.source.OSM`, `ol.source.TileWMS` o `ol.source.BingMaps`. |
| **ol.layer.Image** | Clase de capa de OpenLayers que muestra una única imagen completa (no teselada) que cubre la extensión visible; usada con `ol.source.ImageWMS` o `ol.source.ImageStatic`. |
| **ol.layer.Vector** | Clase de capa de OpenLayers que muestra objetos geográficos vectoriales estilizados en el cliente, a partir de una fuente `ol.source.Vector`. |
| **ol.layer.VectorTile** | Clase de capa de OpenLayers que combina teselado y datos vectoriales, habitualmente usada para consumir teselas en formato MVT. |
| **ol.layer.Heatmap** | Clase de capa de OpenLayers que representa una capa vectorial de puntos como un mapa de calor (densidad), configurable mediante `gradient`, `weight`, `radius`, `blur` y `shadow`. |
| **ol.layer.Group** | Clase de OpenLayers que agrupa varias capas (o grupos) bajo un mismo nodo, usada por ejemplo por el plugin `ol-layerswitcher` para organizar capas base y superpuestas. |
| **ol.source.OSM** | Fuente de OpenLayers que sirve la capa base de OpenStreetMap sin necesidad de configuración adicional. |
| **ol.source.TileWMS** | Fuente de OpenLayers que consume un servicio WMS de forma teselada (peticiones GetMap recortadas en teselas). |
| **ol.source.ImageWMS** | Fuente de OpenLayers que consume un servicio WMS solicitando una única imagen no teselada, recalculada al desplazar o hacer zoom. |
| **ol.source.ImageStatic** | Fuente de OpenLayers que muestra una imagen estática ya georreferenciada mediante su extensión y proyección. |
| **ol.source.BingMaps** | Fuente de OpenLayers que consume las capas base de Bing Maps mediante una clave de API. |
| **ol.source.Vector** | Fuente de OpenLayers que almacena y gestiona objetos geográficos (`ol.Feature`) para una capa vectorial, con métodos como `addFeature`, `clear`, `getFeatures`, `getFeaturesAtCoordinate`, `removeFeature`, `getExtent` y `forEachFeature`. |
| **ol.source.VectorTile** | Fuente de OpenLayers usada por `ol.layer.VectorTile` para consumir teselas vectoriales (habitualmente en formato MVT). |
| **ol.format.GeoJSON / KML / GML / MVT** | Clases del paquete `ol.format` que indican a `ol.source.Vector`/`ol.source.VectorTile` cómo interpretar (parsear) los datos leídos, según el formato de origen. |
| **ol.style.Style** | Clase de OpenLayers que agrupa los distintos componentes de estilo (`fill`, `stroke`, `image`, `text`) aplicables a un objeto geográfico. |
| **ol.style.Fill** | Componente de estilo de OpenLayers que define el color de relleno de polígonos y símbolos puntuales tipo círculo. |
| **ol.style.Stroke** | Componente de estilo de OpenLayers que define el color y grosor del trazo/borde de líneas y polígonos. |
| **ol.style.Circle** | Componente de estilo de OpenLayers que representa un punto como un símbolo circular, con `fill` y `stroke` propios. |
| **ol.style.Icon** | Componente de estilo de OpenLayers que representa un punto mediante una imagen externa (icono). |
| **ol.style.Text** | Componente de estilo de OpenLayers que añade una etiqueta de texto asociada a cualquier geometría. |
| **StyleFunction (función de estilo)** | Función que, en lugar de un estilo fijo, recibe cada `feature` (y la resolución del mapa) y devuelve dinámicamente el `ol.style.Style` a aplicar, permitiendo estilos condicionados por atributos o por zoom. |
| **declutter** | Propiedad de OpenLayers (capa vectorial) que evita la superposición de etiquetas de texto cuando hay muchos objetos próximos, ocultando automáticamente las que no caben sin solaparse. |
| **ol.control (concepto)** | Elemento de interfaz de usuario (widget) superpuesto al mapa con el que el usuario interactúa mediante clic (zoom, atribución, capas, escala...), a diferencia de las interacciones. |
| **ol.control.defaults().extend()** | Patrón de OpenLayers que permite partir de los controles por defecto del mapa (Zoom, Attribution, Rotate) y añadir otros controles adicionales sin sustituir la lista completa. |
| **ol.control.FullScreen** | Control de OpenLayers que añade un botón para mostrar el mapa en pantalla completa. |
| **ol.control.MousePosition** | Control de OpenLayers que muestra la coordenada del ratón sobre el mapa en tiempo real. |
| **ol.control.OverviewMap** | Control de OpenLayers que muestra un mapa de situación en miniatura (minimapa). |
| **ol.control.ScaleLine** | Control de OpenLayers que muestra una barra de escala gráfica. |
| **ol.control.ZoomSlider** | Control de OpenLayers que añade un control deslizante (slider) para el zoom, alternativo a los botones. |
| **ol.control.ZoomToExtent** | Control de OpenLayers que añade un botón para restablecer la vista a una extensión predefinida. |
| **ol.interaction (concepto)** | Mecanismo de OpenLayers que gestiona el comportamiento del mapa en respuesta a gestos del usuario directamente sobre el lienzo (arrastrar, rueda del ratón, pellizco), a diferencia de los controles. |
| **ol.interaction.DragBox** | Interacción de OpenLayers que permite dibujar un rectángulo de selección arrastrando el ratón. |
| **ol.interaction.DragAndDrop** | Interacción de OpenLayers que permite cargar archivos (GeoJSON, KML...) arrastrándolos sobre el mapa. |
| **ol.interaction.Select** | Interacción de OpenLayers que selecciona objetos geográficos al hacer clic (u otro evento) sobre ellos, configurable mediante `style`, `layers`, `condition`, `toggleCondition`, `addCondition` y `removeCondition`. |
| **ol.interaction.Draw** | Interacción de OpenLayers que permite dibujar nuevas geometrías sobre el mapa, configurada mediante `type` (tipo de geometría) y `source` (fuente vectorial de destino). |
| **ol.interaction.Modify** | Interacción de OpenLayers que permite editar los vértices de geometrías existentes, habitualmente combinada con `ol.interaction.Select` mediante la propiedad `features`. |
| **ol-layerswitcher** | Plugin de terceros (Matt Walker) para OpenLayers que añade un control de tipo árbol de capas para gestionar la visibilidad de capas base y superpuestas, apoyado en `ol.layer.Group`. |
| **CORS (Cross-Origin Resource Sharing)** | Mecanismo de seguridad del navegador que restringe las peticiones entre distintos orígenes; en GeoServer se habilita editando el filtro `CorsFilter` (comentado por defecto) en el archivo `web.xml`. |
| **web.xml (GeoServer)** | Archivo de configuración de la aplicación web de GeoServer (dentro de `WEB-INF`) donde se activa, entre otras cosas, el filtro CORS necesario para que aplicaciones OpenLayers de otro origen consuman sus servicios WMS/WFS. |
| **Git** | Sistema de control de versiones distribuido; prerrequisito de `npm create ol-app`, ya que algunas plantillas y dependencias se gestionan mediante repositorios Git. |
| **Git Bash** | Terminal (emulador de línea de comandos) incluida en la instalación de Git para Windows, usada para verificar la instalación (`git --version`) y ejecutar comandos Git. |
| **cql_filter / CQL_FILTER** | Parámetro usado en peticiones WMS/WFS (y en `params` de `ol.source.TileWMS`/`ImageWMS`) para filtrar los objetos geográficos devueltos según una expresión CQL sobre sus atributos. |

*(Ampliación — Unidad 7: MapStore)*

| **MapStore** | *Framework webGIS* de código libre (licencia GNU/GPL3) desarrollado por GeoSolutions, que permite crear, gestionar y compartir mapas, así como construir aplicaciones geoespaciales sofisticadas; se apoya en OpenLayers (escritorio), Leaflet (móvil), Cesium (3D) y React (interfaz). |
| **GeoSolutions** | Empresa desarrolladora de MapStore, GeoServer y GeoWebCache, especializada en software geoespacial de código abierto. |
| **MapManager** | Módulo/aplicación de MapStore orientado a administrar mapas. |
| **MapComposer** | Módulo/aplicación de MapStore orientado a crear mapas. |
| **MapViewer** | Módulo/aplicación WebGIS de MapStore con funciones de geolocalizador y análisis de datos. |
| **Explorador de metadatos** | Componente de MapStore que actúa como cliente CSW (Catalogue Service for the Web) para explorar metadatos de servicios. |
| **Gestor de usuarios (MapStore)** | Componente de MapStore para crear y gestionar usuarios, grupos y roles (Anónimo, Normal, Administrador). |
| **Gestor de mapas (MapStore)** | Herramienta principal de MapStore para crear, visualizar y trabajar con mapas; incluye barra de menú, tabla de contenidos, barra lateral, selector de mapas de fondo y control de pie de página. |
| **Gestor de contexto (MapStore)** | Herramienta administrativa de MapStore para construir y configurar visores personalizados (nombre del contexto, configuración predeterminada del mapa y complementos disponibles para el espectador). |
| **Panel de control / Dashboard (MapStore)** | Área de trabajo de MapStore para crear una presentación combinando widgets: vistas de mapa, leyendas, textos, tablas, gráficos y contadores. |
| **Widget (MapStore)** | Gráfico, tabla, texto o contador generado por MapStore a partir de los datos de una capa del mapa; sus datos se sincronizan con el área visible del mapa. |
| **StoryMap / Stories (MapStore)** | Herramienta de MapStore que permite crear historias o presentaciones dinámicas combinando elementos cartográficos con recursos multimedia (texto, vídeo, fotografía). |
| **Tabla de contenidos (MapStore)** | Panel de gestión de capas de MapStore desde el que se configuran, filtran, eliminan y exportan las capas del mapa, y se crean widgets. |
| **Catálogo (MapStore)** | Herramienta de MapStore para conectar y añadir al mapa servicios OGC (WMS, WFS, CSW, WMTS) de un servidor como GeoServer. |
| **Anotaciones (MapStore)** | Herramienta de MapStore para dibujar geometrías (marcadores, líneas, polígonos, textos, círculos) directamente sobre el mapa, con posibilidad de exportarlas. |
| **Vidrio espía (MapStore)** | Herramienta de comparación de capas con forma de círculo que muestra/oculta los elementos de una capa según la posición del cursor. |
| **Golpe fuerte (MapStore)** | Herramienta de comparación de capas que traza una línea (vertical u horizontal) sobre el mapa, ocultando los elementos de la capa a un lado y mostrándolos al otro. |
| **Nominatim** | Base de datos de geocodificación de OpenStreetMap utilizada por MapStore (y otros clientes) para búsquedas de ubicación y direcciones. |
| **Geoprocesamiento (MapStore)** | Complemento de MapStore que utiliza procesos WPS para realizar operaciones de buffer e intersección sobre las geometrías de una capa del mapa. |
| **Contexto de aplicación (MapStore)** | Configuración personalizada de un visor MapStore (mapa, capas, complementos y tema) creada con el Gestor de contexto, accesible mediante una URL específica. |
| **Complemento / Plugin (MapStore)** | Módulo funcional que se puede habilitar o deshabilitar en un contexto de MapStore (ej. Catálogo, Geoprocesamiento, Anotaciones, Medida, Importar, Exportación de mapas). |
| **Geohistoria (MapStore)** | Recurso de MapStore (creado desde "Agregar recurso") asociado a las Stories/StoryMap, para presentaciones dinámicas con mapas y contenido multimedia. |
| **L.geoJson()** | Clase de Leaflet que permite representar en el mapa un objeto o archivo en formato GeoJSON (como el exportado desde las anotaciones de MapStore), aceptando las opciones `style` y `onEachFeature`. |

*(Ampliación — Unidad 8: Consideraciones finales y recomendaciones)*

| **Entornos de desarrollo, pruebas y producción** | Las tres fases por las que pasa el despliegue de una aplicación web mapping: desarrollo (construcción de la aplicación), pruebas (*testing*, para detectar y corregir fallos) y producción (entorno final, ya publicado en la web). |
| **deegree** | Software libre alternativo a GeoServer para publicar servicios OGC (WMS, WFS, WCS...) de datos geoespaciales. |
| **gvSIG** | Software SIG de escritorio libre, alternativo a QGIS. |
| **TileCache** | Software libre alternativo a GeoWebCache para el almacenamiento en caché de teselas de mapas web. |
| **J2EE (Java 2 Enterprise Edition)** | Plataforma Java para el desarrollo de aplicaciones empresariales; en la arquitectura de ejemplo del curso, un servidor de aplicaciones J2EE se sitúa entre el cliente (OpenLayers) y GeoServer/Oracle. |
| **LATIN1** | Codificación de caracteres (ISO 8859-1) que debe indicarse al importar shapefiles a PostGIS cuando el archivo de origen no está codificado en UTF-8, para evitar problemas con tildes y caracteres especiales. |
| **Confederación Hidrográfica del Duero** | Organismo público español de gestión hidrográfica; entidad ficticia cliente en el enunciado del proyecto final del curso, que solicita migrar su visor cartográfico privativo a una solución open source con PostGIS, GeoServer y Leaflet. |
