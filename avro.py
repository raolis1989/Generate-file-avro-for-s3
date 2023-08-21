import pandas as pd
import fastavro
import json

# Ruta al archivo Excel
excel_file = r'C:/Users/mendo/OneDrive/Documents/test-prueba.xlsx'

# Leer los datos del archivo Excel
data_frame = pd.read_excel(excel_file)

# Leer el archivo Excel
data_frame = pd.read_excel(excel_file)

avro_schema = {
    "type": "record",
    "name": "Person",
    "fields": [
        {"name": "id", "type": "int"},
        {"name": "nombre", "type": "string"},
        {"name": "apellido", "type": "string"},
        {"name": "rut", "type": "int"},
        {"name": "saldo", "type": "int"},
        {"name": "cuenta", "type": "string"}
    ]
}

# Lista para almacenar los registros en formato Avro
avro_records = []

# Recorrer las filas del DataFrame y construir los registros
for _, row in data_frame.iterrows():
    avro_record = {
        "id": row['id'],
        "nombre": row['nombre'],
        "apellido": row['apellido'],
        "rut": row['rut'],
        "saldo": row['saldo'],
        "cuenta": row['cuenta'],
    }
    avro_records.append(avro_record)

avro_file = r'C:/Users/mendo/OneDrive/Documents/GenerateAvro/resultado.avro'
with open(avro_file, 'wb') as f:
    fastavro.writer(f, avro_schema, avro_records)

print(f"Archivo Avro '{avro_file}' generado correctamente.")
