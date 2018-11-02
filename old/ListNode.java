public class ListNode {
    int val;
    ListNode next;
    	
    ListNode(int x) { val = x; }
  	 	
	public int getSize(ListNode x) {
        int size = 1;
        ListNode pointnode = x;
        while (pointnode.next != null) {
        	size = size + 1;
        	pointnode = pointnode.next;
        }
        return size;
	}	

    public int getRandom(ListNode x) {
        int size = getSize(x);
        int random = (int )(Math. random() * size);
        int i = 0;
        ListNode pointnode = x;
        while (i != random){
        	i = i + 1;
        	pointnode = pointnode.next;
        }
        
        int getvalue = pointnode.val;

        return getvalue;

    }

	public static void main(String[] args) {
		ListNode x =new ListNode(3);
		x.next = new ListNode(4);
		x.next.next = null;



        int seze = x.getSize(x);
        int getrad = x.getRandom(x);
        System.out.println(seze);
        System.out.println(getrad);


	}
}