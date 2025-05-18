import sqlite3
import os

# Verificar os arquivos na pasta gold
print("Arquivos na pasta gold:")
for file in os.listdir('gold'):
    print(f"- {file}")

# Tentar conectar ao banco de dados
try:
    conn = sqlite3.connect('gold/gold_layer.db')
    cursor = conn.cursor()
    
    # Listar todas as tabelas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    print("\nTabelas no banco de dados:")
    for table in tables:
        print(f"- {table[0]}")
        
        # Listar colunas de cada tabela
        cursor.execute(f"PRAGMA table_info({table[0]})")
        columns = cursor.fetchall()
        print(f"  Colunas da tabela {table[0]}:")
        for col in columns:
            print(f"  - {col[1]} ({col[2]})")
        print()
    
    conn.close()
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}") 