public class testSort{
	public static testSort(){
		String[] input = {"cows", "above", "below", "duwell"};
		String[] expected = {"above", "below", "cows", "duwell"};
		Sort.sort(input);
		org.junit.Assert.assertArrayEquals(expected, input);
	}
	public static void main(String[] args){
		testSort();
	}	
}