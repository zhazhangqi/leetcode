import java.util.*;
class eghashtable{
    public static void main(String args[]){
        Hashtable has=new Hashtable();
        has.put("one",new Integer(1));
        has.put("two",new Integer(2));
        has.put("three",new Integer(3));
        has.put("four",new Double(12.3));
        Set s=has.keySet();
        for(Iterator<String> i=s.iterator();i.hasNext();){
            System.out.println(has.get(i.next()));
        }
    }
}