"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='123')

try:
    with conn:
        with conn.cursor() as cur:
            with open('north_data/customers_data.csv', encoding='utf-8') as f:
                items = csv.DictReader(f)
                for i in items:
                    cur.execute(
                        'INSERT INTO customers VALUES (%s, %s, %s)',
                        (i['customer_id'], i['company_name'], i['contact_name'])
                    )

            with open('north_data/employees_data.csv', encoding='utf-8') as f:
                items = csv.DictReader(f)
                for i in items:
                    cur.execute(
                        'INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                        (i['employee_id'], i['first_name'], i['last_name'], i['title'], i['birth_date'], i['notes'])
                    )

            with open('north_data/orders_data.csv', encoding='utf-8') as f:
                items = csv.DictReader(f)
                for i in items:
                    cur.execute(
                        'INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                        (i['order_id'], i['customer_id'], i['employee_id'], i['order_date'], i['ship_city'])
                    )
finally:
    conn.close()
