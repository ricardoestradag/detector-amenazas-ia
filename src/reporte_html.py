
import json
from datetime import datetime

def generar_html():
    with open("../reports/reporte.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
    
    amenazas = datos.get("amenazas", [])
    total = datos.get("total_eventos", 0)
    n_amenazas = datos.get("amenazas_detectadas", 0)
    
    filas = ""
    colores = {"CRITICO":"#FCEBEB","ALTO":"#FAEEDA","MEDIO":"#FAEEDA","BAJO":"#E6F1FB","NORMAL":"#EAF3DE"}
    
    for a in amenazas:
        nivel = a["analisis"]["nivel_amenaza"]
        bg = colores.get(nivel, "#f5f5f5")
        filas += f"""
        <tr style="background:{bg}">
          <td style="padding:8px 12px;font-family:monospace;font-size:12px">{a['log'][:70]}...</td>
          <td style="padding:8px 12px;font-weight:500">{nivel}</td>
          <td style="padding:8px 12px">{a['analisis']['tipo_ataque']}</td>
          <td style="padding:8px 12px;font-size:13px">{a['analisis']['explicacion']}</td>
        </tr>"""
    
    html = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8">
<title>Detector de Amenazas - Reporte</title>
<style>
  body{{font-family:system-ui,sans-serif;margin:0;padding:2rem;background:#f8f8f8;color:#111}}
  h1{{font-size:22px;font-weight:500;margin-bottom:4px}}
  .sub{{color:#666;font-size:13px;margin-bottom:2rem}}
  .stats{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:2rem}}
  .stat{{background:#fff;border:0.5px solid #e0e0e0;border-radius:10px;padding:1rem}}
  .stat-n{{font-size:28px;font-weight:500}}
  .stat-l{{font-size:12px;color:#666;margin-top:4px}}
  table{{width:100%;border-collapse:collapse;background:#fff;border-radius:10px;overflow:hidden;border:0.5px solid #e0e0e0}}
  th{{background:#f0f0f0;padding:10px 12px;text-align:left;font-size:12px;font-weight:500;text-transform:uppercase;letter-spacing:.06em;color:#555}}
  tr{{border-bottom:0.5px solid #eee}}
</style></head><body>
<h1>Reporte de Detección de Amenazas</h1>
<p class="sub">Generado el {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} · Análisis con IA (GPT-4o-mini)</p>
<div class="stats">
  <div class="stat"><div class="stat-n">{total}</div><div class="stat-l">Eventos analizados</div></div>
  <div class="stat"><div class="stat-n" style="color:#A32D2D">{n_amenazas}</div><div class="stat-l">Amenazas detectadas</div></div>
  <div class="stat"><div class="stat-n">{round(n_amenazas/total*100) if total>0 else 0}%</div><div class="stat-l">Tasa de detección</div></div>
</div>
<table><thead><tr>
  <th>Evento</th><th>Nivel</th><th>Tipo de ataque</th><th>Análisis IA</th>
</tr></thead><tbody>{filas}</tbody></table>
</body></html>"""
    
    with open("../reports/reporte.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Dashboard HTML generado: reports/reporte.html")

if __name__ == "__main__":
    generar_html()
