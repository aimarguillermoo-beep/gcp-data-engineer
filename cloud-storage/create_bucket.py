from google.cloud import storage

def create_bucket(bucket_name, location="US-CENTRAL1", storage_class="STANDARD"):
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        bucket.storage_class = storage_class
        new_bucket = storage_client.create_bucket(bucket, location=location)
        print(f"✅ Bucket {new_bucket.name} creado exitosamente.")
    except Exception as e:
        print(f"❌ Error al crear el bucket: {e}")

if __name__ == "__main__":
    # ¡CUIDADO! Cambia este nombre por uno que nadie más tenga
    mi_nombre_unico = "gcp-data-engineer-aimar-test" 
    create_bucket(mi_nombre_unico)