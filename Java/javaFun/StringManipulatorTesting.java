public class StringManipulatorTesting{
	public static void main(String[] args){
		StringManipulator sM = new StringManipulator();
		Integer integerResult;
		String strResult;
		strResult = sM.trimAndConcat("        Hello   ", " World         ");
		System.out.println(strResult);

		String strTarget = "Wo";
		integerResult = sM.getIndexOrNull(strResult, strTarget);
		System.out.println(integerResult);
		strTarget = "lll";
		integerResult = sM.getIndexOrNull(strResult, strTarget);
		System.out.println(integerResult);

		char charTarget = 'w';
		integerResult = sM.getIndexOrNull(strResult, charTarget);
		System.out.println(integerResult);
		charTarget = 'l';
		integerResult = sM.getIndexOrNull(strResult, charTarget);
		System.out.println(integerResult);
		charTarget = 'z';
		integerResult = sM.getIndexOrNull(strResult, charTarget);
		System.out.println(integerResult);

		strResult = sM.concatSubstring("potato", 2, 6, "pizza");
		System.out.println(strResult);
		strResult = sM.concatSubstring("meh", 2, 5, "paihsdfpaiohf");
		System.out.println(strResult);

		return;

	}
}