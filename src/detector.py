# Archivo: src/detector.py

import json
import time
from datetime import datetime
from colorama import Fore, Style, init
from analizador import analizar_log, leer_logs

init()  # Inicializar colores en Windows

COLORES = {
    "CRITICO": Fore.RED,
    "ALTO": Fore.LIGHTRED_EX,
    "MEDIO": Fore.YELLOW,
    "BAJO": Fore.CYAN,
    "NORMAL": Fore.GREEN
}

def procesar_logs(ruta_logs="logs/sistema.log"):
    print(f"\n{'='*60}")
    print("  DETECTOR DE AMENAZAS CON IA - v1.0")
    print(f"{'='*60}\n")
    
    logs = leer_logs(ruta_logs)
    print(f"Analizando {len(logs)} eventos con IA...\n")
    
    resultados = []
    amenazas = []
    
    for i, log in enumerate(logs):
        print(f"Analizando evento {i+1}/{len(logs)}...", end="\r")
        
        try:
            respuesta_raw = analizar_log(log)
            analisis = json.loads(respuesta_raw)
            
            nivel = analisis.get("nivel_amenaza", "NORMAL")
            color = COLORES.get(nivel, Fore.WHITE)
            
            if nivel in ["CRITICO", "ALTO", "MEDIO"]:
                amenazas.append({
                    "log": log,
                    "analisis": analisis,
                    "timestamp": datetime.now().isoformat()
                })
                print(f"\n{color}[{nivel}]{Style.RESET_ALL} {analisis['tipo_ataque']}")
                print(f"  Log: {log[:80]}...")
                print(f"  → {analisis['explicacion']}")
                print(f"  Acción: {analisis['accion']}\n")
            
            resultados.append({"log": log, "analisis": analisis})
            time.sleep(0.5)  # Evitar límite de peticiones
            
        except Exception as e:
            print(f"\nError analizando log: {e}")
    
    guardar_reporte(resultados, amenazas)
    
    print(f"\n{'='*60}")
    print(f"  RESUMEN: {len(amenazas)} amenazas detectadas de {len(logs)} eventos")
    print(f"{'='*60}\n")

def guardar_reporte(resultados, amenazas):
    reporte = {
        "fecha_analisis": datetime.now().isoformat(),
        "total_eventos": len(resultados),
        "amenazas_detectadas": len(amenazas),
        "amenazas": amenazas
    }
    
    with open("reports/reporte.json", "w", encoding="utf-8") as f:
        json.dump(reporte, f, ensure_ascii=False, indent=2)
    
    print(f"\nReporte guardado en reports/reporte.json")

if __name__ == "__main__":
    procesar_logs()