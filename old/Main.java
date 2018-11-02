class Main {
    public static void main(String[] args) {
        int M[][] = {{2,3,4},{5,6,7},{8,9,10},{11,12,13},{14,15,16}};
        int columLength = M[0].length;
        System.out.println(columLength);
        int rowLength = M.length;
                System.out.println(rowLength);

        int[][] imageOut = new int[rowLength][columLength];
        for (int i = 0; i < rowLength; i++){
            for (int j = 0; j < columLength; j++){
                int count = 1;
                int sum = M[i][j];
                if(i-1 >= 0){
                    sum += M[i-1][j];
                    count++;
                    if (j-1 >= 0){
                        sum += M[i-1][j-1];
                        count++;
                    }
                    if (j+1 < columLength){
                        sum += M[i-1][j+1];
                        count++;
                    }
                }
                if(i+1 < rowLength){
                    sum += M[i+1][j];
                    count++;
                    if (j-1 >= 0){
                        sum += M[i+1][j-1];
                        count++;
                    }
                    if (j+1 < columLength){
                        //sum += M[i+1][j+1];
                        count++;
                    }
                }
                if (j-1 >= 0){
                    sum += M[i][j-1];
                    count++;
                }
                if (j+1 < columLength){
                  //  sum += M[i][j+1];
                    count++;
                }
                imageOut[i][j] = sum/count;
                System.out.println(imageOut[i][j]);
            }
        }
    }
}