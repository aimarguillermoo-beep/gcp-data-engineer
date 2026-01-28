from google.cloud import storage
import os

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Sube un archivo al bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f"✅ Archivo {source_file_name} subido a {destination_blob_name}.")

if __name__ == "__main__":
    # 1. Crea un archivo de prueba rápido
    with open("datos_prueba.csv", "w") as f:
        f.write("id,nombre,valor\n1,Aimar,100\n2,GCP,200")

    # 2. Súbelo (Usa el nombre del bucket que creaste antes)
    nombre_del_bucket = "gcp-data-engineer-aimar-test" 
    upload_blob(nombre_del_bucket, "datos_prueba.csv", "data/primeros_datos.csv")