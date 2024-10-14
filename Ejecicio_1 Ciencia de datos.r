# Primero se crea el conjunto de datos

set.seed(123) 
sexo <- sample(c("Masculino", "Femenino"), 30, replace = TRUE)
edad <- sample(18:25, 30, replace = TRUE)
estatura <- round(rnorm(30, mean = 170, sd = 10), 1)  # Media 170 cm, sd 10 cm
nota <- sample(1:5, 30, replace = TRUE)
ciudad <- sample(c("Medellin", "Bucaramanga", "Tulua"), 30, replace = TRUE)
# Una vez explicito lo que queremos mostrar, se crea la estructura de los datos que queremos tabular
estudiantes <- data.frame(Sexo = sexo, Edad = edad, Estatura = estatura, Nota = nota, Ciudad = ciudad)
print(estudiantes)

# Realizar una tabla de frecuencias absolutas y otra de frecuencias relativas para la variable Calificación. Almacena las tablas anteriores en dos variables y llámalas absolutas y relativas.
absolutas <- table(estudiantes$Nota)
relativas <- prop.table(absolutas)
print(absolutas)
print(relativas)

#Representar la variable ciudad mediante un diagrama de barras y un diagrama de sectores Incluye un título adecuado para cada gráfico y colorea las barras y los sectores de colores diferentes.
barplot(table(estudiantes$Ciudad), 
        main = "Ciudades", 
        col = rainbow(length(unique(estudiantes$Ciudad))),
        xlab = "Ciudad", 
        ylab = "Frecuencia")

# Diagrama de sectores
pie(table(estudiantes$Ciudad), 
    main = "Sectores de Ciudades", 
    col = rainbow(length(unique(estudiantes$Ciudad))))

# Para la variable Edad, realizar un histograma y un diagrama de caja y bigotes considerando la opción range = 1.5. Incluye un título apropiado para cada gráfico y colorea las barras del histograma de color amarillo. ¿Existe algún valor atípico en esta variable? Reduce el valor del argumento range hasta 0.5. ¿Varían las conclusiones ?
hist(estudiantes$Edad, 
     main = "Histograma de Edad", 
     xlab = "Edad", 
     col = "yellow", 
     border = "black")

boxplot(estudiantes$Edad, 
        main = "Diagrama de Caja de Edad", 
        ylab = "Edad", 
        range = 1.5)

# Realizar un resumen de la variable Puntuación mediante la orden summary.Comprueba que las medidas que proporciona summary coinciden con las medidas calculadas de forma individual usando su función específica

resumen_nota <- summary(estudiantes$Nota)
print(resumen_nota)

# Medidas manuales
media_nota <- mean(estudiantes$Nota)
mediana_nota <- median(estudiantes$Nota)
varianza_nota <- var(estudiantes$Nota)
desviacion_nota <- sd(estudiantes$Nota)

# Resultados
cat("Media:", media_nota, "\n")
cat("Mediana:", mediana_nota, "\n")
cat("Varianza:", varianza_nota, "\n")
cat("Desviación estándar:", desviacion_nota, "\n")

media_estatura <- mean(estudiantes$Estatura)

# Medidas de dispersión
varianza_estatura <- var(estudiantes$Estatura)
desviacion_estatura <- sd(estudiantes$Estatura)

# Imprimir resultados
cat("Media de Estatura:", media_estatura, "\n")
cat("Varianza de Estatura:", varianza_estatura, "\n")
cat("Desviación estándar de Estatura:", desviacion_estatura, "\n")




