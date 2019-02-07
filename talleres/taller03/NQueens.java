package nqueens;

/**
 *
 * @author Juan Sebastián Pérez Salazar - Yhoan Alejandro Guzmán García
 */
public class NQueens {

    public static boolean atackUntilIOrNot(int[] board, int I) {
        for (int i = 0; i < I - 1; i++) {
            for (int j = i + 1; j < I; j++) {
                if (Math.abs(board[i] - board[j]) == Math.abs(i - j)) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void nQueens(int n, int[] board, int col) {
        if (col == n) {
            printBoard(board);
        } else {
            for (int i = 0; i < n; i++) {
                board[col] = i;
                if (!atackUntilIOrNot(board, col)) {
                    nQueens(n, board, col + 1);
                }
            }
        }
        //return true; para una sola solución 
    }

    public static void nQueens(int n) {
        nQueens(n, new int[n], 0);
    }

    public static void printBoard(int[] board) {
        System.out.print("Board");
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       nQueens(4);
    }

}
