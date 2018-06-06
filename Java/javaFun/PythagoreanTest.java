public class PythagoreanTest{
	public static void main(String[] args){
		Pythagorean pyt = new Pythagorean();
		double testData = pyt.calculateHypotenuse(1, 1);
		System.out.println(testData);
		testData = pyt.calculateHypotenuse(3, 4);
		System.out.println(testData);
	}
}