import requests

# 🔹 Configuración de la API
BASE_URL = "https://cnt-b333ee19-b760-489d-bafd-edbf88794de0.containerhub.tripleten-services.com"
KIT_URL = f"{BASE_URL}/api/v1/kits"

# 🔹 Token de autenticación
AUTH_TOKEN = "Bearer jknnFApafP4awfAIFfafam2fma"

# 🔹 Encabezados
HEADERS = {
    "Authorization": AUTH_TOKEN,
    "Content-Type": "application/json"
}

# 🔹 Función para crear un kit
def create_kit(name):
    """Envía una solicitud POST a la API para crear un kit"""
    data = {"name": name} if name is not None else {}
    response = requests.post(KIT_URL, json=data, headers=HEADERS)
    return response

# 🔹 Casos de prueba actualizados
test_cases = [
    {"name": "a", "expected_status": 201},  # 1 carácter
    {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC", "expected_status": 201},  # 511 caracteres permitidos
    {"name": "", "expected_status": 400},  # 0 caracteres (debería fallar)
    {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD", "expected_status": 400},  # 512 caracteres (debería fallar)
    {"name": "№%@,", "expected_status": 201},  # Caracteres especiales
    {"name": " A Aaa ", "expected_status": 201},  # Espacios
    {"name": "123", "expected_status": 201},  # Números
    {"name": None, "expected_status": 400},  # Falta el parámetro
    {"name": 123, "expected_status": 400},  # Número en vez de string
]

# 🔹 Ejecutar pruebas
for test in test_cases:
    response = create_kit(test["name"])
    status_code = response.status_code
    result = "✅" if status_code == test["expected_status"] else "❌"
    
    print(f"{result} Prueba: {test['name']!r} -> Esperado: {test['expected_status']}, Obtenido: {status_code}")
