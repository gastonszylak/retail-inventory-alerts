# modelo_comercio
# 🚀 Pipeline de Automatización Comercial y Alertas de Inventario

Este proyecto es una solución de Inteligencia de Negocios (Business Intelligence) construida en Python. Su objetivo es automatizar el control de inventario y la rentabilidad de productos, pasando de datos operativos crudos a decisiones gerenciales accionables en segundos.

## 🎯 Problema de Negocio a Resolver
Los negocios retail y las pymes suelen perder rentabilidad por dos motivos críticos:
1. **Quiebres de stock:** Quedarse sin mercadería de alta rotación.
2. **Márgenes invisibles:** Vender productos que, al restar el costo del proveedor, no generan el margen de ganancia esperado.

## 💡 Solución Implementada
Desarrollé un script que ingesta la base de datos del inventario y procesa la información de forma automática para generar un **Reporte de Acción Urgente**. 

### 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python
* **Librerías:** `pandas` (Data Wrangling), `numpy` (Cálculo matemático), `datetime` (Marcas de tiempo).

### ⚙️ Funcionalidades Clave
1. **Cálculo de KPIs Financieros:** El sistema calcula automáticamente la Ganancia Neta y el Margen de Rentabilidad Porcentual por cada producto.
2. **Proyección de Demanda:** Calcula los días exactos de stock restante basándose en el promedio de ventas diarias históricas.
3. **Motor de Reglas de Negocio:** Evalúa los datos contra umbrales comerciales y clasifica la urgencia:
   * ⚠️ *Alerta de Quiebre:* Si quedan 7 días o menos de inventario.
   * 📉 *Alerta de Margen:* Si la rentabilidad cae por debajo del 30%.
4. **Generación de Reportes Automáticos:** Filtra los productos sanos y exporta únicamente las urgencias a un archivo `.csv` fechado, listo para ser enviado a Gerencia.

## 🚀 Cómo ejecutar el proyecto

1. Clonar este repositorio:
   ```bash
   git clone https://github.com/gastonszylak/retail-inventory-alerts.git
