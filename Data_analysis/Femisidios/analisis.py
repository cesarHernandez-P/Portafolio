
import pandas as pds
from tabulate import tabulate

#* para graficos
import seaborn as sns
import matplotlib.pyplot as plt

#TODOS para abrir archivos con extension xlsx se instalalo la libreria openpyxl 

dataFrame = pds.read_excel('data/vcm-femicidiossegunregion2013-2014.xlsx' , engine='openpyxl') #?para abrir archivos xlsx

#ver los datos  formato tabulares
print ( tabulate (dataFrame.head(50), headers='keys', tablefmt='psql'))
print(dataFrame.columns.tolist())

#TODOS visualizacion

# Transformar a formato largo para comparar años
df_melt = dataFrame.melt(id_vars='Región', value_vars=[2013,2014], var_name='Año', value_name='Femicidios')

# Estilo y paleta
sns.set_style("whitegrid")
sns.set_palette("pastel")

# Tamaño de figura
plt.figure(figsize=(14,6))

# Gráfico de barras
sns.barplot(data=df_melt, x='Región', y='Femicidios', hue='Año')

plt.xticks(rotation=45)
plt.title('Femicidios según Región - 2013 vs 2014', fontsize=16)
plt.ylabel('Número de Femicidios', fontsize=12)
plt.xlabel('Región', fontsize=12)
plt.legend(title='Año')
plt.tight_layout()
plt.show()


