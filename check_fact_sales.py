import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('gold/gold_layer.db')

# Consultar metadata das tabelas relacionadas a pedidos
query_orders = """
SELECT * FROM sqlite_master 
WHERE type='table' 
AND (name LIKE '%order%' OR name LIKE '%FACT%' OR name LIKE '%fact%');
"""

print("Metadados das tabelas relacionadas a pedidos:")
orders_tables = pd.read_sql_query(query_orders, conn)
print(orders_tables[['name', 'sql']])
print("\n" + "-"*80 + "\n")

# Mostrar colunas da tabela fact_sales
print("Colunas da tabela fact_sales:")
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(fact_sales)")
for col in cursor.fetchall():
    print(f"- {col[1]} ({col[2]})")
print("\n" + "-"*80 + "\n")

# Consultar a primeira linha da tabela fact_sales
print("Primeira linha da tabela fact_sales:")
try:
    fact_sales_sample = pd.read_sql_query("SELECT * FROM fact_sales LIMIT 1", conn)
    print(fact_sales_sample)
except Exception as e:
    print(f"Erro ao consultar fact_sales: {e}")
print("\n" + "-"*80 + "\n")

# Verificar se existem outras tabelas com informações de data de entrega
qdate_columns = """
SELECT m.name as table_name, p.name as column_name
FROM sqlite_master m
JOIN pragma_table_info(m.name) p
WHERE p.name LIKE '%deliver%' OR p.name LIKE '%date%' OR p.name LIKE '%time%'
ORDER BY m.name, p.name
"""

print("Colunas relacionadas a datas e entregas em todas as tabelas:")
try:
    date_columns = pd.read_sql_query(qdate_columns, conn)
    print(date_columns)
except Exception as e:
    print(f"Erro ao consultar colunas de data: {e}")

# Verificar se existe uma tabela orders separada
print("\n" + "-"*80 + "\n")
print("Verificando outras tabelas relacionadas a pedidos:")
order_tables_query = """
SELECT name FROM sqlite_master 
WHERE type='table' 
AND (name LIKE '%order%' OR name LIKE '%pedido%')
"""

order_tables = pd.read_sql_query(order_tables_query, conn)
print(order_tables)

conn.close() 