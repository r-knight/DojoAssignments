import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;
public class PuzzleJava{
	public ArrayList<Integer> printSumReturnBig(ArrayList<Integer> array){
		ArrayList<Integer> bigNums = new ArrayList<Integer>();
		if(array.size() == 0){
			return bigNums;
		}

		int sum = 0;

		for (Integer value : array){
			sum += value;
			if (value > 10){
				bigNums.add(value);
			}
		}
		System.out.println("Sum: " + sum);
		return bigNums;
	}

	public ArrayList<String> shufflePrintAllReturnLong(ArrayList<String> array){
		ArrayList<String> longNames = new ArrayList<String>();
		if(array.size() == 0){
			return longNames;
		}

		Collections.shuffle(array);
		for (String value : array){
			System.out.println(value);
			if (value.length() > 5){
				longNames.add(value);
			}
		}
		return longNames;
	}

	public void shuffleAlphabetPrintFirstLast(ArrayList<Character> alphabet){
		
		Collections.shuffle(alphabet);
		Character first = alphabet.get(0);
		Character last = alphabet.get(alphabet.size()-1);
		System.out.println("Last character: " + last);
		System.out.println("First character: " + first);
		if ("AEIOUaeiou".indexOf(first) != -1){
			System.out.println("First character was a vowel!");
		}
	}

	public ArrayList<Integer> generate10Nums(){
		ArrayList<Integer> nums = new ArrayList<Integer>();

		Random r = new Random();
		for (int i = 0; i < 10; i++){
			nums.add(r.nextInt(45) + 55);
		}
		return nums;
	}
	public ArrayList<Integer> generate10NumsPlus(){
		ArrayList<Integer> nums = new ArrayList<Integer>();

		Random r = new Random();
		for (int i = 0; i < 10; i++){
			nums.add(r.nextInt(45) + 55);
		}
		Collections.sort(nums);
		System.out.println(nums);
		System.out.println("Min: " + nums.get(0));
		System.out.println("Max: " + nums.get(9));
		return nums;
	}

	public String generate5CharString(){
		char[] chars = new char[5];
		Random r = new Random();
		char[] alpha = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
		for (int i = 0; i < 5; i++){
			chars[i] = alpha[r.nextInt(25)];
		}

		String word = new String(chars);
		return word;
	}

	public ArrayList<String> generateTen5CharStrings(){
		ArrayList<String> strings = new ArrayList<String>();

		for (int i = 0; i < 10; i++){
			strings.add(generate5CharString());
		}
		return strings;
	}
}