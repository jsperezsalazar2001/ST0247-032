
package lab5;

/**
 * @autor Juan Sebastián Pérez Salazar
 * @autor Yhoan Alejandro Guzmán García
 * 
 **/

import java.util.ArrayList;

public class HeldKarp {
    static String Binary = ""; // Helper for the binary sequences needed in the different sets
    
     /* This method initializes the matrix
     * @param g given graph
     * returns the minum cost
     */

    public static int HeldKarp(Digraph g) {
        int n = g.size();
        int pot = (((int) Math.pow(2, n)) / 2);
        int[][] costos = new int[n][pot];

        for (int i = n - 1; i >= 0; i = i - 1) {
            costos[i][0] = g.getWeight(0, i);
        }

        return heldKarpAux(g, costos, 0, pot - 1);
    }

    public static int heldKarpAux(Digraph g, int[][] costs, int target, int power) {
            for (int i = costs.length - 1; i >= 0; i--) {
                for (int j = 1; j <= 2; j++) {
                    costs[i][j] = getCost(i, j, g, costs);
                }
            }
            for (int i = costs.length - 1; i >= 0; i--) {
                for (int j = 3; j < 5; j++) {
                    costs[i][j] = getCost(i, j, g, costs);
                }
            }
            for (int i = costs.length - 1; i >= 0; i--) {
                for (int j = 5; j < costs[i].length; j++) {
                    costs[i][j] = getCost(i, j, g, costs);
                }
            }
        return costs[0][7];
    }

    public static int binaryToDecimal(int number) {
        int decimal = 0;
        int binary = number;
        int power = 0;
 
        while (binary != 0) {
            int lastDigit = binary % 10;
            decimal += lastDigit * Math.pow(2, power);
            power++;
            binary = binary / 10;
        }
        return decimal;
    }

    /**
     * This method calculates the cost from sets to nodes
     **/
    public static int getCost(int output, int input, Digraph g, int[][] weights) {

        ArrayList<Integer> arr = new ArrayList<>();
        int cost = 0;   
        char[] aux = intToBinary(input);    
        int size = aux.length;
        int[] auxInt = new int[size]; 
        for(int i = 0; i < auxInt.length; i++){
            auxInt[i] = Integer.valueOf(Character.toString(aux[i]));
        }
        for(int i = 0; i < size; i++){
            if(auxInt[i] == 1){
                if(i == 0){
                    arr.add(3);
                }else if(i == 1){
                    arr.add(2);
                }else if(i == 2){
                    arr.add(1);
                }
            }
        }
        if(output == 0 && input != 7){
            cost = 0;
        }else if(arr.contains(output)){
            cost = 0;
        }else if(arr.size() == 1){    
            cost = g.getWeight(0, arr.get(0)) + g.getWeight(arr.get(0), output);
        }else if (arr.size() == 2){
            cost = Math.min(g.getWeight(arr.get(0), output) + weights[arr.get(0)][binaryToDecimal(buildBinary(arr.get(1)))], g.getWeight(arr.get(1), output) + weights[arr.get(1)][binaryToDecimal(buildBinary(arr.get(0)))]);
        }else if(arr.size() == 3){
            cost = Math.min(Math.min(g.getWeight(arr.get(0), output) + weights[3][3], g.getWeight(arr.get(1), output) + weights[2][5]), g.getWeight(arr.get(2), output) + weights[1][6]);
        }
        reset();
        return cost;
    }
    
    /**
     *  This method shows the calculated weighs of the graph
     * @param g Given graph
     * @param costs parcial or total costs
     **/
    public static void show(Digraph g, int[][] costs) {
        int n = g.size();
        int pot = ((int) Math.pow(2, n)) / 2;
        for (int i = n - 1; i >= 0; i = i - 1) {
            for (int j = 0; j < pot; j++) {
                System.out.print(costs[i][j] + "         ");
            }
            System.out.println();
        }
    }
    /**
     * Int to binary
     * @param value to convert
     * return an array of charts
     **/

    public static char[] intToBinary(int value) { //adapted from https://www.sanfoundry.com/java-program-convert-decimal-binary-number-count-number-1s/
        if (value / 2 != 0) {
            Binary = Integer.toString(value % 2) + Binary;
            value = value / 2;
            intToBinary(value);
        } else {
            Binary = Integer.toString(value) + Binary;
        }
        if (Binary.length() == 1) {
            Binary = "00" + Binary;
        } else if (Binary.length() == 2) {
            Binary = "0" + Binary;
        }
        return Binary.toCharArray();
    }
    
    public static int buildBinary(int value){
        String str = "";
        if(value == 1){
            str = "001";
        }else if(value == 2){
            str = "010";
        }else if(value == 3){
            str = "100";
        }
        return Integer.parseInt(str);
    }
    
     /**
     * Resets the static variable Binary
     **/
    public static void reset() {
        Binary = "";
    }
}
