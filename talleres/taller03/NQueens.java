package nqueens;


/**
 *
 * @author Juan Sebastián Pérez Salazar - Yhoan Alejandro Guzmán García
 */
public class NQueens {
    public static boolean canAtack(int[] board, int I) {
        for (int i = 0; i < I - 1; i++) {
            for (int j = i + 1; j < I; j++) {
                if (hit(i, board[i], j, board[j])) {
                    return true;
                }
            }
        }
        return false;
    }

    public static boolean hit(double x1, double y1, double x2, double y2) {
       // System.out.println(x1+" - "+y1+" - "+x2+" - "+y2+" ---- "+(y2 - y1) / (x2 - x1));
        return ((y2 - y1) / (x2 - x1) == -1) || ((y2 - y1) / (x2 - x1) == 1) || ((y2 - y1) / (x2 - x1) == 0);
    }

    public static void nQueens(int n, int[] board, int col) {
        if (col == n) {
            if (!canAtack(board, col)) {
                printBoard(board);
            }
        } else {
            for (int i = 0; i < n; i++) {
                board[col] = i;
                if (!canAtack(board, col)) {
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
        for (int i = 0; i < board.length; i++) {
            System.out.print(board[i] + " ");
        }
        System.out.println();
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        nQueens(8);
    }

}
