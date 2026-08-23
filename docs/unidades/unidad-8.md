# Unidad 8. Consideraciones finales y recomendaciones

### Resumen estructurado

**1. Contenido de la unidad**
- Pasos para desplegar una aplicación web mapping.
- Recomendaciones.
- Cómo diseñar una aplicación web mapping.

**2. Pasos para desplegar una aplicación web mapping**

Flujo de despliegue en 4 etapas: **1. Datos → 2. Hardware → 3. Crear entornos → 4. Pruebas, producción y publicación**.

- **1. Datos:**
  - Definir qué información mostrará cada capa.
  - Incluirlos en una base de datos espacial.
  - Utilizar el mismo sistema de referencia espacial.
- **2. Hardware:** decidir dónde desplegar la arquitectura. **Una infraestructura web GIS es un trabajo difícil y caro de implementar.**
  - **Servidor interno.**
  - **Servidor externo:**
    - Un servidor especializado en WEB GIS.
    - En un servidor compartido no se podrá crear una arquitectura completa → se necesitará un servidor dedicado no administrado.
  - *Más info:* recurso del curso "Opciones para crear una arquitectura WEB GIS en un servidor" (AcuGIS).
- **3. Crear entornos:**
  - Entorno de desarrollo.
  - Entorno de pruebas.
  - Entorno de producción.
- **4. Pruebas, producción y publicación:** después de desarrollar una aplicación debe pasar por una fase de *testing*, en la que se debe testar para detectar fallos, hasta llegar al punto en el que la aplicación esté libre de errores. Una vez probada, se puede poner en el entorno de producción y publicarla en la web.

**3. Recomendaciones**

- **Cumple con los estándares de la OGC.** Las herramientas hacen uso de los estándares de la OGC, lo que permite que distintos componentes se intercambien con facilidad → **¡Interoperabilidad!**

- **Herramientas alternativas a las vistas en el curso** (equivalencias posibles según el diagrama del curso, en el que un cliente —Google, OpenLayers, Bing— envía una petición de tesela a una caché tipo GeoWebCache: si la tesela ya existe se devuelve directamente, y si no existe se recupera del servidor de mapas —GeoServer, ArcGIS, MapServer— y se guarda antes de devolverla):

| Herramienta vista en el curso | Alternativa posible |
|---|---|
| GeoServer | **MapServer** / **deegree** |
| QGIS | **gvSIG** / **ArcGIS** |
| OpenLayers | **Google Maps** / **Leaflet** |
| GeoWebCache | **TileCache** |

- **La heterogeneidad es buena.** Mezcla y combina las herramientas que mejor funcionen en tu proyecto: no es necesario desarrollar una aplicación con los mismos componentes que se han visto en el curso.
  - *Ejemplo:* se puede implementar **GeoServer sobre Oracle**.
  - *Ejemplo:* se puede implementar **ArcGIS Enterprise sobre PostGIS**.
  - *Arquitectura de ejemplo del curso:* una aplicación empresarial (navegador, JavaScript, OpenLayers) se comunica con un servidor de aplicaciones **J2EE** (Java) y con **GeoServer**, ambos apoyados sobre una base de datos **Oracle**.

- **Tu aplicación web mapping no debería ser como un SIG de escritorio.** Las aplicaciones deben ser intuitivas y familiares para los usuarios; hay que pensar en cómo lo hacen **Google Maps** u **OpenStreetMap** (interfaces sencillas), en contraposición a la complejidad de paneles, barras de herramientas y menús propia de un SIG de escritorio como QGIS.

**4. Cómo diseñar una aplicación web mapping**

Siete recomendaciones de diseño:

1. **Haz un mapa atractivo e informativo.** Un buen diseño de un mapa web va más allá del simple objetivo de proporcionar información geográfica: debe ofrecer una experiencia atractiva e informativa al usuario.
2. **No lo juntes todo.** Hay una tendencia a la sobrecarga con tantas capas como sea posible en un único mapa web.
3. **Simplifica herramientas, menús y botones.** Un mapa web será eficaz si es fácil de usar. Evita llenarlo de muchas herramientas, menús y botones; piensa para qué se va a usar el mapa y ofrece la funcionalidad imprescindible.
4. **Hazlo intuitivo.** El mapa debe ser capaz de entenderse sin necesidad de un manual o unas instrucciones.
   - Recomendaciones asociadas a los puntos 3 y 4:
     - Los datos deben tener una **simbología lógica**.
     - Incluye una **leyenda** para las capas que necesiten una explicación adicional.
     - Utiliza un **fondo neutro** para las capas base, de forma que no compitan con las capas importantes.
     - Configura la **visibilidad de las etiquetas** utilizando los rangos de escala; haz lo mismo con las vistas.
5. **Optimízalo. El mapa debe ser servido rápidamente.** Almacena en caché los *tiles* para mejorar la representación de las imágenes que uses como *base maps* (con baja frecuencia de actualización). **Evita las reproyecciones al vuelo.** Cada vez hay más usuarios con *tablets* y *smartphones*, así que optimizar el mapa web para **dispositivos móviles** es fundamental: si el mapa tarda mucho en mostrarse, el usuario no lo usará.
6. **Actualízalo.** Los datos que muestres deben ser ante todo fiables y deben estar actualizados.
7. **Documéntalo.** Muestra información de la **fecha y origen de los datos**; los usuarios quieren saber cuándo se creó el mapa y quién lo creó. Que no falte información esencial.

**5. La formación es esencial**
- MappingGIS recomienda continuar la formación con el curso online **"Web mapping interactivo con Leaflet, React y PostGIS"**.
- **Leaflet** en combinación con **React** permite crear mapas interactivos; utilizando **Node.js** y, más concretamente, **Express**, se puede establecer la conexión con una base de datos **PostGIS**.
- Contenidos que se plantean como continuación del curso:
  - Añadir datos propios con GeoJSON.
  - Interactuar con el mapa mediante eventos e interacciones.
  - Animar marcadores, crear mapas de calor, realizar geocodificación.
  - Crear formularios para filtrar datos y una herramienta para buscar los datos.
  - Desarrollar funcionalidades **CRUD** (Crear, Leer, Actualizar, Eliminar) para permitir la edición y actualización de datos geoespaciales (PostGIS) directamente desde el cliente Leaflet.
  - Publicar los visores webmapping en internet utilizando un servidor gratuito.

---

### Proyecto final del curso — Ejercicio práctico Unidad 8

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

---

