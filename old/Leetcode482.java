import java.util.*;
import java.lang.*;
public class Leetcode482{
	public static String licenseKeyFormatting(String S, int K){
		List Keyout = new LinkedList<Character>();
		for(int i=0;i<S.length();i++){
			char x = S.charAt(i);
			if(x!='-')
				Keyout.add(x);  //get rid of '-' and added the rest to a list
		}

		int DashIndex = (Keyout.size())%K;
		if (DashIndex == 0)
			DashIndex = DashIndex+K;
		while(DashIndex < Keyout.size()){
			Keyout.add(DashIndex,'-');
			DashIndex = DashIndex+1+K;
		}

		String Sout = new String();
		for(int i=0;i<Keyout.size();i++)
			Sout = Sout.concat(Keyout.get(i).toString());  //Convert each Char at List to a single String
		
		return Sout.toUpperCase();
	}

	public static void main(String[] args) {
		System.out.println("The Key is: "+ licenseKeyFormatting("w1y2-rt4A-3tc0-r7-4eck",3));
	}
}