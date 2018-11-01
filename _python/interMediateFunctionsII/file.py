#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 1. Given
    # x = [ [5,2,3], [10,8,9] ] 
    # students = [
    #         {'first_name':  'Michael', 'last_name' : 'Jordan'},
    #         {'first_name' : 'John', 'last_name' : 'Rosales'}
    # ]
    # sports_directory = {
    #     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    #     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
    # }
    # z = [ {'x': 10, 'y': 20} ]
        # How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].  
    # print(x[1][0])
    # x[1][0] = 15
    # print(x)
        # How would you change the last_name of the first student from 'Jordan' to "Bryant"?
    # print(students[0]['last_name'])
    # students[0]['last_name'] = 'Bryant'
    # print(students)
        # For the sports_directory, how would you change 'Messi' to 'Andres'?
    # print(sports_directory['soccer'][0])
    # sports_directory['soccer'][0] = 'Andres'
    # print(sports_directory)
        # For z, how would you change the value 20 to 30?
    # print(z[0]['y'])
    # z[0]['y'] = 30
    # print(z)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # 2. Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.  For example, given the following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    # iterateDictionary( students ) should output

    # first_name - Michael, last_name - Jordan
    # first_name - John, last_name - Rosales
    # first_name - Mark, last_name - Guillen
    # first_name - KB, last_name - Tonel
    # def iterateDictionary(studentList):
    #     print(type(studentList))
    #     for student in studentList:
    #         keys = student.keys()
    #         keys = list(keys)
    #         # print(keys)
    #         print(keys[0],' - ', student[keys[0]], ', ', keys[1], ' - ', student[keys[1]])
            # print(type(student))
    # iterateDictionary(students)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # 3. Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.  For example, iterateDictionary2('first_name', students) should output

    # Michael
    # John
    # Mark
    # KB

    # def iterateDictionary2(studentKey, students):
    #     for stud in students:
    #     #     print(stud[studentKey])
    #         # print(students[studentKey])
    #         for st in stud.items():
    #             print(type(st))

    # iterateDictionary2('first_name', students)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # 4.  Say that

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
    # Create a function that prints the name of each location and also how many locations the Dojo currently has.  Have the function also print the name of each instructor and how many instructors the Dojo currently has.  For example, printDojoInfo(dojo) should output

def iterateDictionary3(studentDictonary):
    for key, value in studentDictonary.items():
        # print(key)
        # print(value)
        print(len(value), key.upper())
        for l in value:
            print(l)
        # print(type(dojo))
    # print('*'*90)
    # for dojo in studentDictonary:
    #     print(dojo)
    #     print(type(dojo))
    #     print(studentDictonary[dojo])

iterateDictionary3(dojo)
    # 7 LOCATIONS
    # San Jose
    # Seattle
    # Dallas
    # Chicago
    # Tulsa
    # DC
    # Burbank
        
    # 8 INSTRUCTORS
    # Michael
    # Amy
    # Eduardo
    # Josh
    # Graham
    # Patrick
    # Minh
    # Devon