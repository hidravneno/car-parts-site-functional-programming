# Funciones utilitarias funcionales para products

from functools import reduce

# Ejemplo: función pura para filtrar partes disponibles

def filter_available_parts(parts):
    # Mostrar todas las partes, sin filtrar por stock
    return list(parts)

# Ejemplo: función para obtener nombres de partes

def get_part_names(parts):
    return list(map(lambda p: p.name, parts))

# Ejemplo: función para sumar el stock total

def total_stock(parts):
    # Suma solo si el objeto tiene el atributo 'stock', si no lo tiene, suma 0
    return reduce(lambda acc, p: acc + getattr(p, 'stock', 0), parts, 0)
