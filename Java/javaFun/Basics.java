public class Basics {
    public void print1To255() {
		for (int i = 1; i <=255; i++){
			System.out.println(i);
		}
		return;
    }

	public void printOdds1To255(){
		for (int i = 1; i <=255; i+=2){
			System.out.println(i);
		}
		return;
	
	}

	public void printSum(){
		int sum = 0;
		for (int i = 0; i <=255; i++){
			sum += i;
			System.out.println(String.format("New number: %d Sum: %d", i, sum));
		}
		return;
		
	}

	public void printArray(int[] integerArray){
		for (int i = 0; i < integerArray.length; i++){
			System.out.println(integerArray[i]);
		}
		return;
	}
	
	public Integer findMax(int[] integerArray){
		if (integerArray.length == 0){
			Integer max = null;
			return max;
		}
		int max = integerArray[0];
		for (int i = 0; i < integerArray.length; i++){
			if (integerArray[i] > max){
				max = integerArray[i];
			}
		}
		
		return max;
	}
	public double findAverage(int[] integerArray){
		if (integerArray.length == 0){
			Integer average = null;
			return average;
		}
		double sum = 0;
		for (int i = 0; i < integerArray.length; i++){
			sum += integerArray[i];
		}
		
		double average = (sum/integerArray.length);
		return average;
	}

	public int[] odds1To255(){
		int[] y = new int[128];
		for (int i = 0; i < 128; i++){
			y[i] = (2*i + 1);
		}
		return y;
	}

	public Integer greaterThanY(int[] array, int y){
		if (array.length == 0){
			return null;
		}
		int valuesGreaterThanY = 0;
		for (int i = 0; i < array.length; i++){
			if (array[i] > y){
				valuesGreaterThanY +=1;
			}
		}
		return valuesGreaterThanY;
	}
	
	public void squareArrayValues(int[] array){
		if (array.length == 0){
			return;
		}
		for (int i = 0; i < array.length; i++){
			int val = array[i];
			array[i] = val*val;
		}
		return;
	}
	public void elminateNegativeNumbers(int[] array){
		if (array.length == 0){
			return;
		}
		for (int i = 0; i < array.length; i++){
			if (array[i] < 0){
				array[i] = 0;
			}
		}
		return;
	}

	public int[] maxMinAverage(int[] array){
		int[] maxMinAvg = new int[3];

		if (array.length == 0){
			maxMinAvg[0] = 0;
			maxMinAvg[1] = 0;
			maxMinAvg[2] = 0;
			return maxMinAvg;
		}
		int max = array[0];
		int min = array[0];
		int average = array[0];

		int sum = 0;
		for (int i = 0; i < array.length; i++)
		{
			if (array[i] < min){
				min = array[i];
			}
			else if (array[i] > max){
				max = array[i];
			}
			sum += array[i];
		}

		average = (sum/array.length);
		maxMinAvg[0] = max;
		maxMinAvg[1] = min;
		maxMinAvg[2] = average;
		return maxMinAvg;
	}

	public void shiftArrayValsLeft(int[] array){
		if (array.length == 0){
			return;
		}
		for (int i = 0; i < array.length-1; i++){
			array[i] = array[i+1];
		}
		array[array.length-1] = 0;
		return;
	}
}
