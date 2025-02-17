import requests
import data  # Importamos todo el archivo data.py
import configuration  # Importamos configuration.py para usar las URLs de la API

# Función para generar un nuevo cuerpo de solicitud sin modificar el original
def get_kit_body(name):
    """Devuelve una copia de kit_body_template con el nombre modificado"""
    kit_body = data.kit_body_template.copy()
    kit_body["name"] = name  
    return kit_body

# Función para obtener un token de usuario válido
def get_new_user_token():
    """Devuelve un token de usuario válido"""
    return data.headers["Authorization"]  # Usamos el token almacenado en data.py

# Método "sender" para crear un nuevo usuario
def post_new_user(user_body):
    """Envía una solicitud POST para crear un usuario"""
    
    response = requests.post(
        configuration.BASE_URL + configuration.CREATE_USER_PATH,  # Construimos la URL correctamente
        json=user_body,  # Cuerpo de la solicitud
        headers=data.headers  # Usamos los headers definidos en data.py
    )

    return response  # Retorna la respuesta de la API

# Método "sender" para crear un kit
def post_new_client_kit(name):
    """Envía una solicitud POST para crear un kit"""

    kit_body = get_kit_body(name)  # Generamos el cuerpo del kit
    auth_token = get_new_user_token()  # Obtenemos el token de usuario

    response = requests.post(
        configuration.BASE_URL + configuration.KITS_PATH,  # Construimos la URL correctamente
        json=kit_body,  # Cuerpo de la solicitud
        headers={"Authorization": auth_token, "Content-Type": "application/json"}
    )

    return response  # Retorna la respuesta de la API

