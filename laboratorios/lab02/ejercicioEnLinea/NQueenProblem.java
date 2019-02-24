
package nqueens;

import java.util.*;

/**
 *
 * @author Yhoan Alejandro Guzman Garcia - Juan Sebastian Perez Salazar
 */
public class NQueensProblem {

    static HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    static int globalIndex = 0;
    static int[][] board;

    public NQueensProblem(int numberOfQuens) {
        board = new int[factorial(numberOfQuens)][numberOfQuens];
    }

    public static int factorial(int number) {
        int result = 1;
        for (int factor = 2; factor <= number; factor++) {
            result *= factor;
        }
        return result;
    }

    public void nQueensSolution() {
        String chain = "";
        System.out.println("Number of Queens: " + board[0].length);
        System.out.println("Possible permutations: " + board.length);
        int[] sufix = new int[board[0].length];
        for (int i = 0; i < board[0].length; i++) {
            sufix[i] = i + 1;
        }
        int[] prefix = new int[0];
        System.out.println(chain);
        readHoles();
        subSetPermAux(prefix, sufix);
        solutionsBybruteForce();
    }

    public void subSetPermAux(int[] prefix, int[] sufix) {
        if (sufix.length == 0) {
                board[globalIndex] = prefix;
                //printArray(prefix);
                globalIndex++;
        } else {
            for (int i = 0; i < sufix.length; i++) {
                //System.out.println(prefix+" -1- "+sufix.charAt(i)+", -2- "+" -3- "+sufix.substring(i+1));
                subSetPermAux(addElementArray(prefix, sufix[i]), concatArrays(subsArray(sufix, 0, i), subsArray(sufix, (i + 1))));

            }
        }
    }

    public boolean solution(int[] posSol) {
        for (int i = 0; i < posSol.length; i++) {
            if (map.get(i) != null && map.get(i) == posSol[i]) {
                return false;
            }
        }
        return true;
    }

    public void readHoles() {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        for (int i = 0; i <= num; i++) {
            String line = sc.nextLine();
            for (int j = 0; j < line.length(); j++) {
                if (line.charAt(j) == '*') {
                    //System.out.println("entra: "+i+" "+j);
                    map.put(j, i);
                }
            }
        }
    }

    public int[] addElementArray(int[] arr, int val) {
        int[] result = new int[arr.length + 1];
        for (int i = 0; i < arr.length; i++) {
            result[i] = arr[i];
        }
        result[result.length - 1] = val;
        return result;
    }

    public void printArray(int[] arr) {
        System.out.print("[ ");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.print("]");
        System.out.println();
    }

    public int[] subsArray(int[] arr, int index) {
        int[] result = new int[arr.length - index];
        int resIndex = 0;
        for (int i = index; i < arr.length; i++) {
            result[resIndex] = arr[i];
            resIndex++;
        }
        return result;
    }

    public int[] subsArray(int[] arr, int from, int to) {
        int[] result = new int[to - from];
        int resIndex = 0;
        for (int i = from; i < to; i++) {
            result[resIndex] = arr[i];
            resIndex++;
        }
        return result;
    }

    public int[] concatArrays(int[] arr1, int[] arr2) {
        int[] result = new int[arr1.length + arr2.length];
        int resIndex = 0;
        for (int i = 0; i < arr1.length; i++) {
            result[resIndex] = arr1[i];
            resIndex++;
        }
        for (int i = 0; i < arr2.length; i++) {
            result[resIndex] = arr2[i];
            resIndex++;
        }
        return result;
    }

    public void solutionsBybruteForce() {
        LinkedList<Integer> solutionsList = new LinkedList<Integer>();
        for (int i = 0; i < board.length; i++) {
            if (solution(board[i]) && rowBoardSolution(i)) {
                solutionsList.add(i);
            }
        }
        System.out.println("Number of solutions: " + solutionsList.size());
        for (int row : solutionsList) {
            print(row);
        }
    }

    public static boolean rowBoardSolution(int i) {
        boolean solution = true;
        for (int j = 0; j < board[0].length; j++) {
            for (int e = j + 1; e < board[0].length; e++) {
                double slope = slope(board[i][j] - 1, j, board[i][e] - 1, e);
                if (slope == 1 || slope == -1) {
                    solution = false;
                    break;
                }
            }
            if (!solution) {
                break;
            }
        }
        return solution;
    }

    public static double slope(double x1, double y1, double x2, double y2) {
        return (y2 - y1) / (x2 - x1);
    }

    public void print(int row) {

        for (int j = 0; j < board[0].length; j++) {
            System.out.print(board[row][j] + " ");
        }
        System.out.println();

    }

    public static void main(String[] args) {
        NQueensProblem test1 = new NQueensProblem(4);
        test1.nQueensSolution();
    }

}
