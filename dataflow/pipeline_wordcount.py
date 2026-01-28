import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def run():
    # Datos que ya confirmamos anteriormente
    PROJECT_ID = 'gcp-engineer-curso04'
    BUCKET = 'gs://gcp-data-engineer-aimar-test-jc'

    options = PipelineOptions(
        runner='DataflowRunner',
        project=PROJECT_ID,
        region='europe-west1',
        temp_location=f'{BUCKET}/temp',
        staging_location=f'{BUCKET}/staging'
    )

    with beam.Pipeline(options=options) as p:
        (p
         | 'Leer de GCS' >> beam.io.ReadFromText('gs://dataflow-samples/shakespeare/kinglear.txt')
         | 'Dividir palabras' >> beam.FlatMap(lambda line: line.split())
         | 'Crear Parejas' >> beam.Map(lambda word: (word, 1))
         | 'Contar' >> beam.CombinePerKey(sum)
         | 'Formatear' >> beam.Map(lambda wc: f'{wc[0]}: {wc[1]}')
         | 'Escribir en GCS' >> beam.io.WriteToText('gs://gcp-data-engineer-aimar-test-jc/wordcount/output')
        )

if __name__ == '__main__':
    run()