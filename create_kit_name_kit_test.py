import pytest
import data  # Importamos todo data.py
from sender_stand_request import post_new_client_kit  # Importamos la función para enviar la solicitud

# Helper para obtener el token
def get_token():
    return data.headers["Authorization"]

# Helper para obtener el cuerpo del kit
def get_kit_body(name):
    kit_body = data.kit_body_template.copy()
    kit_body["name"] = name
    return kit_body

# Pruebas con los casos de prueba importados
@pytest.mark.parametrize("test_case", data.test_cases)  # Importamos los casos de prueba desde data.py
def test_create_kit(test_case):
    response = post_new_client_kit(test_case["name"])  # Enviamos la solicitud con el nombre del kit
    status_code = response.status_code

    # ✅ PASA si el código de estado es el esperado, ❌ NO PASA si es diferente
    result = "✅ PASA" if status_code == test_case["expected_status"] else "❌ NO PASA"
    
    print(f"{result} Prueba: {test_case['name']!r} -> Esperado: {test_case['expected_status']}, Obtenido: {status_code}")

    # Aseguramos que el código de respuesta es el esperado
    assert status_code == test_case["expected_status"]
