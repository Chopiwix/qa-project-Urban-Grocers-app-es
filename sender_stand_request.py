import requests

#  URL Base de la API
BASE_URL = "https://cnt-b333ee19-b760-489d-bafd-edbf88794de0.containerhub.tripleten-services.com"
KIT_URL = f"{BASE_URL}/api/v1/kits"

#  Token de autenticación
AUTH_TOKEN = "Bearer jknnFApafP4awfAIFfafam2fma"

#  Pruebas para la creación de kits
def test_kit_creation():
    test_cases = [
        {"name": "a", "expected_status": 201},  # 1 carácter
        {"name": "El valor de prueba para esta comprobación será inferior a", "expected_status": 201},  # 511 caracteres
        {"name": "", "expected_status": 400},  # 0 caracteres
        {"name": "a" * 512, "expected_status": 400},  # 512 caracteres
        {"name": "№%@,", "expected_status": 201},  # Caracteres especiales
        {"name": " A Aaa ", "expected_status": 201},  # Espacios
        {"name": "123", "expected_status": 201},  # Números
        {"name": None, "expected_status": 400},  # Falta el parámetro
        {"name": 123, "expected_status": 400},  # Número en vez de string
    ]

    headers = {
        "Authorization": AUTH_TOKEN,
        "Content-Type": "application/json"
    }

    for test in test_cases:
        data = {"name": test["name"]} if test["name"] is not None else {}

        response = requests.post(KIT_URL, json=data, headers=headers)
        status_code = response.status_code

        # Comprobar si la respuesta coincide con la esperada
        result = "✅PASA" if status_code == test["expected_status"] else "❌NO PASA"
        print(f"{result} Prueba: {test['name']!r} -> Esperado: {test['expected_status']}, Obtenido: {status_code}")

#  Ejecutar las pruebas
test_kit_creation()

