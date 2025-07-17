# Funciones utilitarias funcionales para pages

# Ejemplo: función pura para filtrar páginas públicas

def filter_public_pages(pages):
    return list(filter(lambda p: p.is_public, pages))

# Ejemplo: función para obtener títulos de páginas

def get_page_titles(pages):
    return list(map(lambda p: p.title, pages))
