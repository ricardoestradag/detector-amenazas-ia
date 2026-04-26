import random
from datetime import datetime, timedelta

def generar_logs():
    eventos_normales = [
        "login_exitoso | usuario: jgarcia | IP: 192.168.1.10",
        "archivo_accedido | ruta: C:\\Users\\jgarcia\\docs | usuario: jgarcia",
        "conexion_saliente | destino: google.com:443 | proceso: chrome.exe",
        "login_exitoso | usuario: mlopez | IP: 192.168.1.25",
    ]
    
    eventos_sospechosos = [
        "login_fallido | usuario: admin | IP: 45.33.32.156",
        "login_fallido | usuario: root | IP: 45.33.32.156",
        "escaneo_puertos | origen: 45.33.32.156 | puertos: 22,80,443,3389",
        "proceso_desconocido | nombre: svch0st.exe | ruta: C:\\Temp\\svch0st.exe",
        "conexion_saliente | destino: 185.220.101.45:4444 | proceso: svch0st.exe",
        "descarga_script | url: http://evil-site.ru/payload.ps1 | usuario: system",
    ]
    
    logs = []
    tiempo_base = datetime.now() - timedelta(hours=2)
    
    for i in range(40):
        tiempo = tiempo_base + timedelta(seconds=i*180)
        evento = random.choice(eventos_normales)
        logs.append(f"{tiempo.strftime('%Y-%m-%d %H:%M:%S')} | INFO | {evento}")
    
    for i in range(10):
        tiempo = tiempo_base + timedelta(seconds=random.randint(0, 7200))
        evento = random.choice(eventos_sospechosos)
        logs.append(f"{tiempo.strftime('%Y-%m-%d %H:%M:%S')} | WARNING | {evento}")
    
    random.shuffle(logs)
    
    with open("logs/sistema.log", "w", encoding="utf-8") as f:
        f.write("\n".join(logs))
    
    print(f"Generados {len(logs)} eventos en logs/sistema.log")

if __name__ == "__main__":
    generar_logs()
