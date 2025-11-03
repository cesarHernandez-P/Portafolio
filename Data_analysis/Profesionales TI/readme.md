{\rtf1\ansi\ansicpg1252\cocoartf2865
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # \uc0\u55358 \u56800  An\'e1lisis de Datos con Python \'97 Profesionales TI en Latinoam\'e9rica\
\
Este proyecto tiene como objetivo practicar **an\'e1lisis de datos, visualizaci\'f3n y storytelling** con un dataset simulado de **profesionales del \'e1rea TI en Latinoam\'e9rica**.  \
Contiene variables como pa\'eds, edad, experiencia, nivel de ingl\'e9s, satisfacci\'f3n laboral, sueldo, y m\'e1s.\
\
---\
\
## \uc0\u55357 \u56522  Dataset\
\
**Archivo:** `profesionales_ti_latam.csv`  \
**Filas:** 500  \
**Columnas:** 14  \
\
Cada fila representa a un profesional TI de la regi\'f3n, con atributos demogr\'e1ficos, laborales y t\'e9cnicos.\
\
Ejemplo de columnas:\
- `pais`\
- `region`\
- `edad`\
- `experiencia_anios`\
- `sueldo_mensual_usd`\
- `nivel_estudios`\
- `lenguaje_principal`\
- `modo_trabajo`\
- `satisfaccion_laboral`\
- `uso_ai_en_trabajo`\
\
---\
\
## \uc0\u55358 \u56809  1. Limpieza y preparaci\'f3n de datos\
\
**Objetivo:** Dejar el dataset listo para an\'e1lisis.\
\
**Tareas sugeridas:**\
- Detectar valores nulos y decidir c\'f3mo tratarlos (`fillna`, `dropna`).\
- Identificar y eliminar duplicados.\
- Corregir tipos de datos (`astype`, `to_datetime` si agregas fechas).\
- Filtrar registros (ej: solo \'93Chile\'94 o solo \'93Remoto\'94).\
- Crear una nueva columna de **rango etario** (ej. 20\'9630, 31\'9640, etc.).\
\
---\
\
## \uc0\u55357 \u56520  2. An\'e1lisis estad\'edstico b\'e1sico\
\
**Objetivo:** Explorar las variables num\'e9ricas y categ\'f3ricas.\
\
**Ejercicios sugeridos:**\
- Calcular la media, mediana y desviaci\'f3n est\'e1ndar de los sueldos.\
- Obtener la correlaci\'f3n entre edad y sueldo.\
- Ver la distribuci\'f3n de la satisfacci\'f3n laboral.\
- Contar cu\'e1ntos profesionales trabajan con IA (`uso_ai_en_trabajo`).\
\
\uc0\u55357 \u56536  *Tip:* Usa `data.describe()`, `data['columna'].mean()`, `data.corr()`.\
\
---\
\
## \uc0\u55356 \u57256  3. Visualizaci\'f3n con Seaborn y Matplotlib\
\
**Objetivo:** Comunicar informaci\'f3n de forma clara y atractiva.\
\
**Gr\'e1ficos recomendados:**\
| Gr\'e1fico | Ideal para | Ejemplo |\
|----------|-------------|----------|\
| `histplot()` | Distribuci\'f3n de edades o sueldos | `sns.histplot(data, x='edad', kde=True)` |\
| `boxplot()` | Comparar sueldos entre pa\'edses | `sns.boxplot(x='pais', y='sueldo_mensual_usd', data=data)` |\
| `barplot()` | Promedios por grupo | `sns.barplot(x='nivel_estudios', y='sueldo_mensual_usd', data=data, estimator='mean')` |\
| `heatmap()` | Correlaciones | `sns.heatmap(data.corr(), annot=True)` |\
\
\uc0\u55356 \u57256  Mejora est\'e9tica:\
```python\
sns.set_style("whitegrid")\
sns.set_palette("muted")\
plt.figure(figsize=(10,6))\
}