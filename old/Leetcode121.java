import java.lang.*;
public class Leetcode121 {
    public static int maxProfit(int[] prices) {
        int[] localprice = prices;
        int maxProfit = 0;
        for (int i = 0; i < localprice.length; i++) {
        	for (int j = i+1; j < localprice.length; j++ ) {
        		int diff = localprice[j]-localprice[i];
        		if(diff>maxProfit)
        			maxProfit = diff;
        	}
        }
        return maxProfit;
    }

    public static void main(String[] args) {
    	int[] prices = {7, 1, 5, 3, 6, 4};
    	int profit = maxProfit(prices);
    	System.out.println("The maxProfit is "+profit);
    }
}