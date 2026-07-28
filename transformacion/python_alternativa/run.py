"""
Alternativa a dbt (100% válida). Implemente capas raw -> staging -> consumo con pruebas.
Sugerencia: funciones puras por capa + tests (pytest) que validen reglas de calidad y
el contrato de datos. Ejecute: python transformacion/python_alternativa/run.py
"""
def staging(): ...     # limpieza, normalización de moneda/fechas, dedup
def consumo(): ...     # tabla unificada lista para métricas
def validar_contrato(): ...  # rompe si se incumple

if __name__ == "__main__":
    staging(); consumo(); validar_contrato()
