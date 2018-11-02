import java.util.*;
class NumArray {
    int[] x;
    HashMap<Integer, Integer> y = new HashMap();
    public NumArray(int[] nums) {
        x = nums;
    }
    
    public int sumRange(int i, int j) {
        int sumi = 0;
        int sumj = 0;
        if(y.containsKey(i-1)) sumi = y.get(i-1);
        else{
            int k = i-1;
            while(k>-1) sumi = sumi + x[k--];
            y.put(i-1, sumi);
            System.out.println(y);
        }
        if(y.containsKey(j)) sumj = y.get(j);
        else{
            int k = j;
            while(k>-1) sumj = sumj + x[k--];
            y.put(j, sumj);
        }
        return sumj-sumi;
    }
    public static void main(String[] args) {
        int[] nums = {-2,0,3,-5,2,-1};
        NumArray obj = new NumArray(nums);
                    System.out.println(obj.y);

        System.out.println(obj.sumRange(0,2));
                            System.out.println(obj.y);

        System.out.println(obj.sumRange(2,5));
                            System.out.println(obj.y);

        System.out.println(obj.sumRange(0,5));
                            System.out.println(obj.y);

    }
}