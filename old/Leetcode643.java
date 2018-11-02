
public class Leetcode643 {
    public double findMaxAverage(int[] nums, int k) {
        int size = nums.length;
        double total = 0;
        for (int i = 0; i < k; i++ ) {
        	total = total + nums[i];
		}
		double maxtotal = total; 
		for (int i = k; i< size ; i++) {
			total = total+nums[i]-nums[i-k];
			maxtotal = Math.max(maxtotal,total);
		}
		
        return maxtotal/k;
    }

    public static void main(String[] args) {
    	int[] x = {1,2,3,12,5,6,1,100};
    	//int[] x ={8860,-853,6534,4477,-4589,8646,-6155,-5577,-1656,-5779,-2619,-8604,-1358,-8009,4983,7063,3104,-1560,4080,2763,5616,-2375,2848,1394,-7173,-5225,-8244,-809,8025,-4072,-4391,-9579,1407,6700,2421,-6685,5481,-1732,-8892,-6645,3077,3287,-4149,8701,-4393,-9070,-1777,2237,-3253,-506,-4931,-7366,-8132,5406,-6300,-275,-1908,67,3569,1433,-7262,-437,8303,4498,-379,3054,-6285,4203,6908,4433,3077,2288,9733,-8067,3007,9725,9669,1362,-2561,-4225,5442,-9006,-429,160,-9234,-4444,3586,-5711,-9506,-79,-4418,-4348,-5891};
    	//int[] x = {1};
    	Leetcode643 t = new Leetcode643();
    	double y = t.findMaxAverage(x,1);
    	System.out.println(y);
    }
}
/*
    public double findMaxAverage(int[] nums, int k) {
        int size = nums.length;
        double[] sum = new sum[size];
        double maxaverage = Integer.MIN_VALUE;
        double average = 0;
        for (int i = 0; i<= size-k;i++ ) {
        	double total = 0;

        	for (int j = i; j< i +k;j++ ) {
        		total = total +nums[j];
        	}
        	average = total/k;
        	System.out.println(average);
        	        	System.out.println(maxaverage);

        	if (average>maxaverage) maxaverage = average;
        }
        return maxaverage;
    }

        public double findMaxAverage(int[] nums, int k) {
        int size = nums.length;
        double[] sum = new double[size];
        sum[0] = nums[0];
        for (int i = 1; i < size; i++ ) {
        	sum[i] = sum[i-1]+ nums[i];
		}
		double maxaverage = sum[k-1]/k;
		for (int i = k; i<size; i++ ) {
			double average = (sum[i]-sum[i-k])/k;
			maxaverage = Math.max(maxaverage,average);
		}
        	
        return maxaverage;
    }
*/