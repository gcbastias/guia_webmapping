"""Integrate existing unit pages into Material section headings."""

from mkdocs.structure.pages import Page


class UnitIndexPage(Page):
    @property
    def is_index(self):
        return True


def on_nav(nav, config, files):
    for page in nav.pages:
        if page.file.src_uri.startswith("unidades/unidad-"):
            page.__class__ = UnitIndexPage
    return nav
