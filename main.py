import psycopg2
import psycopg2.extras
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    host="localhost",
    database="northwind",
    user="postgres",
    password="26111996"
)


cur = conn.cursor()

cur.execute("""
    SELECT customer_id, company_name, city
    FROM customers
    WHERE country = 'USA'
                """)
query_results_usa = cur.fetchall()
print(query_results_usa)

# dict_res = []
# for row in query_results:
#     dict_res.append(dict(row))
#
# print(dict_res)
# for row in query_results_usa:
#     print(f' id = {row[0]}\n company = {row[1]}\n city = {row[2]}\n')
cur.close()

# --------- dict ---------
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cur.execute("""SELECT product_name, company_name
                FROM products
                JOIN suppliers USING(supplier_id)
                ORDER BY product_name
                """)

products = cur.fetchall()
products_dict = []
for row in products:
    products_dict.append(dict(row))

print(products_dict)

cur.close()
conn.close()