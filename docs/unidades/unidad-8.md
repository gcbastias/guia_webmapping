# Unidad 8 · Integrar y publicar el proyecto

<div class="visual-hero"><div class="eyebrow">Unidad 08 / Piloto visual</div><h2>Un visor claro por fuera.<br>Una arquitectura coherente por dentro.</h2><p>Reúne datos, servicios y experiencia de uso en el proyecto original de la Confederación Hidrográfica del Duero.</p><p>Preparar → integrar → diseñar → validar → entregar</p></div>

Síntesis visual de las clases, con diagramas originales para explicar los conceptos. La práctica se conserva al final de esta misma unidad.

## 1. Preparar el despliegue

<figure class="lesson-figure"><a href="../../assets/unidad-8/despliegue.svg" target="_blank" rel="noopener"><img src="../../assets/unidad-8/despliegue.svg" alt="De los datos a la publicación" loading="lazy" /></a></figure>

Define qué pregunta resolverá el visor, para quién y con qué datos. Comprueba geometrías, atributos, referencia, origen y fecha.

La infraestructura debe responder al volumen, consultas y mantenimiento. Un alojamiento estático puede servir el frontend, pero no ejecuta por sí solo PostGIS o GeoServer. Los servicios necesitan un entorno apropiado.

La interoperabilidad permite combinar componentes compatibles. Cambiar herramientas exige revisar funciones, formatos y configuración; no toda sustitución es automática.


## 2. Arquitectura del proyecto

<figure class="lesson-figure"><a href="../../assets/unidad-8/proyecto.svg" target="_blank" rel="noopener"><img src="../../assets/unidad-8/proyecto.svg" alt="Rutas WMS y GeoJSON del proyecto original" loading="lazy" /></a></figure>

El proyecto solicita Leaflet. Demarcación y ríos se incorporan a PostGIS y GeoServer y se representan como WMS. Los embalses se cargan como GeoJSON.

| Elemento | Tratamiento solicitado |
|---|---|
| Demarcación | WMS; sin relleno |
| Ríos | WMS; etiquetas siguiendo líneas |
| Embalses | GeoJSON; azul |
| Fondo | A elección |
| Controles | Escala métrica, capas y título |

El esquema sintetiza el enunciado, sin añadir entregables. Las instrucciones completas aparecen al final.

<p class="content-source"><strong>Referencia:</strong> <a href="../../materiales/Ejercicio_8_Proyecto%20final.pdf" target="_blank" rel="nofollow noopener noreferrer">MappingGIS · Ejercicio_8_Proyecto final.pdf</a>.</p>

## 3. Diseñar para comprender

<figure class="lesson-figure"><a href="../../assets/unidad-8/jerarquia-visual.svg" target="_blank" rel="noopener"><img src="../../assets/unidad-8/jerarquia-visual.svg" alt="Jerarquía de capas y controles" loading="lazy" /></a></figure>

Un mapa útil necesita fondo discreto, temas distinguibles y controles comprensibles. Un relleno opaco puede ocultar otras capas aunque estén cargadas.

Usa símbolos coherentes, leyenda cuando haga falta y etiquetas que no saturen las escalas. Ofrece las herramientas que necesita la tarea: no hace falta reproducir todos los menús de un SIG de escritorio.

La maqueta no representa la geografía real del Duero. Permite estudiar bordes, líneas y puntos antes de aplicar estilos a las capas del curso.

<p class="content-source"><strong>Referencia:</strong> <a href="../../materiales/Ejercicio_8_Proyecto%20final.pdf" target="_blank" rel="nofollow noopener noreferrer">MappingGIS · Ejercicio_8_Proyecto final.pdf</a>.</p>

## 4. Pruebas y mantenimiento

<figure class="lesson-figure"><a href="../../assets/unidad-8/entornos.svg" target="_blank" rel="noopener"><img src="../../assets/unidad-8/entornos.svg" alt="Separar construcción, validación y servicio" loading="lazy" /></a></figure>

Desarrollo permite construir; pruebas valida recorridos; producción atiende a usuarios. Conservar versiones recuperables permite sustituir una implementación cuando la siguiente está lista.

Comprueba carga, capas, referencia, leyendas, consultas, controles y pantalla. Revisa peticiones cuando un servicio falla. Las pruebas reducen problemas, sin garantizar su ausencia absoluta.

Caché, volumen y peticiones influyen en rendimiento. Documentar origen, fecha y configuración facilita mantener el visor cuando cambian datos o servicios.


## 5. Evaluación original

<figure class="lesson-figure"><a href="../../assets/unidad-8/rubrica.svg" target="_blank" rel="noopener"><img src="../../assets/unidad-8/rubrica.svg" alt="Diez puntos de la rúbrica del curso" loading="lazy" /></a></figure>

La rúbrica reparte diez puntos. Simbología y WMS reciben dos cada uno; los demás criterios, uno.

La entrega utiliza una plantilla con capturas de los pasos y del visor en las escalas indicadas. El PDF también especifica EPSG:4326 y LATIN1 en la importación de los shapefiles de la práctica.

Estos criterios pertenecen al curso: no son una evaluación nueva del piloto. El proyecto original, con ayuda y puntuación, se conserva a continuación.

<p class="content-source"><strong>Referencia:</strong> <a href="../../materiales/Ejercicio_8_Proyecto%20final.pdf" target="_blank" rel="nofollow noopener noreferrer">MappingGIS · Ejercicio_8_Proyecto final.pdf</a>.</p>


## 6. Preparar los materiales del proyecto {#preparacion-practica}

Necesitas las capas originales de **Límite demarcación**, **segmentos de río** y **embalses**, además de PostgreSQL/PostGIS, QGIS, GeoServer con la extensión CSS y el entorno de Leaflet. Recupera los archivos desde los materiales del curso; las capas `countries` y `cities` de unidades anteriores no sustituyen los datos del Duero.

1. Extrae cada shapefile junto con sus archivos auxiliares. Abre las capas en QGIS y revisa su geometría, atributos y sistema de referencia.
2. La consigna original utiliza `EPSG:4326` y solicita `LATIN1` en la importación de los shapefiles. Comprueba su CRS de origen antes de transformar o asignar una etiqueta.
3. Conserva una carpeta de trabajo y otra para las capturas de la entrega. Identifica el campo de nombre de río que necesitarás para las etiquetas.
4. Comprueba que PostgreSQL y GeoServer están iniciados y que puedes abrir el visor Leaflet mediante HTTP.

## 7. Integrar el recorrido de las unidades anteriores {#procedimientos-guiados}

### De las capas a los servicios

1. Sigue la importación PostGIS de la [Unidad 2](unidad-2.md#importar-datos) para las capas de demarcación y ríos. Utiliza nombres de tabla que puedas reconocer después y comprueba sus registros y SRID.
2. En GeoServer conecta un almacén PostGIS a la base donde las importaste. Publica ambas tablas con el procedimiento de la [Unidad 3](unidad-3.md#procedimientos-guiados), calculando límites y comprobando su previsualización.
3. Crea los estilos CSS que pide la consigna: borde de demarcación sin relleno y etiquetas de río siguiendo las líneas. Usa el nombre real del atributo de etiqueta.
4. Valida los estilos y asígnalos a sus capas. Comprueba más de una escala antes de conectar el visor: una etiqueta oculta por escala no implica que la capa no exista.

### Del servicio al visor Leaflet

1. Reutiliza la estructura de la [Unidad 5](unidad-5.md#procedimientos-guiados): biblioteca cargada, contenedor con altura y mapa inicializado una sola vez.
2. Añade demarcación y ríos como WMS con sus nombres publicados. Revisa transparencia y orden para que el fondo y los embalses sean visibles.
3. Exporta embalses a GeoJSON desde QGIS y guárdalo dentro de la carpeta web del proyecto. Cárgalo por HTTP y configura su estilo azul; adapta la opción de estilo al tipo geométrico de esa capa.
4. Añade el fondo elegido y los controles que enumera el enunciado. Comprueba que la escala muestra únicamente la unidad métrica y que el control de capas referencia las instancias que realmente añadiste al mapa.
5. Añade un título visible del visor; el texto de la pestaña HTML por sí solo puede no cumplir ese propósito.

### Comprobar antes de entregar

| Revisión | Evidencia que puedes observar |
|---|---|
| PostGIS | Tablas cargadas y SRID correcto |
| GeoServer | Capas publicadas y estilos aplicados |
| WMS | Demarcación y ríos visibles desde el visor |
| GeoJSON | Embalses visibles con la simbología solicitada |
| Controles | Escala métrica, capas y título funcionales |
| Integración | Sin errores de carga; orden y etiquetas legibles |

Guarda las capturas de los pasos principales en la plantilla original. La rúbrica y el enunciado completos permanecen al final: este recorrido no añade requisitos ni entrega una solución terminada.

**Para compartir el resultado:** una URL con `localhost` solo sirve en el equipo que ejecuta los servicios. Un alojamiento estático puede servir los archivos del visor, pero los servicios PostGIS/GeoServer necesitan su propio entorno accesible. El despliegue requiere revisar direcciones, HTTPS y acceso; no basta con subir el HTML que apunta al servidor local.

<p class="content-source"><strong>Fuentes:</strong> enunciado original del proyecto final de MappingGIS y procedimientos de las unidades 2, 3 y 5. Referencias técnicas: <a href="https://docs.geoserver.org/stable/en/user/data/webadmin/index.html">GeoServer · publicación de datos</a> · <a href="https://leafletjs.com/reference.html">Leaflet · capas y controles</a>.</p>

## Material y referencias


Ampliación técnica: [Publicación con GeoServer](https://docs.geoserver.org/stable/en/user/data/webadmin/index.html) · [Visor Leaflet](https://leafletjs.com/examples/quick-start/). Las versiones e interfaces del PDF corresponden al entorno de las clases; los diagramas muestran conceptos.


## Antes de resolver las actividades {#antes-de-ejercicios}

Completa la preparación y los procedimientos anteriores. Después avanza por los ejercicios en su orden original: varias actividades utilizan archivos, capas o cambios de las anteriores. Cada actividad conserva su enunciado y sus paneles de instrucciones y capturas dentro de la página; el PDF queda como respaldo.

Si una consigna menciona «el código anterior» o «la imagen anterior», abre su panel de contexto antes de trabajar. Comprueba qué archivo o recurso debes modificar, guarda el cambio y verifica el resultado antes de tomar la captura. No ejecutes de nuevo una creación o importación si ya existe el objeto correspondiente.

## Ejercicio Unidad 8 {#ejercicios-originales-del-curso}

Enunciados y contexto de los PDF de MappingGIS. No se añaden actividades ni soluciones. Los paneles incluyen los pasos originales dentro de la unidad; el PDF conserva la maquetación completa.

**Práctica:** [PDF original completo](../materiales/Ejercicio_8_Proyecto%20final.pdf){target="_blank" rel="nofollow noopener noreferrer"}.

### Proyecto final · Enunciado y entrega


Enunciado del proyecto final propuesto al terminar el curso, que integra PostGIS, GeoServer (WMS + estilos CSS) y Leaflet (WMS + GeoJSON).

#### Planteamiento
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

#### Entrega del proyecto
Subir a la plataforma la plantilla de resultados con capturas de pantalla de los pasos principales realizados. En las capturas se debe ver el visor creado, reflejando la visualización de las capas en las escalas determinadas.

#### Ayuda
- Las capas se encuentran en la plataforma de formación.
- El sistema de referencia espacial es el **EPSG:4326**.
- Si no se sabe cómo hacer alguno de los pasos, se puede preguntar al tutor o plantear una pregunta en el foro del curso para debatir con los compañeros.

#### Notas
Dentro de las opciones de importación de los shapefiles a PostGIS, debe indicarse **LATIN1** para definir la codificación de los caracteres.

#### Calificación

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

### Proyecto final · Páginas originales

<details class="source-page"><summary>Ver página 2 del proyecto original</summary><img src="../../assets/ejercicios/unidad-8/proyecto-pagina-2.png" alt="Página 2 del proyecto final original" loading="lazy" /></details>

<details class="source-page"><summary>Ver página 3 del proyecto original</summary><img src="../../assets/ejercicios/unidad-8/proyecto-pagina-3.png" alt="Página 3 del proyecto final original" loading="lazy" /></details>

