//import java.math.*;

public class Leetcode36{
	public static boolean isValidSudoku(char[][] board) {
        boolean valid = true;
        //check every rows 
		for ( int i = 0; i < 9; i++){
    		for ( int j = 0; j < 8; j++){
    			int x = Character.digit(board[i][j],10);
    			for (int k = j+1; k < 9; k++){
    				int y = Character.digit(board[i][k],10);
    				if ((x==y)&&(x>=0)) valid = false;
    			}
    		}    		
    	}
		//check every colum
    	for ( int i = 0; i < 9; i++){
    		for ( int j = 0; j < 8; j++){
    			int x = Character.digit(board[j][i],10);
    			for (int k = j+1; k < 9; k++){
    				int y = Character.digit(board[k][i],10);
    				if ((x==y)&&(x>=0)) valid = false;
    			}
    		}    		
    	} 
    	//check section
	    for (int i = 0; i < 7; i = i+3 ){
	    	for (int j = 0; j < 7; j = j+3 ){
	    		char[] section = new char[9];
	    		section[0] = board[i  ][j  ]; 
	    		section[1] = board[i  ][j+1];
	    		section[2] = board[i  ][j+2];
	    		section[3] = board[i+1][j  ];
	    		section[4] = board[i+1][j+1];
	    		section[5] = board[i+1][j+2];
	    		section[6] = board[i+2][j  ];
	    		section[7] = board[i+2][j+1];
	    		section[8] = board[i+2][j+2];
				System.out.println(section);
				
				for ( int k = 0; k < 8; k++){
    				
    				int x = Character.digit(section[k],10);
    				for (int l = k+1; l < 9; l++){
    					int y = Character.digit(section[l],10);
    					if ((x==y)&&(x>=0)) valid = false;
    				}
    			}   
	    	}
	    }
	return valid;
    }


    public static void main(String[] args) {
    	char[][] board ={	{'5','3','.',  '.','7','.',  '.','.','.'},
    					 	{'6','.','.',  '1','9','5',  '.','.','.'},
    					 	{'.','9','8',  '.','.','.',  '.','6','.'},
							
							{'8','.','.',  '.','6','.',  '.','.','3'},
							{'4','.','.',  '8','.','3',  '.','.','1'},
    					 	{'7','.','.',  '.','2','.',  '.','.','6'},
    					 	
    					 	{'.','6','.',  '.','.','.',  '2','8','.'},
							{'.','.','.',  '4','1','9',  '.','.','5'},
							{'.','.','.',  '.','8','.',  '.','7','9'}};

    boolean isvalid = isValidSudoku(board);
    System.out.println(isvalid);
    }
}