package Punto3;

public class Btree {
    //array de claves
    int key[]; 
    //Num de claves por nodo
    int Nclaves; 
    //array de hijos
    Btree child[]; 
    //para ver si es hoja, lo cual se usará mas adelante
    boolean leaf; 
    
    //Constructor
    public Btree(int t) {
        key = new int[((2 * t) - 1)];  //los nodos tiene un máx de claves 2t-1
        child = new Btree[(2 * t)];  //cada nodo soporta máximo 2t hijos, por definción 
        leaf = true; 
        Nclaves = 0;  
    }

    public void PrintClaves() { //esto es una manera simple de guiarnos al momento de imprimir los nodos
        for (int i = 0; i < Nclaves; i++) {  //se imprime cada clave del nodo
            if (i < Nclaves - 1) {  //imprimimos las claves, hasta la penultima Nclaves - 1 para que no quede la coma
                System.out.print(key[i] + " , ");
            } else {  //aquí se imprime la última, sin la coma :D
                System.out.print(key[i]);
            }
        }
    }
}