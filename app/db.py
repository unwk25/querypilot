import os;
import psycopg;
from dotenv import load_dotenv;    ## dotenv module import load_doteenv function

load_dotenv()
DATABASE_URL=os.getenv("DATABASE_URL")

def run_query(sql):
    with psycopg.connect(DATABASE_URL)as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            column_names=[col.name for col in cur.description]
            # column_name=[]
            # for col in cur.description:
            #     column_name.append(col.name)
            rows=cur.fetchall()
            return column_names,rows

def show(sql):  ## LLM  query will come here in place of sql
    print("\nSQL:",sql)
    try:
        columns, rows=run_query(sql)   ## When we run the SELECT query 
        print(columns)
        for row in rows:
            print(row)
    except psycopg.Error as e:
        print("Refused by the database", e)

if __name__=="__main__":
    show("SELECT company_name, country FROM customers ORDER BY company_name LIMIT 5;")

    show("DELETE FROM orders WHERE order_id = 10248;")

    show("SELECT COUNT(*) FROM customers;")

    show("SELECT company_name, city FROM customers WHERE country = 'Germany' ORDER BY company_name;")

    show("SELECT product_name, unit_price FROM products ORDER BY unit_price DESC LIMIT 5;")

    show("SELECT c.country, COUNT(o.order_id) AS orders FROM customers c JOIN orders o ON o.customer_id = c.customer_id GROUP BY c.country ORDER BY orders DESC LIMIT 5;")

    show("SELECT e.first_name || ' ' || e.last_name AS employee, COUNT(o.order_id) AS orders FROM employees e JOIN orders o ON o.employee_id = e.employee_id GROUP BY employee ORDER BY orders DESC LIMIT 3;") 
  