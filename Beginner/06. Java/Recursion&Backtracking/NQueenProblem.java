// N-Queen Problem using Backtracking
/*
The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.
The solution uses Backtracking to solve the problem.
The expected output will contain all possible positions to place the queens.
           
*/

import java.util.*;

public class Solution
{  

public static void main(String [] args){

	Scanner s=new Scanner(System.in);
  int N=s.nextInt();
  boolean[][] board=new boolean[N][N];
	NQueen(board, 0, 0,0, N ,"");
	
          }

public static void NQueen(boolean[][] board, int row, int col, int queensPlaced, int totalQueens, String ans) {

		if (queensPlaced == totalQueens) {
			System.out.println(ans);
			return;
		}

		if (col == board[0].length) {
			col = 0;
			row++;
		}

		if (row == board.length) {
			return;
		}

		if (isItSafeToPlaceQueen(board, row, col)) {
			board[row][col] = true;
			NQueen(board, row, col + 1, queensPlaced + 1, totalQueens, ans + "[" + row + "-" + col + "]");
			board[row][col] = false;
		}
		NQueen(board, row, col + 1, queensPlaced, totalQueens, ans);

	}

	private boolean isItSafeToPlaceQueen(boolean[][] board, int row, int col) {

                
		int r = row - 1;
		int c = col;
		while (r >= 0) {
			if (board[r][c]) {
				return false;
			}
			r--;
		}

		r = row;
		c = col - 1;
		while (c >= 0) {
			if (board[r][c]) {
				return false;
			}
			c--;
		}

		r = row - 1;
		c = col - 1;
		while (r >= 0 && c >= 0) {
			if (board[r][c]) {
				return false;
			}
			r--;
			c--;
		}

		r = row - 1;
		c = col + 1;
		while (r >= 0 && c < board[0].length) {
			if (board[r][c]) {
				return false;
			}
			r--;
			c++;
			;
		}
		return true;
	}

}


/* Input :
   4
  Output :
  [0-1][1-3][2-0][3-2]
  [0-2][1-0][2-3][3-1]
*/
