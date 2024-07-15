import requests
import mysql.connector

def verify_urls():
    conn = mysql.connector.connect(
        host='localhost',
        user='richin_usr',
        password='P@ssword1',
        database='PRODUCT'
    )
    cursor = conn.cursor()

    # Retrieve the necessary data from the table
    cursor.execute('SELECT id, url FROM PRODUCT_TABLE')
    products = cursor.fetchall()
    print(products)  # For debugging purposes, to check fetched data

    for product in products:
        product_id, url = product
        if url:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    active = True
                else:
                    active = False
            except requests.exceptions.RequestException:
                active = False
        else:
            active = False

        # Update the prd_table column with the active status
        cursor.execute('UPDATE PRODUCT_TABLE SET prd_table = %s WHERE id = %s', (active, product_id))
        conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    verify_urls()
