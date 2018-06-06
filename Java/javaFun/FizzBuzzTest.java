public class FizzBuzzTest{
	public static void main(String[] args){
		FizzBuzz fB = new FizzBuzz();
		String result = fB.fizzBuzz(1);
		System.out.println(result);
		result = fB.fizzBuzz(3);
		System.out.println(result);
		result = fB.fizzBuzz(5);
		System.out.println(result);
		result = fB.fizzBuzz(15);
		System.out.println(result);
		result = fB.fizzBuzz(45);
		System.out.println(result);
	}
}