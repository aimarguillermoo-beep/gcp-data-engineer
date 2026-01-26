import os
from google.cloud import bigquery

# Ruta absoluta para que no falle nunca
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/jcibernet/Desktop/gcp-data-engineer/gcp-data-engineer/cloud-storage/gcp-data-engineer-485516-de81e7eccc4e.json"

def query_public_dataset():
    client = bigquery.Client()
    
    # Esta consulta usa un dataset público de Google sobre nombres en USA
    query = """
    SELECT order_items.id, order_id, product_id, products.name
    FROM `bigquery-public-data.thelook_ecommerce.order_items` AS order_items
    JOIN `bigquery-public-data.thelook_ecommerce.products` AS products
    ON order_items.product_id = products.id
    """
    
    results = client.query(query).to_dataframe()[:20]

    print(results)

if __name__ == "__main__":
    query_public_dataset()