import os
from google.cloud import storage

# --- BORRAMOS LA LÍNEA DE OS.ENVIRON ---
# Ya no la necesitamos porque usamos Application Default Credentials (ADC)

def create_bucket_if_not_exists(bucket_name, location="US-CENTRAL1"):
    try:
        # Al no pasarle argumentos, busca automáticamente tu login de gcloud
        storage_client = storage.Client()
        
        bucket = storage_client.lookup_bucket(bucket_name)
        
        if bucket:
            print(f"⚠️ El bucket '{bucket_name}' ya existe. No es necesario crearlo.")
        else:
            print(f"⏳ Creando el bucket '{bucket_name}'...")
            new_bucket = storage_client.create_bucket(bucket_name, location=location)
            print(f"✅ Bucket {new_bucket.name} creado exitosamente en {location}.")
            
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    # Asegúrate de que este nombre sea único. 
    # Si alguien ya usó 'gcp-data-engineer-aimar-test', cámbialo un poco.
    mi_bucket = "gcp-data-engineer-aimar-test-jc" 
    create_bucket_if_not_exists(mi_bucket)