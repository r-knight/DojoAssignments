import java.util.ArrayList;
public class ListOfExceptionsTest{
	public static void main(String[] args){
		ListOfExceptions lOE = new ListOfExceptions();

		ArrayList<Object> testData = new ArrayList<Object>();
		testData.add("13");
		testData.add("hello world");
		testData.add(48);
		testData.add("Goodbye World");

		lOE.castItemsAsIntegers(testData);
	}

}