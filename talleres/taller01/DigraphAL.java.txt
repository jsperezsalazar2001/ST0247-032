package taller11;

import java.util.ArrayList;
import java.util.LinkedList;

/**
 * Esta clase es una implementación de un digrafo usando listas de adyacencia
 *
 * @author Juan Sebastián Pérez Salazar
 * @version 1
 */
public class DigraphAL extends Graph {

    ArrayList<LinkedList<Pareja>> listaAdyacencia = new ArrayList();

    public DigraphAL(int size) {
        super(size);
        for(int i = 0; i< size; i++)
            listaAdyacencia.add(new LinkedList());
    }

    @Override
    public int getWeight(int source, int destination) {
        LinkedList<Pareja> parejas = listaAdyacencia.get(source);
        for(Pareja p: parejas)
            if(p.vertice == destination)
                return p.peso;
        
        return 0; 
    }
    
    @Override
    public void addArc(int source, int destination, int weight) {
        listaAdyacencia.get(source).add(new Pareja(destination, weight));
    }

    @Override
    public ArrayList<Integer> getSuccessors(int vertice) {
        ArrayList<Integer> successors = new ArrayList();
        for(Pareja p: listaAdyacencia.get(vertice))
            successors.add(p.vertice);
        
        return successors;
    }
}
