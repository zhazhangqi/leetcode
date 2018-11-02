import java.util.*;
public class Leetcode621{
    public int leastInterval(char[] tasks, int n) {
        LinkedHashMap<Character,Integer> tasksmap = new LinkedHashMap<Character,Integer>();
        // load all tasks into a map with tasks as Key and frenquency as Value
        for (char x : tasks) {
        	if (tasksmap.containsKey(x)){
				int xvalue = tasksmap.get(x);
        		tasksmap.put(x,++xvalue);
        	}
        	else {
        		tasksmap.put(x,1);
        	}
		}

	    List<Integer> mapValues = new ArrayList(tasksmap.values());
	    ArrayList<Att> taskFreq = new ArrayList<Att>();
	    for (int x : mapValues) {
	    	Att attx = new Att(x);
	    	taskFreq.add(attx);
	    }

	    int interval = 0;
	    while(taskFreq.size() > 0){
	    	Collections.sort(taskFreq);
	    	//System.out.println("interval = "+interval);
	    	int checkIdel = interval;
	    	
	    	for (Att temp : taskFreq) {
	    		
	    		if (temp.timer < 1) {
	    			interval ++;
	    			temp.task --;
	    			for (Att temp1 : taskFreq) {
	    				temp1.timer --;
	    				//System.out.println("beforeN-task = "+temp1.task+"; timer = "+temp1.timer);
	    			}
	    			temp.timer = n;
	    			if (temp.task < 1) {
	    				taskFreq.remove(temp);
	    				
	    			}
	    			//System.out.println("taskFreq size = "+taskFreq.size());
	    			break;
	    		}
	    	}
	    	if (checkIdel == interval) {
	    		interval++;
	    		for (Att temp1 : taskFreq) {
	    				temp1.timer --;
	    				//System.out.println("idelN-task = "+temp1.task+"; timer = "+temp1.timer);
	    			}
	    	}
	    }
        return interval;
        
    }



    public static void main(String[] args) {
    	char[] tasks = {'E', 'A', 'B', 'B', 'B', 'C'};
    	Leetcode621 x =new Leetcode621();
    	System.out.println(x.leastInterval(tasks,2));
    }
}
// Define a class with info of taskfrequecy and cool timer
class Att implements Comparable<Att>{ 
	int task;
	int timer = 0;
	public Att(int task){
		this.task = task;
	}
	//define the sort using task value;
	public int compareTo(Att p) {
    int result =  p.task-this.task;
    return result;
}
}

/*    public LinkedHashMap<Character,Integer> sortByValue(LinkedHashMap<Character,Integer> passedMap){
    	LinkedHashMap<Character,Integer> sortedMap = new LinkedHashMap<Character,Integer>();
    	List<Integer> mapValues = new ArrayList(passedMap.values());
    	List<Character> mapKeys = new ArrayList(passedMap.keySet());
    	Collections.sort(mapValues,Collections.reverseOrder());
    	for (Integer x : mapValues) {
    		for (Character y : mapKeys) {
    			if (x == passedMap.get(y)) {
    				sortedMap.put(y,x);
    				mapKeys.remove(y);
    				break;
    			}
    		}
    	}
    	return sortedMap;
    }
    */