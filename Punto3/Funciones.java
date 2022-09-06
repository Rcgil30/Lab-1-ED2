package Punto3;

public class Funciones {
    Btree root;
    int t; //grado mínimo del árbol

    //Constructor 
    public Funciones(int t) {
        this.t = t; 
        root = new Btree(t); //nodo
    }
       
    //clave es la clave que queremos comparar, valga la redundancia y current es el nodo en el que nos encontramos
    private Btree BuscarClaveEnNodo(Btree current, int clave) {
        //para buscar y comparar, iniciamos con un contador desde la primera posición
        int i = 0; 
        //cuando acabe este ciclo, i estará ubicado en la clave que queremos (si es q existe)
        while ( clave > current.key[i] && i < current.Nclaves) { //current es el nodo en el q estoy
            i++;
        }
        if (i < current.Nclaves && clave == current.key[i]) { //comparamos si la clave es igual a la clave del nodo
            return current; //retornamos el nodo en donde se encuentra la clave
        } 
        //si no se retorna, quiere decir que debemos seguir buscando en sus hijos, pero primero se debe
        //ver si tiene hijos(nodo hoja o no), por lo que usamos .leaf que se ve vio anteriormente
        if (current.leaf){ 
            return null;  //si es nodo hoja eso quiere decir q no existe otro nodo que pueda contener nuestra clave a buscar
            //por ende, retornamos null 
        } else {
            //Si tiene hijos(no es hoja), hace un llamado recursivo y se repite de nuevo el proceso
            return BuscarClaveEnNodo(current.child[i], clave);
        }
    }
    
    //para crear nuestro árbol y probarlo
    public void InsertarMain(int key) {
        Btree r = root; //pa no perder la raíz
        //por definición de árboles b, la cantidad de claves en un nodo es 2t-1, entonces
        //con esto verificamos si el árbol está lleno, a manera de validación
        if (r.Nclaves == ((2 * t) - 1)) {
            Btree s = new Btree(t); //nodo
            root = s; 
            s.leaf = false;  
            s.child[0] = r; //el primer hijo, corresponde a lo de la raíz  
            s.Nclaves = 0; //cant de elements  0 
            DividirNodo(s, 0, r);  //por definición, si está lleno, se debe dividir el nodo, 
            //tendrá como parámetros los 2 nodos y mi pos
            InsertarNolleno(s, key);  //cuando ya se realice el proceso anterior, se procede a insertar de nuevo
        } else {
            InsertarNolleno(r, key);  //si no está lleno, entonces se inserta de manera normal
        }
    }
    public void ImprimirNodo(int num) {
        Btree node = BuscarClaveEnNodo(root, num);  //aqui buscamos el nodo que necesitamos para ver sus claves y compararlas
        //si node nos arroja un resultado, quiere decir que si hay un  nodo con esta clave
        if (node == null) { //si es null entonces no hay nodo con esa clave
            System.out.println("No existe nodo con esta clave");
        } else { //sino, que se imprima el nodo
            System.out.println("La clave se encontró en el sgt nodo");
            imprimir(node);
        }
    }
    //cuando se llena el nodo y se debe insertar, se realiza lo sgt
    private void DividirNodo(Btree node, int i, Btree p) {  
        //si se divide tendremos 2 nodos x y y 
        Btree c = new Btree(t);  //creamos un nodo temporal con el mismo grado mínimo
        c.leaf = p.leaf; //mi nodo temp tendrá las mismas características
        c.Nclaves = (t - 1); //pero la cant de claves será de t-1
        //Copia las ultimas (t - 1) claves del nodo y al inicio del nodo z     
        for (int j = 0; j < (t - 1); j++) {
            c.key[j] = p.key[(j + t)]; //en este for lo que se busca es escribir los ult
            //valores de p al inicio de c
        }
        if (!p.leaf) {  //si no es hoja, toca ver los hijos 
            for (int k = 0; k < t; k++) {
                c.child[k] = p.child[(k + t)];
            }
        }                                           
        p.Nclaves = (t - 1);  //claramente debemos colocar el nuevo valor de p                                                                            
        //movemos los hijos de node para meter el node c
        for (int j = node.Nclaves; j > i; j--) {
            node.child[(j + 1)] = node.child[j];
        }
        //Por lo que a nuestro nodo le asignamos en la pos i + 1 le asignamos el node c                           
        node.child[(i + 1)] = c;                                                 
        for (int j = node.Nclaves; j > i; j--) {
            node.key[(j + 1)] = node.key[j]; //acomodamos las claves
        }
        //agregamos el valor al node en la pos q necesitamos                                 
        node.key[i] = p.key[(t - 1)];                                             
        node.Nclaves++;                                                                  
    }
    
    //Función que me inserta un nodo
    private void InsertarNolleno(Btree node, int key) {
        //Si es una hoja
        if (node.leaf) {
            //En i se guardará la cantidad de claves del nodo para que después nos diga la pos a insertar el val
            int i = node.Nclaves; 
            //buscamos la posición para insertar el valor
            while (i >= 1 && key < node.key[i - 1]) { //si la clave es menor al último valor q ya existe en el nodo
                //movemos los val
                node.key[i] = node.key[i - 1];
                //i se le restará el val
                i--; 
            }
            //aqui ya insertamos, es decir, incluimos la clave en nuestro nodo, lo cual tambien implica aumentarle 
            //el número de claves ya que aumenta la cantidad de elementos
            node.key[i] = key;
            node.Nclaves++; 
        } else { //si mi nodo no es hoja implica buscar el hijo correcto donde insertar
            int m = 0;
            while (m < node.Nclaves && key > node.key[m]) {//buscamos al hijo, hasta que la clave no sea mayor a nuestro elemento
                m++;
            }
            //Aquí se realiza una validación para ver si el hijo ya está lleno
            //recordando la definicion de 2t-1
            if (node.child[m].Nclaves == (2 * t - 1)) { 
                DividirNodo(node, m, node.child[m]); //si lo está entonces se divide el nodo
                if (key > node.key[m]) { //vemos si nuestra key es mayor a la del nodo
                    m++; //por ende se incrementa el valor de m
                }
            }
            InsertarNolleno(node.child[m], key); //llamamos de forma recursiva la función para que 
            //se inserte de forma correcta
        }
    }
    //imprimimos en preorder
    private void imprimir(Btree n) {
        n.PrintClaves();
        //ver si no es hoja el nodo
        if (!n.leaf) {
            //si no lo es, se mira si tiene hijos
            for (int j = 0; j <= n.Nclaves; j++) {
                if (n.child[j] != null) {
                    System.out.println();
                    imprimir(n.child[j]);
                }
            }
        }
    }
    public void mostrarBtree() {
        imprimir(root);  //con este metodo imprimimos el árbol y ya 
    }
}

