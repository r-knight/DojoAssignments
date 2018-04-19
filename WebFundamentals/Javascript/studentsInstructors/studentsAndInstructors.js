var students = [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
]

function printStudents(students)
{
	for (var i = 0; i < students.length; i++)
	{
		console.log(students[i].first_name, students[i].last_name);
	}
}

var users = {
 'Students': [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }
 
 function printStudentsAndInstructors(studentsAndInstructors)
 {
	for (var i = 0; i < studentsAndInstructors['Students'].length; i++)
	{
		console.log(i+1 + " - " + studentsAndInstructors['Students'][i].first_name.toUpperCase() + " " +
		studentsAndInstructors['Students'][i].last_name.toUpperCase() + " - " +
		(studentsAndInstructors['Students'][i].first_name.length + studentsAndInstructors['Students'][i].last_name.length));
	}
	
	for (var j = 0; j < studentsAndInstructors['Instructors'].length; j++)
	{
		console.log(j+1 + " - " + studentsAndInstructors['Instructors'][j].first_name.toUpperCase() + " " + 
		studentsAndInstructors['Instructors'][j].last_name.toUpperCase() + " - " + 
		(studentsAndInstructors['Instructors'][j].first_name.length + studentsAndInstructors['Instructors'][j].last_name.length) );
	}
 }
 
 printStudents(students);
 printStudentsAndInstructors(users);