# Guía de estudio — Desarrollo de Aplicaciones Webmapping

Sitio estático (MkDocs + Material) con el resumen estructurado, los ejercicios prácticos y el glosario del curso **Desarrollo de Aplicaciones Webmapping**, listo para publicarse gratis en GitHub Pages.

## Estructura del proyecto

```
site-webmapping/
├── docs/
│   ├── index.md                 # Página de inicio
│   ├── plan-de-estudio.md       # Tu plan de estudio personalizado
│   ├── glosario.md              # Glosario acumulativo (todas las unidades)
│   └── unidades/
│       ├── unidad-1.md
│       ├── unidad-2.md
│       ├── unidad-3.md
│       ├── unidad-4.md
│       ├── unidad-5.md
│       ├── unidad-6.md
│       ├── unidad-7.md
│       └── unidad-8.md
├── mkdocs.yml                   # Configuración del sitio (navegación, tema, buscador)
├── requirements.txt             # Dependencia: mkdocs-material
└── .github/workflows/deploy.yml # Publica el sitio automáticamente en cada push a main
```

## 1. Probarlo en tu computador (opcional pero recomendado)

Necesitas Python instalado. Luego, desde esta carpeta:

```bash
pip install -r requirements.txt
mkdocs serve
```

Esto abre un servidor local (normalmente en `http://127.0.0.1:8000`) donde puedes ver el sitio con recarga automática mientras editas cualquier archivo `.md`.

## 2. Subirlo a GitHub

1. Crea un repositorio nuevo en GitHub (por ejemplo `guia-webmapping`), vacío, sin README ni licencia.
2. En `mkdocs.yml`, reemplaza `repo_url` por la URL real de tu repositorio.
3. Desde esta carpeta, ejecuta:

```bash
git init
git add .
git commit -m "Guía de estudio inicial: 8 unidades + glosario + plan de estudio"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/guia-webmapping.git
git push -u origin main
```

## 3. Publicarlo en GitHub Pages

Ya incluye un flujo de GitHub Actions (`.github/workflows/deploy.yml`) que construye y publica el sitio automáticamente cada vez que haces `push` a la rama `main`, usando `mkdocs gh-deploy`.

Después del primer `push`:

1. Ve a tu repositorio en GitHub → **Settings → Pages**.
2. En **Source**, selecciona la rama **`gh-pages`** (la crea automáticamente el workflow la primera vez que corre) y la carpeta `/ (root)`.
3. Guarda. En un par de minutos tu sitio quedará disponible en `https://TU_USUARIO.github.io/guia-webmapping/`.

Cada vez que agregues contenido nuevo (por ejemplo, cuando completes una unidad adicional del curso o quieras anotar tus propios apuntes), simplemente edita el `.md` correspondiente y vuelve a hacer `git push`: el sitio se actualiza solo.

## 4. Cómo agregar tus propios apuntes

Puedes escribir tus notas personales directamente al final de cada archivo de unidad (`docs/unidades/unidad-N.md`), o crear una carpeta `docs/notas/` con tus propios archivos y agregarlos a la navegación en `mkdocs.yml` (sección `nav`). MkDocs no distingue entre el contenido original y tus notas — todo se indexa y se puede buscar igual.

## 5. Editor recomendado

Cualquier editor de texto sirve, pero **Visual Studio Code** con la extensión "Markdown All in One" facilita mucho la edición y previsualización de estos archivos.
