import json

# Cargar los datos de los archivos JSON
with open('data\\usuarios.json', 'r') as file:
    users_data = json.load(file)

with open('data\\escuelas.json', 'r') as file:
    escuelas_data = json.load(file)

# Crear un diccionario para mapear EscuelaID a nombre de la escuela
escuela_id_to_name = {escuela['id']: escuela['nombre'] for escuela in escuelas_data.values()}

# Actualizar el JSON de usuarios
for user in users_data['users']:
    escuela_id = user.pop('EscuelaID')
    user['Escuela'] = escuela_id_to_name.get(escuela_id, 'Escuela desconocida')

# Guardar el JSON actualizado en un nuevo archivo
with open('data\\usuarios.json', 'w') as file:
    json.dump(users_data, file, indent=4)

print("JSON actualizado guardado como 'users_updated.json'")
