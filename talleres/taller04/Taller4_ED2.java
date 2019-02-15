package taller4_ed2;

import java.util.ArrayList;

/**
 *
 * @author Juan Sebastián Pérez Salazar
 * @author Yhoan Alejandro Guzman Garcia
 */
public class Taller4_ED2 {

    /**
     * Metodo auxiliar para llamar el metodo hayCaminoDFS posterior
     *
     * @param g grafo dado
     * @param v vertices
     * @param w vertice
     * @return true si hay camino, false de lo contrario
     */
    public static boolean thereIsAPathDFS(Digraph g, int v, int w) {
        boolean[] valued = new boolean[g.size()];
        return thereIsAPathDFS(g, v, w, valued);
    }

    /**
     * Metodo que recorre el grafo por medio de dfs
     *
     * @param g grafo dado
     * @param v vertices
     * @param w vertice
     * @param valued ayuda a tener un conteo acerca de que nodos han sido o no
     * visitados
     * @return true si hay camino, false de lo contrario
     */
    private static boolean thereIsAPathDFS(Digraph g, int v, int w, boolean[] valued) {
        valued[v] = true;
        if (v == w) {
            return true;
        } else {
            ArrayList<Integer> children = g.getSuccessors(v);
            for (Integer hijo : children) {
                if (!valued[hijo] && thereIsAPathDFS(g, hijo, w, valued)) {
                    return true;
                }
            }
            return false;
        }
    }

    /**
     * Metodo que recorre el grafo por medio de dfs teniendo en cuenta que se
     * quiere encontrar el de menor costo
     *
     * @param g grafo dado
     * @param inicio nodo desde el cual empieza el recorrido
     * @param fin nodo donde termina el recorrido
     * @return cual es el costo que tiene ir desde inicio a fin
     */
    public static int costoMinimo(Digraph g, int inicio, int fin) {
        boolean[] valued = new boolean[g.size()];
        int cost = costoMinimo(g, inicio, fin, Integer.MAX_VALUE, 0, valued);
        return cost == Integer.MAX_VALUE ? -1 : cost;
    }

    public static int costoMinimo(Digraph g, int v, int w, int costoMin, int acumulado, boolean[] valued) {
        valued[v] = true;
        if (v == w) {
            if (costoMin > acumulado) {
                costoMin = acumulado;
            }
            return costoMin;
        } else {
            ArrayList<Integer> children = g.getSuccessors(v);
            int value = Integer.MAX_VALUE;
            for (Integer hijo : children) {
                int costoPadreHijo = g.getWeight(v, hijo);
                if ((costoPadreHijo < costoMin) && !(v==hijo) /*&& !valued[hijo]*/) {
                    value = Math.min(costoMinimo(g, hijo, w, costoMin, acumulado + g.getWeight(v, hijo), valued), value);
                }
            }
            return value;
        }
    }

    /**
     * Metodo auxiliar que llama al metodo recorrido posterior con cada uno de
     * los vertices
     *
     * @param g grafo dado
     * @return cual es el costo que tiene
     *
     * public static int recorrido(Digraph g) {
     *
     * }
     */
    /**
     * Metodo que recorre todo el grafo con la intencion de buscar un camino que
     * represente el menor costo pasando por todos los vertices exactamente una
     * vez y vuelva al nodo inicial
     *
     * @param g grafo dado
     * @param v vertice inicial
     * @param unvisited arreglo de nodos aun no visitados
     * @return cual es el costo que tiene
     *
     * private static int recorrido(Digraph g, int v, int[] unvisited) {
     *
     * }
     */
    public static void main(String[] args) {
        DigraphAL g1 = new DigraphAL(5);
        g1.addArc(0, 1, 2);
        g1.addArc(0, 2, 2);
        g1.addArc(0, 3, 1);
        g1.addArc(1, 0, 2);
        g1.addArc(1, 2, 3);
        g1.addArc(1, 3, 2);
        g1.addArc(2, 0, 2);
        g1.addArc(2, 1, 3);
        g1.addArc(2, 3, 2);
        g1.addArc(3, 0, 1);
        g1.addArc(3, 1, 2);
        g1.addArc(3, 2, 2);
        g1.addArc(3, 4, 2);
        g1.addArc(4, 0, 4);
        g1.addArc(4, 1, 3);
        g1.addArc(4, 2, 2);
        //System.out.println(thereIsAPathDFS(g1, 3, 4));
        DigraphAL g2 = new DigraphAL(5);
        g2.addArc(0, 2, 100);
        g2.addArc(2, 4, 100);
        g2.addArc(0, 1, 15);
        g2.addArc(1, 2, 10);
        g2.addArc(0, 3, 20);
        g2.addArc(3, 2, 20);
        g2.addArc(3, 4, 50);
        System.out.println(costoMinimo(g2, 0, 4));
    }

}
