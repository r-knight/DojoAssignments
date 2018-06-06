import java.util.ArrayList;
public class ListOfExceptions{

	public void castItemsAsIntegers(ArrayList<Object> testData){

		for (int i = 0; i < testData.size(); i++){
			try{
				Integer castedValue = (Integer) testData.get(i);
			}
			catch (ClassCastException e)
			{
				System.out.println(e);
				System.out.println("Array index: " + i);
				System.out.println("Array value: " + testData.get(i));
			}
		}
	}



}