# Guía visual de Webmapping

Sitio de estudio con ocho unidades, diagramas ampliables, fuentes dentro del contenido y los ejercicios originales integrados en cada unidad.

Sitio: https://gcbastias.github.io/guia_webmapping/

## Editar y previsualizar

Instalar dependencias: `python -m pip install -r requirements.txt`.
Previsualizar: `python -m mkdocs serve`.
Comprobar la generación: `python -m mkdocs build --strict`.

Editar `docs/`, `mkdocs.yml` y las plantillas de `overrides/`. La carpeta `site/` es una salida generada y no se edita ni se versiona.

## Organización

- `docs/index.md`: portada con los paneles de unidades.
- `docs/unidades/`: contenido, referencias y práctica original.
- `docs/assets/`: diagramas SVG y páginas de referencia de los ejercicios.
- `docs/materiales/`: PDF originales enlazados en el contenido.
- `docs/stylesheets/`: estilos del sitio.
- `overrides/partials/`: navegación personalizada.

Las fuentes se indican junto a las explicaciones. Los diagramas propios se amplían al pulsarlos. Los enlaces a PDF de ejercicios abren otra pestaña. La Unidad 1 no incorpora ejercicios nuevos; las prácticas de las demás unidades conservan la numeración de los materiales de MappingGIS.

## Publicar y recuperar una versión

El flujo `.github/workflows/deploy.yml` genera y publica GitHub Pages al recibir cambios en `main`, usando la rama `gh-pages`.

Antes de publicar el piloto se conserva la versión anterior mediante la etiqueta `respaldo-antes-piloto-visual-2026-10-24`. Para recuperarla, preparar un cambio de restauración desde esa etiqueta y publicarlo mediante el mismo flujo.

## Indexación y acceso

La plantilla `overrides/main.html` añade `noindex, nofollow, noimageindex` a todas las páginas HTML. Los enlaces a PDF incluyen la indicación `nofollow`.

Estas indicaciones no restringen el acceso. No configuran un encabezado `X-Robots-Tag` para los PDF y no hacen privado el repositorio. Los PDF y sus capturas siguen siendo archivos públicos mientras se alojen aquí. Para excluir los PDF de búsquedas se requiere un alojamiento que permita enviar `X-Robots-Tag: noindex`; para restringir acceso se requiere autenticación y almacenamiento privado.
