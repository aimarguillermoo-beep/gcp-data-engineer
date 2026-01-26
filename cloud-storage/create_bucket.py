import os
from google.cloud import storage

# 1. Configuramos la ruta absoluta de tu llave
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/jcibernet/Desktop/gcp-data-engineer/gcp-data-engineer/cloud-storage/gcp-data-engineer-485516-de81e7eccc4e.json"

def create_bucket_if_not_exists(bucket_name, location="US-CENTRAL1"):
    try:
        storage_client = storage.Client()
        
        # 2. Verificamos si el bucket ya existe
        bucket = storage_client.lookup_bucket(bucket_name)
        
        if bucket:
            print(f"⚠️ El bucket '{bucket_name}' ya existe. No es necesario crearlo.")
        else:
            # 3. Si no existe, lo creamos
            print(f"⏳ Creando el bucket '{bucket_name}'...")
            new_bucket = storage_client.create_bucket(bucket_name, location=location)
            print(f"✅ Bucket {new_bucket.name} creado exitosamente en {location}.")
            
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    # Definimos el nombre una sola vez para evitar confusiones
    mi_bucket = "gcp-data-engineer-aimar-test" 
    create_bucket_if_not_exists(mi_bucket)