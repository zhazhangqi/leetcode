import java.math.*;
public class Leetcode593{
	public static boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        //first check if exsist two edge equal each other
        if((lenght2(p1,p2)==lenght2(p2,p3))&&(lenght2(p2,p3)==lenght2(p3,p4))&&(lenght2(p3,p4)==lenght2(p4,p1))&&(lenght2(p1,p3)==lenght2(p2,p4))&&(lenght2(p2,p4)!=0))
        		return true;
        else if((lenght2(p1,p3)==lenght2(p3,p2))&&(lenght2(p3,p2)==lenght2(p2,p4))&&(lenght2(p2,p4)==lenght2(p4,p1))&&(lenght2(p1,p2)==lenght2(p3,p4))&&(lenght2(p2,p4)!=0))
        		return true;
        else if((lenght2(p1,p3)==lenght2(p3,p4))&&(lenght2(p3,p4)==lenght2(p4,p2))&&(lenght2(p4,p2)==lenght2(p2,p1))&&(lenght2(p1,p4)==lenght2(p3,p2))&&(lenght2(p2,p4)!=0))
        		return true;
        else return false;
    }

    public static double lenght2(int[] p1, int[] p2){
    	double Deltax = p2[0]-p1[0];
    	double powx = Math.pow(Deltax,2);
    	double Deltay = p2[1]-p1[1];
    	double powy = Math.pow(Deltay,2);
    	return powx+powy;
    }

    public static void main(String[] args) {
    	int[] p1 = {0,0}, p2 = {1,1}, p3 = {1,0}, p4 = {0,1};
    	
    	if(validSquare(p1,p2,p3,p4))
    		System.out.println("This is a valid square");
    	else
    		System.out.println("This is not a valid square");
    }
}