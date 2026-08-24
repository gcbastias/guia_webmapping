# Ejercicios — Unidad 8

Enunciado del proyecto final propuesto al terminar el curso, que integra PostGIS, GeoServer (WMS + estilos CSS) y Leaflet (WMS + GeoJSON).

**Planteamiento**
La **Confederación Hidrográfica del Duero** quiere migrar su visor cartográfico, basado en una arquitectura privativa, a una solución más potente que sea *open source*. Solicita realizar una aplicación web mapping con la librería **Leaflet**, con los siguientes requisitos:

- Las capas **Límite demarcación** y **segmentos de río** deben mostrarse como **WMS**: para ello hay que añadir las capas a **PostGIS** y a **GeoServer**, utilizando el complemento **CSS** de GeoServer para personalizar la simbología:
  - La capa **Límite demarcación** no debe tener relleno, para poder ver las capas de ríos y embalses.
  - La capa **segmentos de río** debe mostrar las etiquetas de los ríos siguiendo las líneas.
- La capa **embalses** debe mostrarse como **GeoJSON**. Hay que utilizar una función de estilo para mostrar los embalses de color azul.
- Un **mapa base** a elección (OSM, Stamen, Bing, etc.).
- Añadir, al menos, los siguientes **controles**:
  - Escala (solo la escala métrica decimal).
  - Control de capas.
  - Título.

**Entrega del proyecto**
Subir a la plataforma la plantilla de resultados con capturas de pantalla de los pasos principales realizados. En las capturas se debe ver el visor creado, reflejando la visualización de las capas en las escalas determinadas.

**Ayuda**
- Las capas se encuentran en la plataforma de formación.
- El sistema de referencia espacial es el **EPSG:4326**.
- Si no se sabe cómo hacer alguno de los pasos, se puede preguntar al tutor o plantear una pregunta en el foro del curso para debatir con los compañeros.

**Notas**
Dentro de las opciones de importación de los shapefiles a PostGIS, debe indicarse **LATIN1** para definir la codificación de los caracteres.

**Calificación**

| Criterio | Puntuación |
|---|---|
| Creación de base de datos e importación de datos a PostGIS | 1 punto |
| Importación a GeoServer | 1 punto |
| Personalización de simbología | 2 puntos |
| Mostrar las capas como WMS (visor Leaflet) | 2 puntos |
| Mostrar la capa GeoJSON (visor Leaflet) | 1 punto |
| Título (visor Leaflet) | 1 punto |
| Escala, solo la escala métrica (visor Leaflet) | 1 punto |
| Control de capas (visor Leaflet) | 1 punto |
| **Total** | **10 puntos** |
