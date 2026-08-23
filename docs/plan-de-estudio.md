# Plan de estudio personalizado

Este plan combina tres cosas que definiste: tu **perfil de aprendizaje** (medido con un mini test estilo VARK), tu **ritmo disponible** (ligero, 1-3 horas/semana, sin apuro) y tu **orden de estudio preferido** (secuencial, Unidad 1 → 8, terminando con el proyecto final).

## 1. Tu perfil de aprendizaje

Con tus 8 respuestas al test, el resultado fue:

| Estilo | Puntaje | Peso en tu perfil |
|---|---|---|
| **Kinestésico (aprender haciendo)** | 4 / 8 | Dominante |
| **Visual (diagramas, arquitecturas)** | 3 / 8 | Secundario, fuerte |
| **Auditivo (verbalizar, explicar en voz alta)** | 1 / 8 | Apoyo puntual, útil para destrabarte |
| **Lecto-escritor (leer/escribir texto extenso)** | 0 / 8 | Mínimo — no es tu vía principal |

**Qué significa esto en la práctica:**

- **No empieces por leer la teoría completa de una unidad.** Es tu punto más débil como método de aprendizaje y es donde más te vas a aburrir o perder foco. Usa el resumen estructurado como *referencia* (para consultar mientras haces algo), no como lectura de principio a fin.
- **Empieza cada unidad por el diagrama o la arquitectura general** (por ejemplo: "Interfaz de usuario → Servidor web → Base de datos" o el flujo de peticiones WMS). Este sitio incluye esos esquemas al inicio de cada resumen estructurado — míralos primero, antes de leer nada más.
- **Pasa a la práctica lo antes posible.** Tu mejor forma de fijar un concepto (ej. una función `ST_`, una clase de OpenLayers) es usarla en un ejercicio real, no memorizarla. Por eso el plan de abajo te lleva a la sección de ejercicios de cada unidad muy rápido, casi en paralelo con la teoría.
- **Cuando te traves con un error, verbaliza el problema antes de buscar la solución.** Explícatelo en voz alta (o grábate un audio corto) como si se lo contaras a otra persona: "Estoy intentando publicar la capa X como WMS, GeoServer me devuelve tal error, ya revisé tal cosa...". Esto activa tu canal auditivo y muchas veces la solución aparece sola al formular bien el problema.
- **Repasa rehaciendo, no releyendo.** La estrategia de repaso que más te sirve es volver a hacer el ejercicio desde cero sin mirar la guía, no releer tus apuntes. El plan de repaso (sección 6) está armado sobre esta base.

## 2. Método de estudio por unidad (tu rutina)

Cada unidad del curso, sin importar el tamaño, la vas a trabajar con la misma rutina de 3 pasos, pensada para tu perfil kinestésico-visual:

1. **Mirar antes de leer (10-15 min).** Abre la unidad en el sitio, ubica el o los diagramas/tablas de arquitectura, y recorre los títulos en negrita como si fuera un índice. No leas párrafo por párrafo todavía.
2. **Practicar (el grueso del tiempo).** Ve directo a la sección "Ejercicios prácticos" de esa unidad y empieza a ejecutarlos paso a paso en tu propio entorno (PostgreSQL, GeoServer, el navegador, etc.). Vuelve al resumen estructurado solo como referencia puntual cuando el ejercicio te pida un concepto que no recuerdas.
3. **Cerrar con una verbalización (5 min).** Al terminar la sesión, resume en voz alta (o en una nota de audio) qué hiciste y qué aprendiste, en tus propias palabras. No hace falta escribirlo — el punto es decirlo.

## 3. Calendario de estudio (ritmo ligero, ~1-3 h/semana)

A tu ritmo, completar las 8 unidades + proyecto final toma aproximadamente **6 meses** (~26 semanas). Está pensado en fases mensuales para que puedas seguir tu avance sin sentir presión. Los tiempos son orientativos: si una unidad te resulta más simple, avanza antes; si te traba una instalación, tómate una semana extra sin culpa.

| Fase | Semanas aprox. | Contenido |
|---|---|---|
| **Fase 0 — Preparar el entorno** | Semana 1 | Instalar PostgreSQL+PostGIS, GeoServer, Node.js+Git (ver checklist sección 5) |
| **Fase 1 — Fundamentos** | Semanas 2-3 | Unidad 1 (conceptual) + arranque de Unidad 2 |
| **Fase 2 — PostGIS** | Semanas 3-6 | Unidad 2 completa (teoría + ejercicios de instalación/SQL espacial) |
| **Fase 3 — GeoServer y estándares OGC** | Semanas 7-10 | Unidad 3 (la más extensa: GeoServer, WMS/WFS/WCS/WPS, SLD/CSS, conexiones QGIS) |
| **Fase 4 — Caché de mapas** | Semanas 11-12 | Unidad 4 (GeoWebCache) |
| **Fase 5 — Frontend: HTML/CSS/JS + Leaflet** | Semanas 13-16 | Unidad 5 y 5-1 (21 ejercicios progresivos con Leaflet) |
| **Fase 6 — OpenLayers** | Semanas 17-20 | Unidad 6 (16 ejercicios progresivos) |
| **Fase 7 — MapStore** | Semanas 21-23 | Unidad 7 (instalación, usuarios, capas, widgets, dashboards) |
| **Fase 8 — Cierre y proyecto final** | Semanas 24-26 | Unidad 8 + proyecto final (Confederación Hidrográfica del Duero) |

**Ritmo semanal sugerido dentro de cada fase (2 sesiones de ~1 h, o 1 sesión de ~2-3 h):**

- Sesión A: pasos 1 y 2 de tu rutina (mirar diagrama + empezar el/los ejercicios).
- Sesión B: terminar el ejercicio + paso 3 (verbalizar el cierre).

## 4. Plan de ejecución de los ejercicios prácticos (orden del curso)

Vas a ejecutar los ejercicios en el mismo orden en que aparecen en el curso, unidad por unidad. Esta tabla es tu checklist maestra — puedes ir marcando cada bloque a medida que lo completas.

| # | Unidad | Ejercicio / bloque práctico | Requiere instalar |
|---|---|---|---|
| 1 | 2 | Instalación PostgreSQL + PostGIS, creación BD `world`, primeras consultas SQL espaciales | PostgreSQL, PostGIS, pgAdmin |
| 2 | 3-1 | Instalación GeoServer, extensiones (CSS, Vector Tiles, WPS), publicar capas raster/vectoriales, estilos SLD y CSS, filtros CQL, teselas vectoriales | JDK 17, GeoServer |
| 3 | 3 | Conexiones WMS/WFS/OGC API/WCS desde QGIS | QGIS |
| 4 | 4 | Caché raster y vectorial con GeoWebCache, comparación de velocidad, visualización en Google Earth | Google Earth (opcional) |
| 5 | 5 | Fundamentos HTML/CSS/JS y depuración de errores en el navegador (9 ejercicios) | Editor de texto (VS Code, Notepad++) |
| 6 | 5-1 | Visor Leaflet progresivo: mapa básico → WMS → capas UI → grupos → eventos → controles → GeoJSON/coropletas → WFS+AJAX → plugins (12 ejercicios, `L_map1.html` a `L_map12.html`) | — |
| 7 | 6 | Visor OpenLayers progresivo: CDN vs npm, proyección, capas WMS/WFS/VectorTile, heatmap, estilos, controles, interacciones (16 ejercicios, `ol_map1.js` a `ol_map16.js`) | Node.js, Git |
| 8 | 7 | Instalación MapStore, usuarios/roles, mapas WMS/WFS, anotaciones, estilos, widgets, contextos con geoprocesamiento WPS, dashboards | MapStore (Tomcat embebido) |
| 9 | 8 | **Proyecto final**: visor Leaflet para la Confederación Hidrográfica del Duero (capas WMS con CSS + capa GeoJSON con función de estilo + controles de escala/capas/título) | — (reutiliza todo lo anterior) |

**Regla de oro para cada bloque:** no pases al siguiente ejercicio de la lista sin haber dejado funcionando el actual (aunque sea de forma básica). Como tu aprendizaje es kinestésico, saltarte pasos prácticos te va a costar más caro que en otros perfiles — la memoria "muscular" del ejercicio anterior es la base del siguiente.

## 5. Checklist de entorno técnico (una sola vez, al inicio)

Instálalo todo en la Fase 0, antes de empezar la Unidad 2, para no interrumpir el flujo de práctica más adelante:

- [ ] **PostgreSQL** (con pgAdmin 4, Stack Builder y Command Line Tools) — contraseña recomendada `postgres`, puerto `5432`.
- [ ] **PostGIS** vía Stack Builder, en el mismo directorio que PostgreSQL.
- [ ] **JDK 17** (Adoptium/Eclipse Temurin) — requerido por GeoServer.
- [ ] **GeoServer** (versión estable, Platform Independent Binary) + extensiones CSS Styling, Vector Tiles y WPS.
- [ ] **QGIS** (para las conexiones OGC de la Unidad 3 y como cliente SIG de apoyo).
- [ ] **Node.js** (LTS) y **Git** (con Git Bash en Windows) — requeridos por `npm create ol-app` en la Unidad 6.
- [ ] **MapStore** (paquete binario, requiere el mismo JDK/JRE) — para la Unidad 7.
- [ ] Un editor de código (VS Code recomendado) con extensión de resaltado para HTML/CSS/JS/SQL.

## 6. Estrategia de repaso y refuerzo

Como tu mejor repaso es *rehacer*, no *releer*, usa este esquema con cada unidad ya completada:

- **Repaso corto (misma semana):** vuelve a ejecutar el ejercicio más importante de la unidad de memoria, sin mirar la guía. Si te trabas, ahí sí consultas el paso puntual que te falta.
- **Repaso de refuerzo (2-3 semanas después):** antes de empezar una unidad nueva, dedica 15-20 minutos a rehacer *una parte* (no todo) del ejercicio de la unidad anterior — por ejemplo, solo la publicación de una capa en GeoServer, o solo un mapa básico de Leaflet.
- **Repaso final (antes del proyecto final, Fase 8):** repite de memoria el flujo completo PostGIS → GeoServer → Leaflet a menor escala (una sola capa), como calentamiento antes de encarar el proyecto final real.

## 7. Cómo encaja el sitio web (GitHub Pages) en este método

El sitio que vas a publicar en GitHub Pages (ver `README.md` del repositorio) es tu **libro de consulta**, no tu material de lectura principal. Úsalo así:

- Ábrelo en una pestaña aparte mientras haces el ejercicio práctico, y consúltalo solo cuando necesites un dato puntual (una función SQL, una URL de ejemplo, un fragmento de código).
- Usa el buscador del sitio en vez de navegar manualmente — es más rápido y evita que te distraigas leyendo secciones que no necesitas en ese momento.
- El glosario es tu mejor amigo para repasos cortos: en 5 minutos puedes escanear los términos de una unidad y verbalizar en voz alta la definición de los que no recuerdes, antes de comprobarla.
