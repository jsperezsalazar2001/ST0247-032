package lab02;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;

/**
 * This class contains the methods that read the file and decide if graph is bipartite or not.
 * @author Juan Sebastián Pérez Salazar
 */
public class Claw {
    private HashMap<Integer, Integer> graph = new HashMap<Integer, Integer>();
    
    /**
     * This method reads the file and generate the graph
     * @param fileName name of the file with vertices and edges 
     */
    public void readGraph(String fileName) {
        BufferedReader reader = null;
        try {
            File file = new File(fileName);
            reader = new BufferedReader(new FileReader(file));
            String line;
            boolean print = true;
            line = reader.readLine();
            while ((line = reader.readLine()) != null) {
                
                String[] lineArray = line.split(" ");
                if(lineArray.length == 1){
                    if(print) System.out.println("Yes");
                    if(lineArray[0].equals("0")) break;
                    graph = new HashMap<Integer, Integer>();
                    print = true;
                    line = reader.readLine();
                    lineArray = line.split(" ");
                }
                
                int vertex1 = Integer.parseInt(lineArray[0]);
                int vertex2 = Integer.parseInt(lineArray[1]); 
               
                if(graph.containsKey(vertex1) || graph.containsValue(vertex1)){
                    if(graph.containsKey(vertex1) && graph.containsKey(vertex2)) {
                        if(print) System.out.println("No");
                        print = false;
                    }else if(graph.containsValue(vertex1) && graph.containsValue(vertex2)) {
                        if(print) System.out.println("No");
                        print = false;
                    }else{
                        if(graph.containsKey(vertex1) && !graph.containsValue(vertex2)) graph.put(-1, vertex2);
                        else if(!graph.containsKey(vertex2) && graph.containsValue(vertex1)) graph.put(vertex2, -1);
                    }
                }else {
                    if(!graph.containsKey(vertex2) && !graph.containsValue(vertex2)) graph.put(vertex1, vertex2);
                    else if(graph.containsKey(vertex2)) graph.put(-1, vertex1);
                    else if(graph.containsValue(vertex2)) graph.put(vertex1, -1);
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
     * This is the main method, in this method the proves are executed. 
     * @param args 
     */
    public static void main(String[] args) {
        Claw test = new Claw();
        test.readGraph("ClawTest.txt");
        
    }
}
