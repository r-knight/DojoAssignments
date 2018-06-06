public class FizzBuzz {
    public String fizzBuzz(int number) {
        // fizzbuzz logic here
		String result;
		if (number % 15 == 0){
			result = "FizzBuzz";
		}
		else if(number % 3== 0){
			result = "Fizz";
			
		}
		else if(number % 5 == 0){
			result = "Buzz";
		}
		else{
			result = Integer.toString(number);
		}
		return result;
    }
}
