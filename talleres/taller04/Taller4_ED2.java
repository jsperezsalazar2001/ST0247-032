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
	* @param g grafo dado 
	* @param v vertices 
	* @param w vertice
	* @param valued ayuda a tener un conteo acerca de que nodos han sido
	* o no visitados
	* @return true si hay camino, false de lo contrario
	*/
    private static boolean thereIsAPathDFS(Digraph g, int v, int w, boolean[] valued) {
        valued[v] = true;
        if (v == w) {
            return true;
        } else {
            ArrayList<Integer> children = g.getSuccessors(v);
            for(Integer hijo : children) {
                if (!valued[hijo] && thereIsAPathDFS(g, hijo, w, valued)) {
                    return true;
                }
            }
            return false;
        }
    }

    /**
	* Metodo que recorre el grafo por medio de dfs teniendo en cuenta que
	* se quiere encontrar el de menor costo
	* @param g grafo dado 
	* @param inicio nodo desde el cual empieza el recorrido 
	* @param fin nodo donde termina el recorrido
	* @return cual es el costo que tiene ir desde inicio a fin
	*/
	public static int costoMinimo(Digraph g, int inicio, int fin) {
		
	}

	/**
	* Metodo auxiliar que llama al metodo recorrido posterior
	* con cada uno de los vertices
	* @param g grafo dado 
	* @return cual es el costo que tiene
	*/
	public static int recorrido(Digraph g) {
		
	}

	/**
	* Metodo que recorre todo el grafo con la intencion de buscar un
	* camino que represente el menor costo pasando por todos los vertices exactamente
	* una vez y vuelva al nodo inicial
	* @param g grafo dado 
	* @param v vertice inicial
	* @param unvisited arreglo de nodos aun no visitados
	* @return cual es el costo que tiene
	*/
	private static int recorrido(Digraph g, int v, int[] unvisited) {
		
	}


	/**
	* Metodo que dada un conjunto de costos en cada arco, encuentra el camino desde el nodo v
	* @param g grafo dado 
	* @param v vertice inicial
	* @param coso arreglo de valores que tiene de ir de un nodo a otro
	* 
	*/
	private static void dfs(Digraph g, int v, int[] costo) {
		
	}

}