import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def analizar_log(linea_log):
    prompt = f"""Eres un analista de ciberseguridad experto.
Analiza esta línea de log de seguridad:

LOG: {linea_log}

Responde SOLO en este formato JSON exacto, sin texto adicional:
{{
  "nivel_amenaza": "CRITICO|ALTO|MEDIO|BAJO|NORMAL",
  "tipo_ataque": "nombre del tipo de ataque o 'ninguno'",
  "explicacion": "explicacion breve en español de máximo 2 oraciones",
  "accion": "acción recomendada o 'ninguna'"
}}"""

    respuesta = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )
    return respuesta.choices[0].message.content

def leer_logs(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        return [linea.strip() for linea in f.readlines() if linea.strip()]

print("Iniciando prueba...")
log_prueba = "2024-01-15 03:47:22 | WARNING | login_fallido | usuario: admin | IP: 45.33.32.156"
print(f"Analizando: {log_prueba}")
resultado = analizar_log(log_prueba)
print("Resultado:")
print(resultado)