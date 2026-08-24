# Ejercicios — Unidad 2

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
