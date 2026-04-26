# Detector de Amenazas con IA

Herramienta de ciberseguridad que analiza logs del sistema 
usando Groq LLaMA 3.1 para detectar y clasificar amenazas en 
tiempo real.

## Lo que hace
- Lee logs de eventos del sistema operativo
- Analiza cada evento con IA (OpenAI GPT-4o-mini)
- Clasifica amenazas: CRÍTICO / ALTO / MEDIO / BAJO / NORMAL
- Genera reporte HTML visual con resumen ejecutivo

## Tecnologías
Python · OpenAI API · YARA · Pandas · Flask

## Cómo ejecutarlo
```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Configurar API Key
setx OPENAI_API_KEY "tu-clave-aqui"

# 3. Generar logs de prueba
python src/generador.py

# 4. Ejecutar el detector  
python src/detector.py

# 5. Ver reporte
start reports/reporte.html
```

## Amenazas que detecta
- Ataques de fuerza bruta SSH/RDP
- Conexiones a IPs maliciosas conocidas
- Procesos sospechosos en rutas inusuales
- Descargas de scripts remotos
- Escaneo de puertos

## Autor
Ricardo Hervey Estrada Garcia · Estudiante de Ciberseguridad
Universidad Autonoma de Nuevo Leon · 