
import java.util.*;

public class topKFrequent {
    public static List<Integer> topKFrequent(int[] nums, int k) {      
        List<Integer> FinalList = new ArrayList();
        List<Integer> SingleNums = new ArrayList();
        List<Integer> SingleNumsFreq = new ArrayList();
        for (int x:nums){
            boolean noThisItem = true;
            int SigSize = SingleNums.size();
            //System.out.println("SigSize:"+SigSize);
            for (int i=0; i<SigSize;i++){
                if (x==SingleNums.get(i)){
                    noThisItem = false;
                    //System.out.println("SingleNumsFreq before:"+SingleNumsFreq);
                    int Freq =SingleNumsFreq.remove(i);
                    Freq++;
                    SingleNumsFreq.add(i,Freq);
                    //System.out.println("SingleNumsFreq after:"+SingleNumsFreq);
                }
            }
            if (noThisItem){
                SingleNums.add(x);
                SingleNumsFreq.add(1);
                //System.out.println("After add new item:"+SingleNums);
                //System.out.println("After add new item Freq:"+SingleNumsFreq);
            }    
        }

        for (int i=0; i<SingleNumsFreq.size();i++){
        	if (SingleNumsFreq.get(i)>=k)
        		FinalList.add(SingleNums.get(i));
        }
    return FinalList;
    }    

    public static void main(String[] args){
        int[] testlist ={1,2};
        List<Integer> testResult = topKFrequent(testlist,2);
        System.out.println(testResult);
    }


} 




 /*      	public class IntNode{
            public int item;
            public IntNode next;
            
            public IntNode(int i, IntNode n){
                item = i;
                next = n;
            }
            public void addlast(int x){
               IntNode temp = new IntNode(88,null);
                while
            }
                    
        }
    //1->freq->2->freq->5->freq......
    public List<Integer> topKFrequent(int[] nums, int k) {      
        List FinalList = new ArrayList();
        IntNode singlenums= new IntNode(88,null);
        IntNode temp= new IntNode(66,null);
       	for(int x :nums){
        	boolean NothisItem = true;
        	
                while (temp.next != null){
                    if (x==temp.next.item){
                        temp.next.next.item++;
                        NothisItem = false;
                        if(temp.next.next.item>=k)
                            FinalList.add(temp.next.item);
                    }
        	}
                if (NothisItem == true)
                    
        }
    }
} */

