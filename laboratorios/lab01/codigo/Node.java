/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lab1;

import java.util.LinkedList;
import javafx.util.Pair;

/**
 *
 * @author Yhoan Alejandro Guzmán García
 * @author Juan Sebastián Pérez 
 */
public class Node {
   private String ID;
   private double longitude;
   private double latitude;
   private String name;
   private LinkedList<Pair<String,Arc>> neighbors = new LinkedList<Pair<String,Arc>>();

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
   
    public void addNeighbor(String neighbor, Arc arc) {
        Pair pair = new Pair(neighbor,arc);
        this.neighbors.add(pair);
    }
         
}
