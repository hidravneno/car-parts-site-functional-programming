# Obtener URLs de páginas
def get_page_urls(pages):
    return list(map(lambda p: getattr(p, 'url', ''), pages))

# Filtrar páginas por fecha de publicación
def filter_pages_by_date(pages, date):
    return list(filter(lambda p: getattr(p, 'published_date', None) == date, pages))
# Funciones utilitarias funcionales para pages

# Ejemplo: función pura para filtrar páginas públicas

def filter_public_pages(pages):
    return list(filter(lambda p: p.is_public, pages))

# Ejemplo: función para obtener títulos de páginas

def get_page_titles(pages):
    return list(map(lambda p: p.title, pages))
