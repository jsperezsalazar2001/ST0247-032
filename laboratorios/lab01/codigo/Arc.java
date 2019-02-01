package javaapplication1;

/**
 * This class is the arc or edge object. 
 * @author Yhoan Alejandro Guzmán García
 * @author Juan Sebastián Pérez 
 */
public class Arc {
    private String nodeIDFrom;
    private String nodeIDTo;
    private double distance;
    private String name;
    
    /**
     * Class constructor
     * @param nodeIDFrom name of the first node
     * @param nodeIDTo name of the second node
     * @param distance distance between nodes
     * @param name street name
     */
    public Arc(String nodeIDFrom, String nodeIDTo, double distance, String name) {
        this.nodeIDFrom = nodeIDFrom;
        this.nodeIDTo = nodeIDTo;
        this.distance = distance;
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

    public double getDistance() {
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
