package Punto3;

public class Main {
    public static void main(String[] args) {
        int t = 6; //en nuestro caso le daremos un valor de grado minimo de 6
        Funciones B = new Funciones(t); //creamos el árbol
        //creamos un array con las claves a ingresar por nodo, para crear nuestro árbol y poder desarrollar el punto 
        int[] keys = {1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,19,18,20,21,22,23,24,25};
        for(int i=0; i<keys.length; i++) {  //con este for insertamos 1 a 1 las claves
            B.InsertarMain(keys[i]);  //insertar se encuentra en Funciones.java
        }
        //Imprimimos el árbol en preorder 
        System.out.println("Árbol B:");
        B.mostrarBtree();
        System.out.println("\nLa clave a buscar en el árbol es 15");
        B.ImprimirNodo(15);  //aquí se realiza el proceso para buscar la clave e imprimir el resultado
        System.out.println("\nlaboratorio realizado por Roberto Gil, María C. Gómez y Darwin Charris");
    }
}
