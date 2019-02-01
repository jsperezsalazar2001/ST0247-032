package javaapplication1;

import java.util.LinkedList;
import javafx.util.Pair;

/**
 * This class is the node object. 
 * @author Yhoan Alejandro Guzmán García
 * @author Juan Sebastián Pérez
 */
public class Node {

    private String ID;
    private double longitude;
    private double latitude;
    private String name;
    private LinkedList<Pair<String, Arc>> neighbors = new LinkedList<Pair<String, Arc>>();

    /**
     * Class constructor. 
     * @param ID node identifier.
     * @param longitude node longitude
     * @param latitude node latitude
     * @param name node name
     */
    public Node(String ID, double longitude, double latitude, String name) {
        this.ID = ID;
        this.longitude = longitude;
        this.latitude = latitude;
        this.name = name;
    }

    public String getID() {
        return ID;
    }

    public void setID(String ID) {
        this.ID = ID;
    }

    public double getLongitude() {
        return longitude;
    }

    public void setLongitude(double longitude) {
        this.longitude = longitude;
    }

    public double getLatitude() {
        return latitude;
    }

    public void setLatitude(double latitude) {
        this.latitude = latitude;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    /**
     * This method add a new neighbor(creates an edge between two nodes).
     * @param neighbor the other node
     * @param arc edge between nodes
     */
    public void addNeighbor(String neighbor, Arc arc) {
        Pair pair = new Pair(neighbor, arc);
        this.neighbors.add(pair);
    }

    /**
     * This method get the adyacent nodes of one vertex. 
     * @return a linkedList
     */
    public LinkedList<Pair<String, Arc>> getNeighbors() {
        return neighbors;
    }
}
