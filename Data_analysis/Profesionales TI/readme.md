# 🧠 Análisis de Datos con Python — Profesionales TI en Latinoamérica

Este proyecto tiene como objetivo practicar **análisis de datos, visualización y storytelling** con un dataset simulado de **profesionales del área TI en Latinoamérica**.  
Contiene variables como país, edad, experiencia, nivel de inglés, satisfacción laboral, sueldo, y más.

---

## 📊 Dataset

**Archivo:** `profesionales_ti_latam.csv`  
**Filas:** 500  
**Columnas:** 14  

Cada fila representa a un profesional TI de la región, con atributos demográficos, laborales y técnicos.

Ejemplo de columnas:
- `pais`
- `region`
- `edad`
- `experiencia_anios`
- `sueldo_mensual_usd`
- `nivel_estudios`
- `lenguaje_principal`
- `modo_trabajo`
- `satisfaccion_laboral`
- `uso_ai_en_trabajo`

---

## 🧩 1. Limpieza y preparación de datos

**Objetivo:** Dejar el dataset listo para análisis.

**Tareas sugeridas:**
- Detectar valores nulos y decidir cómo tratarlos (`fillna`, `dropna`).
- Identificar y eliminar duplicados.
- Corregir tipos de datos (`astype`, `to_datetime` si agregas fechas).
- Filtrar registros (ej: solo “Chile” o solo “Remoto”).
- Crear una nueva columna de **rango etario** (ej. 20–30, 31–40, etc.).

---

## 📈 2. Análisis estadístico básico

**Objetivo:** Explorar las variables numéricas y categóricas.

**Ejercicios sugeridos:**
- Calcular la media, mediana y desviación estándar de los sueldos.
- Obtener la correlación entre edad y sueldo.
- Ver la distribución de la satisfacción laboral.
- Contar cuántos profesionales trabajan con IA (`uso_ai_en_trabajo`).

📘 *Tip:* Usa `data.describe()`, `data['columna'].mean()`, `data.corr()`.

---

## 🎨 3. Visualización con Seaborn y Matplotlib

**Objetivo:** Comunicar información de forma clara y atractiva.

**Gráficos recomendados:**
| Gráfico | Ideal para | Ejemplo |
|----------|-------------|----------|
| `histplot()` | Distribución de edades o sueldos | `sns.histplot(data, x='edad', kde=True)` |
| `boxplot()` | Comparar sueldos entre países | `sns.boxplot(x='pais', y='sueldo_mensual_usd', data=data)` |
| `barplot()` | Promedios por grupo | `sns.barplot(x='nivel_estudios', y='sueldo_mensual_usd', data=data, estimator='mean')` |
| `heatmap()` | Correlaciones | `sns.heatmap(data.corr(), annot=True)` |

🎨 Mejora estética:
```python
sns.set_style("whitegrid")
sns.set_palette("muted")
plt.figure(figsize=(10,6))
