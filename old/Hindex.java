
/**
 * Created by zhangqi on 5/21/17.
 */
import java.util.*;
public class Hindex {
    //public int Hindex;
    public static int FindHindex(int[] Citation){
        int Hindex = Citation.length + 1;
        boolean flag = true;
        while(flag) {
            for (int each : Citation) {
                int tempindex = Hindex;
                if (each < Hindex) {
                    Hindex--;
                    //if (tempindex)
                    //System.out.println("each is "+ each);
                    //System.out.println("Hindex-- is "+ Hindex);
                }
                else flag = false;
            }
        }
        return Hindex;
    }
    public static void main(String[] args){
        int Citation[] = {3,1,0,5,6,0,7};
        int ThisH = FindHindex(Citation);
        System.out.print("The Hindex is "+ ThisH);
    }
}
