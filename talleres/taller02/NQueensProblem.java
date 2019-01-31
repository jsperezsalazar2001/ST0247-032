package taller2_ed2;

import java.util.LinkedList;

/**
 *
 * @author Juan Sebastian Perez Salazar - Yhoan Alejandro Guzman Garcia
 */

public class NQueensProblem {
    static int globalIndex = 0;
    static LinkedList<int[]> board = new LinkedList<>();
    public static void nQueensSolution(){
        subSetPermAux("", "12345678");
    }
    
    public static void subSetPermAux(String prefix, String sufix){
        if(sufix.length()==0) {
            board[globalindex][1] = chainToArray(prefix);
        }
        else{
            for(int i=0; i<sufix.length(); i++ ){
                subSetPermAux(prefix+sufix.charAt(i),sufix.substring(0,i)+sufix.substring(i+1));
            }
        }
    }


    public static int[] chainToArray(String chain){
        int[] array = new int[8];
        for(int i = 0; i < array.length;i++){
            array[i] = (int)chain.charAt(i);
        }
        return array;
    }
}