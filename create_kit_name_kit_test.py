from sender_stand_request import post_new_client_kit
from data import get_new_user_token  # Importamos la función para obtener el token

#  Obtener el token de autenticación
AUTH_TOKEN = get_new_user_token()

#  Casos de prueba 
test_cases = [
    {"name": "a", "expected_status": 201},  # 1 carácter
    {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC", "expected_status": 201},  # 511 caracteres
    {"name": "", "expected_status": 400},  # 0 caracteres
    {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD", "expected_status": 400},  # 512 caracteres
    {"name": "№%@,", "expected_status": 201},  # Caracteres especiales
    {"name": " A Aaa ", "expected_status": 201},  # Espacios
    {"name": "123", "expected_status": 201},  # Números
    {"name": None, "expected_status": 400},  # Falta el parámetro
    {"name": 123, "expected_status": 400},  # Número en vez de string
]

#  Ejecutar las pruebas
for test in test_cases:
    response = post_new_client_kit(test["name"], AUTH_TOKEN)
    status_code = response.status_code

    result = "✅PASA" if status_code == test["expected_status"] else "❌NO PASA"
    
    print(f"{result} Prueba: {test['name']!r} -> Esperado: {test['expected_status']}, Obtenido: {status_code}")
