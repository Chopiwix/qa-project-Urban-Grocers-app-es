# 🧪 Urban Grocers | Pruebas automatizadas de API REST

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?logo=pytest&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP-217C77)
![API](https://img.shields.io/badge/Tipo-API%20Testing-153E63)

> Automatización de pruebas para la creación de kits, con validación de datos de entrada y respuestas HTTP.

[← Mi perfil](https://github.com/Chopiwix) · [Ver portafolio de QA](https://chopiwix.github.io/Portafolio/)

## 🎯 Objetivo

Validar el campo **`name`** de la creación de kits a través del endpoint **`POST /api/v1/kits`**, utilizando **Python, Requests y Pytest**.

Las pruebas envían solicitudes HTTP con encabezados de autorización y comparan el código de estado recibido con el resultado esperado para cada escenario.

## ✅ Cobertura implementada

El archivo `data.py` contiene **9 casos de prueba**, ejecutados con `@pytest.mark.parametrize`:

| Escenario de entrada | HTTP esperado |
| --- | ---: |
| Nombre de 1 carácter | 201 |
| Nombre de 511 caracteres | 201 |
| Nombre vacío | 400 |
| Nombre de 512 caracteres | 400 |
| Caracteres especiales | 201 |
| Nombre con espacios | 201 |
| Caracteres numéricos como texto | 201 |
| Valor `null` | 400 |
| Valor numérico en lugar de texto | 400 |

> Los códigos indicados son **resultados esperados definidos en las pruebas**, no un reporte de ejecución actual.

## 🧩 Estructura del repositorio

| Archivo | Función |
| --- | --- |
| [`create_kit_name_kit_test.py`](create_kit_name_kit_test.py) | Caso parametrizado y aserciones del estado HTTP |
| [`sender_stand_request.py`](sender_stand_request.py) | Construcción de solicitudes POST y cuerpos JSON |
| [`data.py`](data.py) | Datos de entrada, resultados esperados y encabezados |
| [`configuration.py`](configuration.py) | URL base y rutas de la API |

## ▶️ Cómo ejecutarlo

```bash
git clone https://github.com/Chopiwix/qa-project-Urban-Grocers-app-es.git
cd qa-project-Urban-Grocers-app-es
python -m venv .venv
# Activa el entorno virtual según tu sistema operativo.
python -m pip install pytest requests
pytest -v create_kit_name_kit_test.py
```

**Antes de ejecutar:** configura una URL de API disponible en `configuration.py` y utiliza credenciales de prueba válidas en tu entorno local. Los servidores temporales del curso pueden haber expirado. **No publiques tokens o contraseñas reales en el repositorio.**

## 💡 Habilidades demostradas

Pruebas de API REST · diseño de escenarios positivos y negativos · análisis de valores límite · parametrización con Pytest · solicitudes JSON · validación de códigos HTTP.

---

**Contacto:** [Marina Barreiro Vargas](https://github.com/Chopiwix) · [Portafolio completo](https://chopiwix.github.io/Portafolio/)
