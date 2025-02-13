import requests
from data import get_kit_body  # Importamos la función para obtener el cuerpo del kit

#  Configuración de la API
BASE_URL = "https://cnt-b333ee19-b760-489d-bafd-edbf88794de0.containerhub.tripleten-services.com"
KIT_URL = f"{BASE_URL}/api/v1/kits"

#  Función para crear un kit utilizando kit_body_template
def post_new_client_kit(name, auth_token):
    """Envía una solicitud POST para crear un kit de producto"""

    kit_body = get_kit_body(name)  # Generamos el cuerpo usando la plantilla

    headers = {
        "Authorization": auth_token,
        "Content-Type": "application/json"
    }

    response = requests.post(KIT_URL, json=kit_body, headers=headers)
    
    return response  # Retornamos la respuesta para su verificación
