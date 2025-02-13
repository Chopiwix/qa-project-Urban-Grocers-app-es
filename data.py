# Definir la plantilla del cuerpo de la solicitud
kit_body_template = {
    "name": "Ejemplo de kit"
}

# Función para generar un nuevo cuerpo de solicitud sin modificar el original
def get_kit_body(name):
    """Devuelve una copia de kit_body_template con el nombre modificado"""
    kit_body = kit_body_template.copy()  # Copiamos el diccionario original
    kit_body["name"] = name  # Reemplazamos el nombre
    return kit_body

# Función para obtener un token de usuario válido
def get_new_user_token():
    """Devuelve un token de usuario válido (reemplazar con lógica real si es necesario)"""
    return "Bearer jknnFApafP4awfAIFfafam2fma"
