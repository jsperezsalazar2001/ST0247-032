/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lab1;

/**
 *
 * @author Yhoan Alejandro Guzmán García
 * @author Juan Sebastián Pérez 
 */
public class Arc {
    private String nodeIDFrom;
    private String nodeIDTo;
    private int distance;
    private String name;
    public Arc(String nodeIDFrom, String nodeIDTo, int weight, String name) {
        this.nodeIDFrom = nodeIDFrom;
        this.nodeIDTo = nodeIDTo;
        this.distance = weight;
        this.name = name;
    }

    public String getNodeIDFrom() {
        return nodeIDFrom;
    }

    public void setNodeIDFrom(String nodeIDFrom) {
        this.nodeIDFrom = nodeIDFrom;
    }

    public String getNodeIDTo() {
        return nodeIDTo;
    }

    public void setNodeIDTo(String nodeIDTo) {
        this.nodeIDTo = nodeIDTo;
    }

    public int getDistance() {
        return distance;
    }

    public void setDistance(int distance) {
        this.distance = distance;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    
    
}
