public class ProjectTest{
	public static void main(String[] args){
		Project blankProject = new Project();
		Project namedProject = new Project("named project");
		Project namedAndDetailedProject = new Project("named and detailed", "this is a description");

		namedProject.setDescription("description added by setDescription method");
		System.out.println(namedProject.getDescription());
		
		blankProject.setName("new name for blank");
		System.out.println(blankProject.getName());

		namedAndDetailedProject.elevatorPitch();
	}
}