import pytest
from sender_stand_request import post_new_client_kit  # Importar función para enviar solicitudes
from data import get_kit_body, get_new_user_token  # Importar funciones auxiliares

# Función para validar respuestas exitosas (201)
def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201, f"Esperado: 201, Obtenido: {response.status_code}"
    assert response.json().get("name") == kit_body["name"], \
        f"El nombre del kit no coincide: {response.json().get('name')}"

# Función para validar respuestas fallidas (400)
def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400, f"Esperado: 400, Obtenido: {response.status_code}"

# Pruebas individuales basadas en la lista de comprobación
def test_kit_name_min_length():
    """Número permitido de caracteres (1)"""
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

def test_kit_name_max_length():
    """Número permitido de caracteres (511)"""
    kit_body = get_kit_body("a" * 511)
    positive_assert(kit_body)

def test_kit_name_too_short():
    """Número de caracteres menor al permitido (0)"""
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

def test_kit_name_too_long():
    """Número de caracteres mayor al permitido (512)"""
    kit_body = get_kit_body("a" * 512)
    negative_assert_code_400(kit_body)

def test_kit_name_special_characters():
    """Se permiten caracteres especiales"""
    kit_body = get_kit_body("№%@")
    positive_assert(kit_body)

def test_kit_name_spaces():
    """Se permiten espacios"""
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)

def test_kit_name_numbers():
    """Se permiten números"""
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

def test_kit_name_missing_parameter():
    """El parámetro no se pasa en la solicitud"""
    kit_body = {}
    negative_assert_code_400(kit_body)

def test_kit_name_invalid_type():
    """Se pasa un tipo de parámetro diferente (número)"""
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)
