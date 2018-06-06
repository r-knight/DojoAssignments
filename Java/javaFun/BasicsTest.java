public class BasicsTest{
	public static void main(String[] args){
		Basics basics = new Basics();

		//printing only


		System.out.println("**********Printing 1 to 255**************");
		basics.print1To255();
		System.out.println("**********Printing odds 1 to 255**************");
		basics.printOdds1To255();
		System.out.println("**********Printing num and sum 0 to 255**************");
		basics.printSum();


		int[] integerArray = new int[10];
		for (int i = 0; i < 10; i ++){
			integerArray[i] = i;
		}
		System.out.println("**********Printing test array**************");
		basics.printArray(integerArray);

		Integer max = basics.findMax(integerArray);
		System.out.println("**********Printing max from test array**************");
		System.out.println(max);

		double average = basics.findAverage(integerArray);
		System.out.println("**********Printing average from test array**************");
		System.out.println(average);
		int[] odds = basics.odds1To255();
		System.out.println("**********Printing odds array 1-255**************");
		basics.printArray(odds);

		Integer greaterThan = basics.greaterThanY(odds, 110);
		System.out.println("**********Printing number of values greater than 110 in odds array**************");
		System.out.println(greaterThan);

		basics.squareArrayValues(integerArray);
		System.out.println("**********Printing test array after squaring values**************");
		basics.printArray(integerArray);

		integerArray[1] = -3;
		integerArray[7] = -8;
		integerArray[2] = -4;
		integerArray[5] = 0;
		integerArray[4] = -1;

		basics.elminateNegativeNumbers(integerArray);
		System.out.println("**********Printing test array after eliminating negatives**************");
		basics.printArray(integerArray);

		int[] maxMinAvg = basics.maxMinAverage(integerArray);
		System.out.println("**********Printing min, max, average of test array**************");
		basics.printArray(maxMinAvg);

		basics.shiftArrayValsLeft(integerArray);
		System.out.println("**********Printing test array after shifting array values left**************");
		basics.printArray(integerArray);
		return;
	}
}