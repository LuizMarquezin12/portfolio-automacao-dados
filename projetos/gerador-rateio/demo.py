import pandas as pd

OBRIGATORIOS = ["instalacao", "distribuidora", "grupo", "percentual_rateio"]

def validar(df: pd.DataFrame) -> pd.DataFrame:
    pendencias = []
    for i, row in df.iterrows():
        for campo in OBRIGATORIOS:
            if campo not in df.columns or pd.isna(row.get(campo)):
                pendencias.append({"linha_excel": i + 2, "campo": campo})
    return pd.DataFrame(pendencias)

if __name__ == "__main__":
    exemplo = pd.DataFrame([{
        "instalacao": "UC-DEMO-01",
        "distribuidora": "DISTRIBUIDORA DEMO",
        "grupo": "01",
        "percentual_rateio": 25.0
    }])
    print(validar(exemplo))
