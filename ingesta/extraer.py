"""
Stub de ingesta. Extraiga las fuentes que ELIJA hacia una zona raw local.
Debe incluir al menos 2 formatos y al menos 1 fuente remota (API de NY o descarga).
Sugerencia de destino: Parquet particionado o DuckDB. Justifique.
"""
def desde_csv_local(): ...
def desde_json_paginado(): ...   # recorra meta.next
def desde_xml(): ...
def desde_api_remota(): ...      # p.ej. data.ny.gov (SODA: $limit/$offset)

if __name__ == "__main__":
    pass
