# Definir la plantilla del cuerpo de la solicitud
kit_body_template = {
    "name": "Ejemplo de kit"
}

# Datos de prueba adicionales
user_body = {
    "name": "Usuario de prueba",
    "email": "usuario@example.com",
    "password": "segura123"
}

# Encabezados para las solicitudes
headers = {
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma",
    "Content-Type": "application/json"
}

# Datos de prueba para cada caso
test_cases = [
    {"name": "a", "expected_status": 201},  # 1 carácter
    {"name": "Ab" * 255 + "C", "expected_status": 201},  # 511 caracteres
    {"name": "", "expected_status": 400},  # 0 caracteres
    {"name": "Ab" * 256, "expected_status": 400},  # 512 caracteres
    {"name": "№%@,", "expected_status": 201},  # Caracteres especiales
    {"name": " A Aaa ", "expected_status": 201},  # Espacios
    {"name": "123", "expected_status": 201},  # Números
    {"name": None, "expected_status": 400},  # Falta el parámetro
    {"name": 123, "expected_status": 400},  # Número en vez de string
]
