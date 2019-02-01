/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lab1;

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

/*
*
 *
 * @author cl18405
 */
public class Graph {

    private HashMap<String, Node> graph = new HashMap<String, Node>();

    public void readGraph(String fileName) {
        BufferedReader reader = null;
        try {
            File file = new File(fileName);
            reader = new BufferedReader(new FileReader(file));
            String line;
            line = reader.readLine();
            while ((line = reader.readLine()) != null) {
                if (!line.equals("")) {
                    if (line.contains("Arco")) {
                        break;
                    }
                    String[] lineArray = line.split(" ");
                    Node node = new Node(lineArray[0], Double.parseDouble(lineArray[1]), Double.parseDouble(lineArray[2]), lineArray[3]);
                    graph.put(node.getID(), node);
                }
            }
            while ((line = reader.readLine()) != null) {
                if (!line.equals("")) {
                    String[] lineArray = line.split(" ");
                    Arc arc = new Arc(lineArray[0], lineArray[1], Integer.parseInt(lineArray[2]), lineArray[3]);
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

    public void printGraph() {
        Iterator hmIterator = graph.entrySet().iterator();
        while (hmIterator.hasNext()) {
            Map.Entry mentry = (Map.Entry) hmIterator.next();
            System.out.print(mentry.getKey() + " -> ");
            LinkedList<Pair<String, Arc>> list = graph.get(mentry.getKey()).getNeighbors();
            Iterator list_Iter = list.iterator();
            while (list_Iter.hasNext()) {
                Pair par = (Pair)list_Iter.next();
                System.out.print(par.getKey());
            }
            System.out.println(mentry.getValue());
        }

    }

    public static void main(String[] args) {
        Graph test = new Graph();
        test.readGraph("dataExample.txt");
    }

}
