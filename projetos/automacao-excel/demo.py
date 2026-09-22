import pandas as pd
import re
import unicodedata

def normalizar_coluna(nome: str) -> str:
    texto = unicodedata.normalize("NFKD", str(nome))
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return re.sub(r"[^a-zA-Z0-9]+", "_", texto).strip("_").lower()

def preparar(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [normalizar_coluna(c) for c in df.columns]
    return df.drop_duplicates()
