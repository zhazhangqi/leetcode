import java.util.*;
import java.io.*;
public class arrayTest{
	 public static void main(String[] args) {
  int[] y = {-2, 0, -1};
      //int[] array = {-9,-6,-8,-3,-2,1,2,8,7,6,4,5};
      //Arrays.sort(array);
  System.out.println(maxProduct(y));
      //printarray("The sorted array is : ", array);
      //int index = Arrays.binarySearch(array,88);
      //System.out.println(index);
      //array = insertToArray(array,88);
      //printarray("The final array is : ", array);
	
      //mystery(0);
      //System.out.println("it is: "+numOccur('Z',""));
      //File f = new File("/users/Zhangqi/Desktop");
      //System.out.println(f.getPath());
      //File[] files = f.listFiles();
      //System.out.println(files);
      //print(f);
	}
     public static int maxProduct(int[] nums) {
        if (0 == nums.length)
            return 0;
        else{
            int maxPre = nums[0];
            int minPre = nums[0];
            int maxNow = nums[0];
            int minNow = nums[0];
            int maxFinal = nums[0];;
           // int MaxFinal;
            for (int i = 1; i<nums.length; i++){
                minNow = Math.min(Math.min(minPre*nums[i],minPre),nums[i]);
                System.out.println("i = " + i+ "; minNow = " + minNow);
                maxNow = Math.max(Math.max(maxPre*nums[i],maxPre),nums[i]);
                System.out.println("i = " + i+ "; maxNow = " + maxNow);
                maxFinal = Math.max(minPre*nums[i],maxNow);
                minPre = minNow;
                maxPre = maxNow;
            }
            return maxFinal;
        }
    }
		public static void print(int x){
			System.out.println(x);
		}

      public static int maximumProduct(int[] nums) {
        Arrays.sort(nums);
        if (nums[nums.length-3] > 0) {
            int outmax1 = nums[0] * nums[1] * nums[nums.length-1];
            int outmax2 = nums[nums.length-1]*nums[nums.length-2]*nums[nums.length-3];
            return Math.max(outmax1,outmax2);
        }
        return 0;
    }


      private static void printarray (String message, int array[]){
      	System.out.print(message);
      	for (int i = 0; i < array.length; i++) {
      		if (i != 0) {
      			System.out.print(", ");
      		}
      		System.out.print(array[i]);
      	}
      	System.out.println("\n");
      }

  public static void mystery(int i) {
if (i <= 0) { // base case
return;
}
// recursive case
System.out.println(i);
mystery(i - 1);
System.out.println(i);
}

public static int numOccur(char x, String string){
	if (string == null || string.equals("")) 
		return 0;
	
	else{
		int nOc = numOccur(x, string.substring(1));
		if (x == string.charAt(0))
			nOc = nOc + 1;
		return nOc;
	}
	
}

	public static void print(File f) {
		System.out.println(f.getPath());
		
		if (f.isDirectory()) {
			File[] files = f.listFiles();
			for (int i = 0; i < files.length; i++) {
				print(files[i]);
			}
		}
	}

}