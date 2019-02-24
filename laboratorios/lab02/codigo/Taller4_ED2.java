package lab02;

import java.util.ArrayList;

/**
 * This class constains a method that find the minimun cost of a path in a Hamiltonian circuit.
 * @author Juan Sebastián Pérez Salazar
 * @author Yhoan Alejandro Guzman Garcia
 */
public class Taller4_ED2 {
    
    /**
     * This is the auxiliar method, this method is called from the main, and this pass the necessary parameters to the principal method.
     * @param g this is the graph
     * @param start this is the start and end node
     * @return an Integer, the minimun cost
     */
    public static int hamiltoniano(Digraph g, int start) {
        boolean[] valued = new boolean[g.size()];
        int cost = hamiltoniano(g, start, start, Integer.MAX_VALUE, 0, valued, 0);
        return cost == Integer.MAX_VALUE ? Integer.MIN_VALUE : cost;
    }

    /**
     * This method, find a path with the minimun cost to solve the Hamiltonian circuit
     * @param g The graph
     * @param v The start vertex
     * @param w The end vertex
     * @param minCost the minimum cost that has been found
     * @param acumulate the acumulate value of the path
     * @param valued array that contains nodes that have been traveled
     * @param evaluated number of nodes traveled 
     * @return an Integer,the minimun cost
     */
    public static int hamiltoniano(Digraph g, int v, int w, int minCost, int acumulate, boolean[] valued, int evaluated) {
        valued[v] = true;
        if(evaluated!=valued.length)evaluated++;
       
        if (v == w && evaluated==valued.length) {
            if (minCost > acumulate) {
                minCost = acumulate;
            }
            return minCost;
        } else{
            ArrayList<Integer> children = g.getSuccessors(v);
            int value = Integer.MAX_VALUE;
            for (Integer hijo : children) {
                int costoPadreHijo = g.getWeight(v, hijo);
                if (!valued[hijo] || (hijo==w && evaluated==valued.length)) {
                    value = Math.min(hamiltoniano(g, hijo, w, minCost, acumulate + costoPadreHijo, valued, evaluated), value);
                }
            }
            return value;
        }
    }
    /**
     * The main method executes tests to the algorithm
     * @param args 
     */
    public static void main(String[] args) {
        DigraphAL g1 = new DigraphAL(5);
        g1.addArc(0, 1, 2);
        g1.addArc(0, 2, 2);
        g1.addArc(0, 3, 1);
        g1.addArc(0, 4, 4);
        g1.addArc(1, 0, 2);
        g1.addArc(1, 2, 3);
        g1.addArc(1, 3, 2);
        g1.addArc(1, 4, 3);
        g1.addArc(2, 0, 2);
        g1.addArc(2, 1, 3);
        g1.addArc(2, 3, 2);
        g1.addArc(2, 4, 2);
        g1.addArc(3, 0, 1);
        g1.addArc(3, 1, 2);
        g1.addArc(3, 2, 2);
        g1.addArc(3, 4, 4);
        g1.addArc(4, 0, 4);
        g1.addArc(4, 1, 3);
        g1.addArc(4, 2, 2);
        g1.addArc(4, 3, 4);
        System.out.println(hamiltoniano(g1, 0));
    }

}
