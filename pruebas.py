import json
import pandas as pd

# Cargar el JSON directamente
with open('data\\estudiantes.json', 'r') as file:
    data = json.load(file)

# Convertir el JSON en un DataFrame de Pandas
df = pd.DataFrame([(school, student['carnet'], student['edad']) for school, students in data.items() for student in students], columns=['Escuela', 'Carnet', 'Edad'])

# Guardar el DataFrame como un archivo CSV
df.to_csv('data\\estudiantes.csv', index=False)



print("Archivos guardados exitosamente.")
