# Unidad 2. Bases de datos espaciales. PostGIS 3 (Introducción)

### Resumen estructurado

**1. La base de datos PostgreSQL**
- Sistema de gestión de bases de datos objeto-relacional.
- Distribuido bajo licencia BSD (*Berkeley Software Distribution*), con código fuente disponible libremente.
- Es el sistema de gestión de bases de datos de código abierto más potente del mercado; en sus últimas versiones no tiene nada que envidiarle a otras bases de datos comerciales.
- Se puede extender para adaptarse a distintos objetivos.

*¿Por qué elegir PostgreSQL?* Fiabilidad probada e integridad transaccional por defecto (ACID); soporte para estándares SQL (full SQL92); extensiones y funciones fácilmente integrables orientadas a una comunidad de desarrollo; sin límite en el tamaño de columnas (apoya grandes objetos SIG); estructura de índice genérico (GiST) que permite índices R-Tree; fácil añadir funciones personalizadas.

**2. ¿Por qué usar una base de datos espacial y no shapefiles?**
Los *shapefiles* han sido la forma estándar de almacenar datos espaciales, pero como archivos "planos" tienen desventajas:
- Requieren software especial para leer/escribir.
- Usuarios concurrentes pueden corromperlos.
- Preguntas complicadas requieren software complicado para responderlas.

**3. El componente espacial: PostGIS**
PostGIS = PostgreSQL + extensión espacial → **base de datos espacial**.
- Permite el uso de objetos GIS; incluye soporte para índices GiST basados en R-Tree y funciones básicas de análisis de objetos GIS.
- Totalmente compatible con OGC. Aunque a nivel general su uso no está tan extendido como MySQL, dentro del sector GIS su uso es casi canónico.

**Arquitectura típica (open source):**
- **Interfaz de usuario:** Leaflet, OpenLayers, QGIS
- **Servidor web:** GeoServer + GeoWebCache
- **Base de datos:** PostGIS

**4. ¿Qué es una base de datos espacial?**
Una base de datos espacial es una base de datos optimizada para almacenar y consultar datos que representan objetos definidos en un espacio geométrico. Factores que permiten que los objetos espaciales existan de forma nativa:
- **Tipos de datos espaciales:** almacenan formas (*shapes*) como puntos, líneas y polígonos en columnas de geometría.
- **Funciones espaciales:** en lenguaje SQL, consultan propiedades y relaciones espaciales.
- **Índices espaciales multidimensionales:** procesamiento eficiente de operaciones espaciales.

*Tipos de datos espaciales:* POINT, LINESTRING, POLYGON, COLLECTION y sus variantes MULTI* (MULTIPOINT, MULTILINESTRING, MULTIPOLYGON) — representación binaria de *shapes* en una fila de la BD (con localización).

*Jerarquía de tipos (superclase → subclases):*
- Superclase: `ST_Geometry`
- Subclases: `ST_Point`, `ST_Curve` (→ `ST_LineString`), `ST_Surface` (→ `ST_Polygon`), `ST_GeometryCollection` (→ `ST_MultiPoint`, `ST_MultiCurve` → `ST_MultiLineString`, `ST_MultiSurface` → `ST_MultiPolygon`)

**5. Índices espaciales**
- El orden natural de números, cadenas y fechas es fácil de determinar (menor/mayor/igual). Pero los polígonos pueden solaparse, estar contenidos unos en otros y estar dispuestos en 2+ dimensiones, por lo que un B-tree no puede indexarlos eficientemente.
- Los **índices espaciales multidimensionales** se usan para el procesamiento eficiente de operaciones espaciales.
- Funcionan calculando y comparando el **bounding box** (cuadro delimitador) de cada elemento geográfico: el rectángulo de tamaño más pequeño capaz de contener un elemento geográfico dado. Incluso polígonos complejos y cadenas lineales pueden representarse por un bounding box simple.

**6. Funciones espaciales — clasificación**
Las funciones sirven para manipular datos durante una consulta. Una BD espacial proporciona funciones para el análisis de componentes geométricos (relaciones espaciales y manipulación de geometrías), agrupadas en 5 categorías (definidas por la OGC SFSQL):

| Categoría | Ejemplo |
|---|---|
| **Administración** | Crear columna de geometría: `AddGeometryColumn()`; actualizar columnas existentes: `Populate_Geometry_Columns()` |
| **Conversión** | Texto de un punto: `ST_AsText()`; texto → geometría PostGIS: `ST_GeomFromText()` |
| **Recuperación** | ¿Cuánto mide esta línea? `ST_Length()`; perímetro: `ST_Perimeter()` |
| **Comparación** | ¿Se tocan? `ST_Touches()`; ¿está contenido? `ST_Contains()` |
| **Generación** | Zona de exclusión: `ST_Buffer()`; unir geometrías: `ST_Union()` |

**7. Normativa**
- La **OGC** (*Open Geospatial Consortium*) definió un esquema SQL que soporta acceso, almacenamiento, consulta y actualización de fenómenos geoespaciales simples: **"OpenGIS Simple Features Implementation Specification for SQL. Version 1.1"** (SFS1.1, de 1999).
- Especificaciones relacionadas: SFA 1.1.0, SFA 1.2.1, SQL/MM.
- **PostGIS se apoya principalmente en SFS1.1.**

**8. Objetos GIS**
- PostGIS soporta todos los tipos de vectores definidos en "*Simple Features for SQL 1.2.1*" (OGC) y el documento ISO "*SQL/MM Part 3: Spatial*".
- Además soporta el **tipo raster** (sin normas formales a seguir) y un modelo de **topología** (sigue un borrador ISO aún no publicado).
- Los estándares OGC e ISO definen variantes 2D (x/y), 3D (x/y/z, x/y/m) y 4D (x/y/z/m) de puntos, líneas, polígonos, elementos curvos, poliedros y TINs.

**Representaciones WKB y WKT:** ambas incluyen tipo de objeto y coordenadas. Ejemplos WKT: `POINT(0 0)`, `LINESTRING(0 0,1 1,1 2)`, `POLYGON(...)`, `MULTIPOINT(...)`, `MULTILINESTRING(...)`, `MULTIPOLYGON(...)`, `GEOMETRYCOLLECTION(...)`.

- La especificación OpenGIS requiere que el formato interno de almacenamiento incluya un **SRID** (identificador de sistema de referencia espacial), obligatorio al crear objetos espaciales:
  ```sql
  INSERT INTO geotable (geom, name)
  VALUES ( ST_GeomFromText('POINT(-126.4 45.32)', 312), 'A Place');
  ```

**EWKB, EWKT y formas canónicas:**
- Los formatos OGC solo admiten geometrías 2D y el SRID *nunca* se incrusta en la representación de entrada/salida.
- PostGIS define formatos extendidos (superconjunto de OGC): **EWKT** y **EWKB**, que añaden soporte para coordenadas 3dm, 3dz, 4d, e incrustación del SRID.
  - Ejemplos EWKT: `POINT(0 0 0)` (XYZ), `SRID=32632;POINT(0 0)` (XY con SRID), `POINTM(0 0 0)` (XYM), `POINT(0 0 0 0)` (XYZM).
  ```sql
  INSERT INTO geotable ( geom, name )
  VALUES ( ST_GeomFromEWKT('SRID=312;POINTM(-126.4 45.32 15)'), 'A Place' );
  ```

**SQL-MM Part 3:** la especificación *SQL Multimedia Applications Spatial* amplía la especificación de elementos simples definiendo curvas circularmente interpoladas (incluye 3dm/3dz/4d, pero no SRID). Ejemplos: `CIRCULARSTRING(...)`, `COMPOUNDCURVE(...)`, `CURVEPOLYGON(...)`, `MULTICURVE(...)`, `MULTISURFACE(...)`. Las extensiones WKT para curvas aún no son totalmente compatibles.

**9. Clientes SQL**
- **Cliente de texto:** `psql` (línea de comandos).
- **Cliente gráfico:** `pgAdmin 4` — más amigable; tiene apariencia de aplicación de escritorio con interfaz gráfica, herramienta de consultas SQL, depurador de código, etc. Incluye: creador de consultas SQL, ventana para escribir consultas, panel de manipulación de objetos de la BD y visor del objeto seleccionado.

**10. Enlaces de interés**
- PostGIS: https://postgis.net/ — Docs: https://postgis.net/documentation/
- PostgreSQL: https://www.postgresql.org/ — Docs: https://www.postgresql.org/docs/
- PgAdmin: https://www.pgadmin.org/

---

## Unidad 2-1. Gestión de datos en PostGIS

### Resumen estructurado

**1. Estándares OpenGIS**
- La norma **"Simple Features Specification for SQL" (SFSQL)** de OpenGIS define los tipos estándar de los objetos GIS, las funciones para manipularlos y un conjunto de tablas de metadatos.
- Para mantener los metadatos consistentes, operaciones como crear/eliminar una columna espacial se hacen mediante procedimientos especiales definidos por OpenGIS.
- Dos tablas/vistas de metadatos OpenGIS incluidas en PostGIS (conformes a la OGC):
  - **`spatial_ref_sys`**: enumera ~3.000 sistemas de referencia espacial conocidos y los detalles para transformar/reproyectar entre ellos. Columnas clave: `srid`, `auth_name` (ej. "EPSG"), `auth_srid` (código EPSG), `srtext` (WKT del SRS), `proj4text` (cadena Proj4 usada por PostGIS para transformar coordenadas).
    - SRS comunes: 4326 (WGS84 Lat/Long), 4269 (NAD83 Lat/Long), 3395 (WGS84 Mercator Mundial), 2163 (US National Atlas Equal Area).
    - Las zonas UTM son las más idóneas para mediciones, pero cada una solo cubre 6 grados de longitud.
    - Si un SRS no está en la tabla, se pueden definir proyecciones propias con construcciones **Proj4** (recurso: spatialreference.org).
  - **`geometry_columns`** (vista): documenta qué tablas/columnas tienen geometría. Columnas: `f_table_catalog`, `f_table_schema`, `f_table_name` (tabla), `f_geometry_column` (columna), `coord_dimension` (2, 3 o 4), `srid`, `type` (POINT, MULTIPOLYGON, etc.).

**2. Tipos de geometrías (representación WKT)**
- POINT, LINESTRING, POLYGON, MULTIPOINT, MULTILINESTRING, MULTIPOLYGON, GEOMETRYCOLLECTION.
- SFSQL solo maneja 2 dimensiones; PostGIS extiende a 3 y 4 dimensiones.
- Funciones de metadatos de geometría: `ST_GeometryType()`, `ST_NDims()`, `ST_SRID()`.

**3. Formatos de entrada/salida de geometrías** (PostGIS emite y consume varios):
| Formato | Función de entrada (→ geometry) | Función de salida (→ text/bytea) |
|---|---|---|
| WKT (Well-Known Text) | `ST_GeomFromText(text)` | `ST_AsText(geometry)` |
| WKB (Well-Known Binary) | `ST_GeomFromWKB(bytea)` | `ST_AsBinary(geometry)` |
| GML | `ST_GeomFromGML(text)` | `ST_AsGML(geometry)` |
| KML | `ST_GeomFromKML(text)` | `ST_AsKML(geometry)` |
| GeoJSON | — | `ST_AsGeoJSON(geometry)` |
| SVG | — | `ST_AsSVG(geometry)` |

- **WKT y WKB** siguen la especificación SFSQL pero **no manejan geometrías de 3 o 4 dimensiones**.
- PostGIS extiende estos formatos a **EWKT** (Extended WKT) y **EWKB** (Extended WKB) mediante `ST_AsEWKT()` / `ST_AsEWKB()`, que sí incluyen metadatos SRID.
- **Conversión desde texto:** sintaxis `olddata :: newtype` (ej. `'POINT(0 0)'::geometry`). Se puede incluir el SRID con la forma extendida: `'SRID=4326;POINT(0 0)'::geometry`.
- Ejemplo de representación WKB: `SELECT encode(ST_AsBinary(ST_GeometryFromText('LINESTRING(0 0 0,1 0 0,1 1 2)')), 'hex');`
- Ejemplo consumiendo KML y devolviendo GeoJSON: `SELECT ST_AsGeoJSON(ST_GeomFromKML('<Point><coordinates>1,1</coordinates></Point>'));` → `{"type":"Point","coordinates":[1,1]}`

**4. Tipo `geography`**
- Las coordenadas geográficas son verdaderas **coordenadas esféricas**; desde la versión 1.5, PostGIS ofrece esta funcionalidad mediante el tipo **`geography`** (paralelo al tipo `geometry`, que trabaja en cartesiano/plano).
- Distintas BBDD espaciales resuelven esto de forma distinta (Oracle lo disimula de forma transparente; SQL Server usa `STGeometry`/`STGeography`; Informix tiene extensiones separadas). PostGIS, como SQL Server, usa dos tipos explícitos: `Geometry` y `geography`.
- Los índices de **geography** sí controlan correctamente consultas que cruzan los polos o la línea de fecha internacional; los índices de **geometry**, no.
- Funciones nativas para `geography` (mismos nombres que en geometry, pero devuelven distancias/áreas en metros/m² por defecto): `ST_Distance`, `ST_DWithin`, `ST_Area`, `ST_Length`, `ST_Covers`, `ST_CoveredBy`, `ST_Intersects`, `ST_Buffer`, `ST_Intersection`, `ST_AsText`, `ST_GeographyFromText`, etc.
- Los nuevos campos de geografía se registran en la vista **`geography_columns`** (equivalente a `geometry_columns`).
- **¿Cuándo usar geometry vs geography?**
  - Datos geográficamente **compactos** (área pequeña/local) → `geometry` (más rápido, requiere elegir buen SRS de spatialreference.org).
  - Datos geográficamente **dispersos** (a escala global) → `geography` (evita complejidad de reproyección; el ahorro en complejidad compensa el rendimiento).
  - Se puede convertir a `geometry` para compensar limitaciones de funciones no disponibles en `geography`.

---

## Unidad 2-2. Análisis espacial con PostGIS

### Resumen estructurado

**1. Relaciones entre geometrías**
Hasta la unidad anterior solo se usaban funciones que operan sobre **una** geometría; ahora se comparan **relaciones entre dos geometrías**, según el estándar OGC:

| Función | Devuelve TRUE cuando... |
|---|---|
| `ST_Equals(A, B)` | A y B representan la misma geometría (la direccionalidad se ignora) |
| `ST_Intersects(A, B)` | A y B comparten cualquier porción de espacio (no son disjuntas) |
| `ST_Disjoint(A, B)` | A y B **no** comparten ningún espacio entre sí |
| `ST_Crosses(A, B)` | A y B tienen algunos puntos interiores en común, pero no todos |
| `ST_Overlaps(A, B)` | A y B comparten espacio, son de la misma dimensión, pero ninguna contiene completamente a la otra |
| `ST_Touches(A, B)` | A y B tienen al menos un punto en común, pero sus interiores no se intersectan |
| `ST_Within(A, B)` | A está completamente dentro de B |
| `ST_Contains(A, B)` | no hay puntos de B fuera de A, y al menos un punto interior de B está dentro de A (inversa de `ST_Within`) |
| `ST_Distance(A, B)` | (no es booleana) distancia mínima entre A y B — cartesiana 2D en `geometry`, esferoidal en metros en `geography` |
| `ST_DWithin(A, B, radio)` | A y B están a una distancia ≤ radio entre sí |

*Ejemplos prácticos del curso (con tablas `nyc_estaciones_metro`, `nyc_barrios`, `nyc_calles`):*
- `ST_Equals`: comparar si la geometría de una estación coincide exactamente con un WKB dado.
- `ST_Intersects`: usar `ST_Intersects(geom, ST_GeomFromText('POINT(...)',SRID))` sobre `nyc_barrios` para saber en qué barrio cae una estación de metro (ej. la estación "Broad St" cae en Manhattan, Financial District).
- `ST_DWithin(geom, punto, 10)` sobre `nyc_calles` para listar las calles a menos de 10 unidades de un punto (ej. devuelve Wall St, Broad St, Nassau St).

**2. Generación de geometrías**
Dos grandes grupos de funciones espaciales:
- **Funciones para trabajar con geometrías** (dado un dato geográfico, devuelven análisis/serialización/partes/booleanos): ej. `ST_Length()`, `ST_Area()`, `ST_AsText()`, `ST_AsGML()`, `ST_RingN()`, `ST_Contains()`, `ST_Intersects()`.
- **Funciones de construcción de geometrías**: crean **nuevas formas** a partir de las existentes:

| Función | Qué hace |
|---|---|
| `ST_Centroid(geom)` | Devuelve el centro geométrico de una geometría |
| `ST_PointOnSurface(geom)` | Devuelve un punto que garantiza estar dentro de la superficie (a diferencia del centroide, que puede caer fuera en formas cóncavas) |
| `ST_Buffer(geom, distancia, [opciones])` | Devuelve una geometría con todos los puntos cuya distancia a la geometría original es ≤ la distancia dada (crea una zona de influencia). El parámetro opcional `quad_segs` controla la suavidad de las curvas |
| `ST_Intersection(A, B)` | Devuelve la geometría que representa la porción **compartida** entre A y B |
| `ST_Union(A, B)` / `ST_Union([geometrías])` | Devuelve la geometría que representa la **unión** de puntos de las geometrías (también existe como función de agregado sobre varias filas) |

*Ejemplo práctico del curso:* `CREATE TABLE buffer_liberty_island AS SELECT ST_Buffer(geom,500) AS geom FROM nyc_bloque_censal WHERE blkid = '...'` seguido de `SELECT Populate_Geometry_Columns();` para registrar la nueva tabla espacial en `geometry_columns`.

*Otros ejemplos prácticos:*
- `ST_Intersection`: área compartida entre dos círculos creados con `ST_Buffer('POINT(0 0)', 2)` y `ST_Buffer('POINT(3 0)', 2)`.
- `ST_Union`: área total cubierta por esos mismos dos círculos.

**3. Otras funciones de la "lista de funciones" (unidades 2-1 y 2-2)**
- `Populate_Geometry_Columns()`: asegura que las columnas geométricas tengan las restricciones espaciales adecuadas y existan en `geometry_columns`.
- `ST_ExteriorRing(geom)`: linestring que representa el anillo exterior de un POLYGON (no funciona con MULTIPOLYGON).
- `ST_InteriorRingN(geom, n)`: enésimo anillo interior de un polígono.
- `ST_GeometryN(geom, n)`: geometría n-ésima (1 a N) si es GEOMETRYCOLLECTION/MULTI*.
- `ST_NumGeometries(geom)`: número de geometrías si es GEOMETRYCOLLECTION/MULTI*.
- `ST_NPoints(geom)` / `ST_NRings(geom)`: número de vértices / de anillos.
- `ST_StartPoint(geom)` / `ST_EndPoint(geom)`: primer/último punto de un LINESTRING.
- `ST_X(point)` / `ST_Y(point)`: coordenadas X/Y de un punto.
- `ST_Perimeter(geom)`: longitud de los límites de una superficie (ST_Surface/ST_MultiSurface).
- `ST_Transform(geom, srid)`: reproyecta una geometría a otro SRID.
- `substring(string [from int] [for int])` y `sum(expression)`: funciones estándar de PostgreSQL (no espaciales) usadas junto con las anteriores.

---

## Ejercicios Unidad 2 — PostGIS (instalación y primer uso)

Guía práctica paso a paso — checklist de lo esencial (útil para repasar antes de repetir la instalación):

1. Descargar `webmapping.zip` y descomprimir en un directorio **sin espacios** (ideal: `C:\webmapping\`).
2. Instalar **PostgreSQL** desde enterprisedb.com — durante la instalación:
   - Dejar todas las casillas de componentes marcadas (PostgreSQL Server, pgAdmin 4, Stack Builder, Command Line Tools).
   - Contraseña recomendada: `postgres`.
   - Puerto: `5432`.
3. Instalar **PostGIS** vía *Stack Builder* (Spatial Extensions → PostGIS Bundle) — **importante:** debe instalarse en el mismo directorio que PostgreSQL.
4. Abrir **pgAdmin 4**, conectar al servidor (localhost:5432, usuario/contraseña `postgres`).
5. Crear una base de datos (`world`) y habilitarla espacialmente con:
   ```sql
   CREATE EXTENSION postgis;
   ```
6. Verificar la instalación:
   ```sql
   SELECT postgis_full_version();
   ```
7. Elementos clave del esquema PostGIS:
   - Tabla `spatial_ref_sys`: sistemas de referencia espacial conocidos (por SRID, ej. 4326 = WGS84).
   - Vistas `geometry_columns` y `geography_columns`: se actualizan automáticamente con la dimensión/geometría/SRID de cada tabla espacial.
8. Formas de importar datos a PostGIS:
   - `shp2pgsql` (línea de comandos, solo shapefiles).
   - **PostGIS Shapefile and DBF Loader Exporter** (versión gráfica de shp2pgsql) — la usada en el ejercicio.
   - Administrador de BBDD de QGIS — permite además GeoPackage y otros formatos.
9. Al importar con el Loader: prestar atención a poner **SRID correcto (4326)**, no dejarlo en 0, o los datos no cargarán bien.
10. QGIS DB Manager también permite **exportar** tablas PostGIS a GeoJSON, GeoPackage, Shapefile, DXF, etc.
11. pgAdmin incluye un **visor de geometrías integrado** (Geometry Viewer) que muestra sobre OpenStreetMap cualquier resultado de consulta que devuelva una columna `geom`/`geog` en SRID 4326.
12. Consultas SQL básicas practicadas: `SELECT`, `WHERE`, alias con `AS`, funciones de agregación (`avg`, `stddev`, `sum`) con `GROUP BY`, `ORDER BY`.
13. Funciones espaciales introducidas:
    - **Conversión:** `ST_AsText(geom)` → convierte binario a WKT legible.
    - **Recuperación:** `ST_Perimeter(geom)` → longitud/perímetro.
    - **Comparación:** `ST_Distance(geomA, geomB)` → distancia (grados si es geometry, metros si es geography).
    - **Generación:** `ST_Centroid(geom)` → centroide; buffers con `ST_Buffer`.
    - **Relación espacial:** `ST_Intersects(geomA, geomB)` → intersección booleana.
14. Errores típicos: si al insertar aparece `Geometry SRID (0) does not match column SRID (4326)`, es porque la tabla origen se importó sin definir el SRID. Se soluciona reimportando con SRID correcto o con:
    ```sql
    SELECT UpdateGeometrySRID('countries','geom',4326);
    ```

---

