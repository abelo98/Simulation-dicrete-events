#### Especificaciones :

- Al iniciar la simulación se le introduce en una aplicación de consola que recibe la cantidad de simulaciones que desea realizar y la cantidad de trabajadores extra a utilizar en las horas pico. Por defecto son 1000 simulaciones y 1 solo trabajador extra. Además se le pedirá introducir una lista que contenga los diferentes valores de lambda con los que simular las llegadas de los clientes en horas normales y otra para horas pico. por defecto es arrive = 1/5,1/9,1/13 y 
rushHour = 1/2,1/2,1/2. Estas listas deben tener el mismo tamaño y las fracciones deben estar separadas por coma sin dejar espacios.
- La salida está redirigida hacia un archivo output.txt donde podrá examinar los resultados una vez concluida la simulación.
-  Versión de Python utilizada: 3.8.10 64 bit.
-  Bibliotecas empleadas: fractions, numpy, sys.
-  simulation es un pdf con el resultado de la simulación que se analiza en las recomendaciones.
-  El archivo Console.py contiene la lógica de la consola y en Stats.py es donde se analizan los resultados de las simulaciones.

