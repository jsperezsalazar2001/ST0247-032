package javaapplication1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.ListIterator;
import javafx.util.Pair;

/**
 * This class contains the methods that read the file and save the graph for later access.
 *
 * @author Juan Sebastián Pérez Salazar
   @author Yhoan Alejandro Guzmán García
 */
public class Graph {

    private HashMap<String, Node> graph = new HashMap<String, Node>();

    /**
     * This method reads the file and generateS the graph
     * @param fileName name of the file with vertices and edges 
     */
    public void readGraph(String fileName) {
        BufferedReader reader = null;
        try {
            File file = new File(fileName);
            reader = new BufferedReader(new FileReader(file));
            String line;
            line = reader.readLine();
            while ((line = reader.readLine()) != null) {
                if (line.length() > 0) {
                    if (line.contains("Arco")) {
                        break;
                    }
                    String description = "";
                    String[] lineArray = line.split(" ");
                    if ((lineArray.length >= 4)) {
                        description = lineArray[3];
                    }
                    Node node = new Node(lineArray[0], Double.parseDouble(lineArray[1]), Double.parseDouble(lineArray[2]), description);
                    graph.put(node.getID(), node);
                }
            }
            while ((line = reader.readLine()) != null) {
                if (!line.equals("")) {
                    String description = "";
                    String[] lineArray = line.split(" ", 4);
                    if ((lineArray.length >= 4)) {
                        description = lineArray[3];
                    }
                    Arc arc = new Arc(lineArray[0], lineArray[1], Double.parseDouble(lineArray[2]), description);
                    graph.get(arc.getNodeIDFrom()).addNeighbor(arc.getNodeIDTo(), arc);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                reader.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * This method prints the vertices and their neighbors. 
     * 
     */
    public void printGraph() {
        Iterator hmIterator = graph.entrySet().iterator();
        while (hmIterator.hasNext()) {
            Map.Entry mentry = (Map.Entry) hmIterator.next();
            System.out.print(mentry.getKey() + " -> ");
            LinkedList<Pair<String, Arc>> list = graph.get(mentry.getKey()).getNeighbors();
            Iterator list_Iter = list.iterator();
            while (list_Iter.hasNext()) {
                Pair par = (Pair) list_Iter.next();
                System.out.print(par.getKey() + " -> ");
            }
            System.out.println();
        }

    }

    /**
     * This is the main method, in this method the tests are executed. 
     * @param args 
     */
    public static void main(String[] args) {
        Graph test = new Graph();
        test.readGraph("medellin_colombia-grande.txt");
        
        test.printGraph();
    }

}
