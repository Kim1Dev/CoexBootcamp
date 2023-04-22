//Realiza una función que retorne la cantidad de los elementos del arreglo cuyo valor es mayor a 18.
//Escribe tu código aquí
Algoritmo retorno
	Definir tamaño, cant Como Entero;
	cant = 0;
	
	Escribir "Digite el numero de datos que va a ingresar";
	Leer tamaño
	
	Dimension array[tamaño];
	
	//Metodo largo pero detallado
	
	//Con este For ingresamos los datos al arreglo
//	Para i<-1 Hasta tamaño Con Paso 1 Hacer
//		Escribir "Digite el valor numero ", i, ": ";
//		Leer num;
//		array[i] = ConvertirANumero(num);
//	Fin Para
	
	//Con este arreglo validamos la condicion puesta
//	Para i<-1 Hasta tamaño Con Paso 1 Hacer
//		Si array[i] > 18 Entonces
//			cant = cant + 1;
//		Fin Si
//	Fin Para
	
	//Metodo corto
	
	//Con este For Ingresamos datos y evaluamos
	Para i<-1 Hasta tamaño Con Paso 1 Hacer
		Escribir "Digite el valor numero ", i, ": ";
		Leer num;
		array[i] = ConvertirANumero(num);
		Si array[i] > 18 Entonces
			cant = cant + 1;
		Fin Si		
	Fin Para
	
	//Imprimimos el resultado
	Escribir "";
	Escribir "Con un total de ", tamaño, " elementos, ", cant, " son mayor a 18";
FinAlgoritmo
