import pandas as pd

# Crear los datos para Gr1
data_gr1 = {
    'Sexo': ['Mujer', 'Hombre', 'Mujer', 'Mujer', 'Mujer', 'Hombre', 'Mujer', 'Hombre', 'Hombre', 'Mujer',
             'Mujer', 'Hombre', 'Hombre', 'Mujer', 'Mujer', 'Hombre', 'Mujer', 'Mujer', 'Mujer', 'Mujer'],
    'Edad': [25, 30, 28, 20, 23, 22, 22, 22, 21, 21, 22, 20, 22, 29, 29, 21, 30, 21, 22, 23],
    'Estatura': [1.82, 1.83, 1.78, 1.79, 1.80, 1.90, 1.79, 1.83, None, 1.65, 1.73, 1.79, 1.80, 1.77, 1.69, 1.75, 1.66, None, 1.79, 1.80],
    'Grupo Sanguíneo': ['A', 'B', 'A', 'AB', 'O', 'A', 'B', 'A', 'B', 'AB', 'A', 'B', 'O', 'O', 'A', 'B', 'AB', 'B', 'B', 'B']
}

# Crear el DataFrame
df_gr1 = pd.DataFrame(data_gr1)

# Crear los datos para Gr2
data_gr2 = {
    'Sexo': ['Mujer', 'Hombre', 'Hombre', 'Mujer', 'Hombre', 'Hombre', 'Mujer', 'Hombre', 'Hombre', 'Mujer',
             'Mujer', 'Hombre', 'Hombre', 'Mujer', 'Hombre', 'Hombre', 'Mujer', 'Hombre', 'Mujer', 'Hombre'],
    'Edad': [25, 30, 38, 26, 23, 22, 32, 26, 25, 28, 22, 30, 22, 39, 29, 25, 30, 23, 32, 33],
    'Estatura': [1.72, 1.73, 1.78, 1.79, 1.83, 1.90, 1.79, 1.83, None, 1.75, 1.79, 1.79, 1.85, None, 1.77, 1.79, 1.66, None, 1.79, 1.83],
    'Grupo Sanguíneo': ['B', 'B', 'A', 'AB', 'O', 'AB', 'B', 'B', 'B', 'AB', 'A', 'B', 'O', 'O', 'B', 'B', 'A', 'O', 'B', 'B']
}

# Crear el DataFrame
df_gr2 = pd.DataFrame(data_gr2)
import matplotlib.pyplot as plt

# Función para crear un diagrama de sectores
def plot_pie_chart(df, group_name):
    counts = df['Grupo Sanguíneo'].value_counts()
    plt.figure(figsize=(8, 6))
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140, colors=['blue', 'yellow', 'pink', 'green'])
    plt.title(f'Diagrama de Sectores - Grupo {group_name}')
    plt.axis('equal')  # Para que el gráfico sea un círculo
    plt.show()

# Crear gráficos para ambos grupos
plot_pie_chart(df_gr1, 'A')
plot_pie_chart(df_gr2, 'B')
def plot_histogram(df, group_name):
    plt.figure(figsize=(8, 6))
    plt.hist(df['Estatura'].dropna(), bins=10, color='skyblue', edgecolor='black')
    plt.title(f'Histograma de Estatura - Grupo {group_name}')
    plt.xlabel('Estatura (m)')
    plt.ylabel('Frecuencia')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

# Crear histogramas para ambos grupos
plot_histogram(df_gr1, 'A')
plot_histogram(df_gr2, 'B')
def detect_outliers_edad(df, group_name):
    Q1 = df['Edad'].quantile(0.25)
    Q3 = df['Edad'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df['Edad'] < lower_bound) | (df['Edad'] > upper_bound)]

    print(f'Datos atípicos en la variable Edad - Grupo {group_name}:')
    print(outliers[['Sexo', 'Edad']])

# Detectar datos atípicos para ambos grupos
detect_outliers_edad(df_gr1, 'A')
detect_outliers_edad(df_gr2, 'B')
def calculate_values_estatura(df_a, df_b):
    # Grupo A
    estaturas_a = df_a['Estatura'].dropna().sort_values()
    max_40_percent_a = estaturas_a.quantile(0.4)

    # Grupo B
    estaturas_b = df_b['Estatura'].dropna().sort_values(ascending=False)
    min_30_percent_b = estaturas_b.quantile(0.3)

    print
