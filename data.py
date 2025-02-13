# Definir la plantilla del cuerpo de la solicitud
kit_body_template = {
    "name": "Ejemplo de kit"
}

# Función para generar un nuevo cuerpo de solicitud sin modificar el original
def get_kit_body(name):
    
    kit_body = kit_body_template.copy()  
    kit_body["name"] = name  
    return kit_body

# Función para obtener un token de usuario válido
def get_new_user_token():
   
    return "Bearer jknnFApafP4awfAIFfafam2fma"
