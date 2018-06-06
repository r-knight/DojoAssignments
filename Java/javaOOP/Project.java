public class Project{
	private String name;
	private String description;


	public Project() {

	}

	public Project(String name) {
		this.name = name;
	}

	public Project(String name, String description) {
		this.name = name;
		this.description = description;
	}


    // getter
    public String getName() {
        return this.name;
    }
    // setter
    public void setName(String name) {
        this.name = name;        
    }

    // getter
    public String getDescription() {
        return this.description;
    }
    // setter
    public void setDescription(String description) {
        this.description = description;      
    }


	public void elevatorPitch (){
		System.out.println(this.name + ": " + this.description);
	}
	
}