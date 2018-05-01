students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def printStudentNames(studentDict):
    for student in studentDict:
        print (student['first_name'], student['last_name'])

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printUserNames(usersDict):
    print ("Students")
    for i in range(len(usersDict['Students'])):
        print (i+1, usersDict['Students'][i]['first_name'], usersDict['Students'][i]['last_name'],"-",len(usersDict['Students'][i]['first_name']) + len(usersDict['Students'][i]['last_name']))
    print ("Instructors")
    for j in range(len(usersDict['Instructors'])):
        print (j+1, usersDict['Instructors'][j]['first_name'], usersDict['Instructors'][j]['last_name'],"-", len(usersDict['Instructors'][j]['first_name']) + len(usersDict['Instructors'][j]['last_name']))
