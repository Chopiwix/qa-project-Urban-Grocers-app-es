import requests
from copy import copy
from configuration import BASE_URL

#funcion para crear el número permitido de caracteres (1)
def post_new_client_kit(kit_body, auth_token):
    """
    Envía una solicitud para crear un nuevo kit.
    :param kit_body: Diccionario con el cuerpo de la solicitud (datos del kit).
    :param auth_token: Token de autenticación del usuario.
    :return: Respuesta de la API.
    """
    kit_data = copy(kit_body)
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(f"{BASE_URL}/api/v1/kits", json=kit_data, headers=headers)
    return response

# Token de autenticación
auth_token = "jknnFApafP4awfAIFfafam2fma"

# Prueba de creación de un kit con un nombre de 1 carácter
if __name__ == "__main__":
    kit_body = { "name": "a" }  # Nombre del kit
    response = post_new_client_kit(kit_body, auth_token)

    # Verificar el código de respuesta
    if response.status_code == 200 or response.status_code == 201:
        print("Código de respuesta:", response.status_code)
        print("Respuesta del servidor:", response.json())
    else:
        print(f"Error: Código de respuesta {response.status_code}")
        print("Cuerpo de la respuesta:", response.text)



