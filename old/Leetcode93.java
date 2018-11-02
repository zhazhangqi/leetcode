import java.util.*;
import java.lang.*;
public class Leetcode93{
	public static List<String> restoreIpAddresses(String s) {
		List<String> res = new ArrayList<String>();
		// divide string to 4 groups
		int slength = s.length();
		//if(slength<13){
			for(int i=1;i<slength-2;i++){
				for (int j=i+1;j<slength-1;j++){
					for(int k= j+1;k<slength; k++){
						String S1 = s.substring(0,i);String S2 = s.substring(i,j);
						String S3 = s.substring(j,k);String S4 = s.substring(k,slength);
						if(isvalid(S1) && isvalid(S2) && isvalid(S3) && isvalid(S4)) 
							res.add(S1+'.'+S2+'.'+S3+'.'+S4);
					}
				}
			}	
		//}
	return res;
	}

	public static boolean isvalid(String x){
		if(x.equals("0"))
		    return true;
		else if(x.length()<4 && x.charAt(0)!='0' && Integer.parseInt(x)<=255)
			return true;
		else return false;
	}


	public static void main(String[] args) {
		List<String> IPAddress = restoreIpAddresses("123123123");
		System.out.println(IPAddress);
	}
}