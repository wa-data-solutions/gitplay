import pandas as pd
import json
import os

# ==========================
# CAMINHOS DOS ARQUIVOS
# ==========================

arquivo_excel = r"C:\Users\user\gitplay\extract\client.xlsx"
arquivo_json = r"C:\Users\user\gitplay\extract\client.json"

# Cria a pasta de saída, caso não exista
os.makedirs(os.path.dirname(arquivo_json), exist_ok=True)

try:
    # Lê a planilha Excel
    df = pd.read_excel(arquivo_excel)

    # Substitui valores nulos por None
    df = df.where(pd.notnull(df), None)

    # Converte os registros para uma lista de dicionários
    dados = df.to_dict(orient="records")

    # Salva o arquivo JSON
    with open(arquivo_json, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4, default=str)

    print("Conversão realizada com sucesso!")
    print(f"Arquivo Excel: {arquivo_excel}")
    print(f"Arquivo JSON : {arquivo_json}")

except Exception as erro:
    print(f"Ocorreu um erro: {erro}")