import pandas as pd

def classificar(faturavel: pd.DataFrame, capturas: pd.DataFrame) -> pd.DataFrame:
    base = faturavel.copy()
    base["chave"] = base["distribuidora"].str.upper().str.strip() + "|" + base["uc"].astype(str)
    chaves_capturadas = set(capturas["chave"])
    base["status"] = base["chave"].apply(
        lambda x: "Capturada" if x in chaves_capturadas else "Faltante"
    )
    return base
