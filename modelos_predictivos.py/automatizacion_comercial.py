import pandas as pd
import numpy as np
from datetime import datetime

print("iniciando pepeline de automatizacion comercial")

data_inventario ={
    'id_producto': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'nombre': ['Pintura Latex 20L', 'Rodillo Pro', 'Cinta de Enmascarar', 'Enduido 10L', 'Pincel Fino'],
    'stock_actual': [15, 8, 120, 5, 50],
    'ventas_promedio_diarias': [2.5, 1.0, 15.0, 3.0, 2.0],
    'costo_proveedor': [12000, 1500, 800, 5000, 400],
    'precio_venta': [18000, 3000, 1200, 6500, 1000]
}
df = pd.DataFrame(data_inventario)
#¿Cuántos días nos quedan antes de quedarnos sin mercadería?
df["dias_stock_restante"] = np.floor(df["stock_actual"] / df["ventas_promedio_diarias"])
#¿Cuánta plata limpia nos deja cada producto?
df["ganancia_neta"] = df["precio_venta"] - df["costo_proveedor"]
df['margen_porcentaje'] = np.round((df['ganancia_neta'] / df['precio_venta']) * 100, 2)

#motor de alertas
def generar_alerta(row):
    alertas =[]
    if row["dias_stock_restante"] <= 7:
        alertas.append("QUIEBRE INMINENTE: Recomprar urgente al proveedor.")
    if row ["margen_porcentaje"] < 30:
        alertas.append(" MARGEN BAJO: Subir precio o cambiar proveedor.")
    if not alertas:
        alertas.append(" Todo en orden. Negocio sano.")
    return "|". join(alertas)

#aplicamos motor de reglas 
df["accion_requerida"] = df.apply(generar_alerta, axis=1)

#exportacion de reporte gerencial
fecha_hoy = datetime.now(). strftime("%Y-%m-%d")
nombre_archivo = f"alertas_gerencia_{fecha_hoy}.csv"

#filtramos lo urgente
df_urgente= df[df["accion_requerida"] !="todo en orden. Negocio sano"]

print("\n REPORTE DE ALERTAS CRÍTICAS PARA GERENCIA:")
print("-" * 60)
print(df_urgente[['nombre', 'dias_stock_restante', 'margen_porcentaje', 'accion_requerida']])
print("-" * 60)

# Guardamos el archivo final que se enviaría por mail o sistema
df.to_csv(nombre_archivo, index=False, encoding='utf-8')
print(f"\n Automatización finalizada con éxito. Archivo generado: {nombre_archivo}")
               


       

    

   
