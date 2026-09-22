import pandas as pd

def normalizar_uc(valor) -> str:
    return "".join(c for c in str(valor) if c.isdigit())

def cruzar(demo: pd.DataFrame, faturavel: pd.DataFrame) -> pd.DataFrame:
    demo = demo.copy()
    demo["uc_normalizada"] = demo["uc"].map(normalizar_uc)
    universo = set(faturavel["uc"].map(normalizar_uc))
    demo["encontrado"] = demo["uc_normalizada"].isin(universo)
    return demo
