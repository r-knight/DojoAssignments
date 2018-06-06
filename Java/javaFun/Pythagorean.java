public class Pythagorean {
    public double calculateHypotenuse(int legA, int legB) {
        // the hypotenuse is the side across the right angle. 
        // calculate the value of c given legA and legB
        int legASquared = legA * legA;
		int legBSquared = legB * legB;
		double legC = Math.sqrt(legASquared + legBSquared);
		return legC;
    }
}