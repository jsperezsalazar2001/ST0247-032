import java.util.*;

/**
 *
 * @author Yhoan Alejandro Guzman Garcia - Juan Sebastian Perez Salazar 
 */

public class NQueensProblem {
    static int globalIndex = 0;
    static int[][] board;;
    public NQueensProblem(int numberOfQuens){
        board = new int[factorial(numberOfQuens)][numberOfQuens];
    }

    public static int factorial(int number) {
        int result = 1;
        for (int factor = 2; factor <= number; factor++) {
            result *= factor;
        }
        return result;
    }

    public void nQueensSolution(){
        String chain = "";
        System.out.println("Number of Queens: "+board[0].length);
        System.out.println("Possible permutations: "+board.length);
        for(int i = 1; i <= board[0].length;i++){
            chain += i;
        }
        System.out.println(chain);
        subSetPermAux("", chain);
        solutionsBybruteForce();
    }

    public void subSetPermAux(String prefix, String sufix){
        if(sufix.length()==0) {
            newBoardRow(prefix);
            globalIndex++;
        }
        else{
            for(int i=0; i<sufix.length(); i++ ){
                if(board[0].length < 10){
                subSetPermAux(prefix+sufix.charAt(i),sufix.substring(0,i)+sufix.substring(i+1));
                }else if(false){//need change for n > 9
                subSetPermAux(prefix+sufix.charAt(i+1),sufix.substring(0,i+1)+sufix.substring(i+1+1));
                }
            }
        }
    }

    public void newBoardRow(String chain){
        for(int j = 0; j < board[0].length;j++){
            board[globalIndex][j] = Character.getNumericValue(chain.charAt(j));
        }
    }

    public void solutionsBybruteForce(){
        LinkedList<Integer> solutionsList = new LinkedList<Integer>();
        for(int i = 0; i < board.length;i++){
            if(rowBoardSolution(i)){
                solutionsList.add(i);  
            }
        } 
        System.out.println("Number of solutions: "+solutionsList.size());
        /*for (int row : solutionsList) {
            print(row);
        }*/
    }

    public static boolean rowBoardSolution(int i){
        boolean solution = true;
        for(int j = 0; j < board[0].length; j++){
            for(int e = j+1; e < board[0].length; e++){
                double slope = slope(board[i][j]-1,j,board[i][e]-1,e);
                if(slope == 1 || slope == -1){
                    solution = false;
                    break;
                }
            }
            if(!solution){
                break;
            }
        }
        return solution;
    }

    public static double slope(double x1, double y1, double x2, double y2) { 
        return (y2 - y1) / (x2 - x1); 
    } 

    public void print(int row){

        for(int j = 0; j < board[0].length; j++){
            System.out.print(board[row][j]+" ");
        }
        System.out.println();

    }

    public static void main(String[]args){
        NQueensProblem test1 = new NQueensProblem(8);
        test1.nQueensSolution();
    }

}
