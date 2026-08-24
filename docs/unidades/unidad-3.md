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

**Ejercicios prácticos de esta unidad:** [ver ejercicios →](../ejercicios/ejercicio-3.md)

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

**Ejercicios prácticos de esta unidad:** [ver ejercicios →](../ejercicios/ejercicio-3.md)

---

