package laboratorio4;
/**
 * @autor Daniel Felipe Gomez Martinez
 * @autor Daniel Garcia Garcia
 * @autor Cesar Andres Garcia
 * 
 **/

import java.util.ArrayList;

public class HeldKarp {
     

    static String Binario = ""; 
    /*Variable estatica para determinar el número en binario que corresponde a cada uno de los cunjuntos potencia (Mascara
    para la programacion)*/

    /**
     *  Método que muestra la matriz de costos totales ya calculados
     * @param g Grafo dado
     * @param costos arreglo de costos parciales o bien sea el caso de costos totales
     **/
    public static void mostrar(Digraph g, int[][] costos) {
        int n = g.size();
        int pot = ((int) Math.pow(2, n)) / 2;
        for (int i = n - 1; i >= 0; i = i - 1) {
            for (int j = 0; j < pot; j++) {
                System.out.print(costos[i][j] + "         ");
            }
            System.out.println();
        }
    }
    
    
    /**
     * Método para crear un número en binario correspondiente a una celda a visitar para calcular el costo minimo por medio de HeadKarp
     * @param value valor a convertir en binario
     * @return arreglo de tipo char con los valores del número en binario
     **/

    public static char[] Binario(int value) {
        if (value / 2 != 0) {
            Binario = Integer.toString(value % 2) + Binario;
            value = value / 2;
            Binario(value);
        } else {
            Binario = Integer.toString(value) + Binario;
        }
        if (Binario.length() == 1) {
            Binario = "00" + Binario;
        } else if (Binario.length() == 2) {
            Binario = "0" + Binario;
        }
        return Binario.toCharArray();
    }
    
    
    /**
     * Metodo auxiliar
     **/
    public static int construirBinario(int value){
        String cadena = "";
        if(value == 1){
            cadena = "001";
        }else if(value == 2){
            cadena = "010";
        }else if(value == 3){
            cadena = "100";
        }
        return Integer.parseInt(cadena);
    }

    
    /**
     * Método para convertir un binario a decimal
     **/
    public static int binaryToDecimal(int number) {
        int decimal = 0;
        int binary = number;
        int power = 0;
 
        while (binary != 0) {
            int lastDigit = binary % 10;
            decimal += lastDigit * Math.pow(2, power);
            power++;
            binary = binary / 10;
        }
        return decimal;
    }

    /**
     * Método para resetear la variable estatica de Binario, debido a que es necesario encontrar varios binarios
     **/
    public static void reset() {
        Binario = "";
    }

    /**
     * M´étodo que calcula el costo de un subconjunto del conjunto potencia del grafo con todos los otros nodos del grafo
     **/
    public static int determinarCosto(int salida, int entrada, Digraph g, int[][] costos) {
        
        ArrayList<Integer> pos2 = new ArrayList<>(); //Arreglo auxiliar con el fin de determinar por que veritices del grafo se esta pasando (mascara en binario)
       
        char[] aux = Binario(entrada); // Se hace el número en vinario del subconjunto que se esta analizando (arreglo en char9
        int tam = aux.length;
        
        int[] auxInt = new int[tam]; // Arreglo en entero del numero en binario
        
        for(int i = 0; i < auxInt.length; i++){
            auxInt[i] = Integer.valueOf(Character.toString(aux[i]));
        }
        
        int cost = 0; //Variable del costo parcial
        
        for(int i = 0; i < tam; i++){
            if(auxInt[i] == 1){
                if(i == 0){
                    pos2.add(3);
                }else if(i == 1){
                    pos2.add(2);
                }else if(i == 2){
                    pos2.add(1);
                }
            }
        }
        //Condiciones para el peso
        /****
         * Condicion 1 y 2) para ahorrar tiempo y memoria, todo costo que se tenga que calcular de la forma [a, {b,a}] se ignora debido a que calcular el costo de 
         * un trayecto que pase por un punto dos veces es ineficiente y costoso (esto a excepcion del ultimo caso es necesario ir del nodo 0 al nodo 0 pasando por todos los otros vertices)
         * Condicion 3) si el subconjunto del conjunto potencia solo tiene un elemento se calcula el costo desde el nodo 0 a este y de este al que se desea llegar
         * por medio de la funcion getWeight de los grafos
         * condicion 4) Si el subconjunto del conjunto potencia tiene dos elementos, se calcula el minimo entre el costo desde el nodo 0 a cada uno y de cada uno al nodo de llegada
         * condicion 5) Si el subconjunto del conjunto potencia tiene tres elementos, se hace el mismo proceso que en la condicion 4
         */
        if(salida == 0 && entrada != 7){
            cost = 0;
        }else if(pos2.contains(salida)){
            cost = 0;
        }else if(pos2.size() == 1){    
            cost = g.getWeight(0, pos2.get(0)) + g.getWeight(pos2.get(0), salida);
        }else if (pos2.size() == 2){
            cost = Math.min(g.getWeight(pos2.get(0), salida) + costos[pos2.get(0)][binaryToDecimal(construirBinario(pos2.get(1)))], g.getWeight(pos2.get(1), salida) + costos[pos2.get(1)][binaryToDecimal(construirBinario(pos2.get(0)))]);
        }else if(pos2.size() == 3){
            cost = Math.min(Math.min(g.getWeight(pos2.get(0), salida) + costos[3][3], g.getWeight(pos2.get(1), salida) + costos[2][5]), g.getWeight(pos2.get(2), salida) + costos[1][6]);
        }
        reset(); //Se resetea la bariable binario para posteriores analisis 
        return cost; //Se retorna el costo calculado
    }
    
    
    /* Método auxiliar que inicializa las matrices de costos
     * @param grafo dado
     * @return  costo mínimo del recorrido que pasa por todos los vértices solo una vez y vuelve al nodo inicial.
     */

    public static int HeldKarp(Digraph g) {
        int n = g.size();
        int pot = (((int) Math.pow(2, n)) / 2);
        /**Se crea la matriz de costos de tamaño N * pot, donde N es el número de elementos del grafo y pot corresponde a la cantidad de 
        *subconjunto del conjunto potencia, cabe destacar que es necesario dividir esta cantidad entre dos debido a que:
        * Se comienza del nodo 0 por defecto, por ende se descartan los subconjuntos del conjunto potencia en los que se encuentra el nodo 0, 
        * a excepcion del subconjunto {0}. Esto es Cardinalidad conjunto potencia sobre 2
        **/
        int[][] costos = new int[n][pot];

        // Se colocan los costos al ir del nodo 0 a todos los demasn nodos
        for (int i = n - 1; i >= 0; i = i - 1) {
            costos[i][0] = g.getWeight(0, i);
        }
        // Se llama al metodo que calcula los costos
        return HeldKarpCosto(g, costos, 0, pot - 1);
    }

     /**
     * Metodo que llama al metodo que calcula un determinado costo
     * @param g grafo dado
     * @param costos arreglo de costos
     * @param destino destino final (Nodo 0)
     * @return costo minimo es decir, el costo de ir del nodo 0 al nodo 0 pasando por el subconjunto {1,2,3}
     **/
    public static int HeldKarpCosto(Digraph g, int[][] costos, int destino, int potencia) {
        /**
         * NOTA: Cabe destacar que si se hace el recorrido por columnas y no por filas, solo se requiere de dos cilos anidados y no de 6 como se verá
         * acontinuación
         **/
        /**
         * Llenar las promeras 2 columnas de la matriz
         **/
            for (int i = costos.length - 1; i >= 0; i--) {
                for (int j = 1; j <= 2; j++) {
                    costos[i][j] = determinarCosto(i, j, g, costos);
                }
            }
            /**
             * Llenar las siguientes dos columnas
             **/
            for (int i = costos.length - 1; i >= 0; i--) {
                for (int j = 3; j < 5; j++) {
                    costos[i][j] = determinarCosto(i, j, g, costos);
                }
            }
            /****
             * Llenas las ultimas columnas de la amtriz
             */
            for (int i = costos.length - 1; i >= 0; i--) {
                for (int j = 5; j < costos[i].length; j++) {
                    costos[i][j] = determinarCosto(i, j, g, costos);
                }
            }
            /****
             * mostrar la matriz final
             */
        //mostrar(g, costos);
        // Valor a retornar
        return costos[0][7];
    }
}
