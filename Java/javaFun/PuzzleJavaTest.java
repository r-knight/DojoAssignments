import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;
public class PuzzleJavaTest{
	public static void main(String[] args){
		PuzzleJava pJ = new PuzzleJava();

		ArrayList<Integer> testArray = new ArrayList<Integer>();
		testArray.add(3);
		testArray.add(5);
		testArray.add(1);
		testArray.add(2);
		testArray.add(7);
		testArray.add(9);
		testArray.add(8);
		testArray.add(13);
		testArray.add(25);
		testArray.add(32);
		ArrayList<Integer> bigNums = pJ.printSumReturnBig(testArray);
		System.out.println(bigNums);

		ArrayList<String> testStrArray = new ArrayList<String>();
		testStrArray.add("Nancy");
		testStrArray.add("Jinichi");
		testStrArray.add("Fujibayashi");
		testStrArray.add("Momochi");
		testStrArray.add("Ishikawa");
		ArrayList<String> longNames = pJ.shufflePrintAllReturnLong(testStrArray);
		System.out.println("Names longer than 5 letters:");
		System.out.println(longNames);

		char[] alpha = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
		ArrayList<Character> alphabet = new ArrayList<Character>();
		for (int i = 0; i < alpha.length; i++){
			alphabet.add(alpha[i]);
		}
		pJ.shuffleAlphabetPrintFirstLast(alphabet);

		ArrayList<Integer> nums = new ArrayList<Integer>();
		nums = pJ.generate10Nums();
		System.out.println(nums);

		pJ.generate10NumsPlus();

		String word = pJ.generate5CharString();
		System.out.println(word);

		ArrayList<String> strings = new ArrayList<String>();
		strings = pJ.generateTen5CharStrings();
		System.out.println(strings);
	}

}