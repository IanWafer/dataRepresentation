from santaPresentsDAO import santaPresentsDAO

present1= {
    'id': 1,
    'name': 'Test 1',
    'from_age': 12,
    'price': 10
}

present2 = {
    'id': 2,
    'name': 'Test 2',
    'from_age': 12,
    'price': 10
}

present3 = {
    'id': 3,
    'name': 'Test 3',
    'from_age': 30,
    'price': 12
}

present4 = {
    'id': 4,
    'name': 'Test 4',
    'from_age': 8,
    'price': 15
}

present5 = {
    'id': 5,
    'name': 'Test 5',
    'from_age': 20,
    'price': 10
}

print("Create")
returnvalue =  santaPresentsDAO.create(present1)
returnvalue =  santaPresentsDAO.create(present2)
returnvalue =  santaPresentsDAO.create(present3)
returnvalue =  santaPresentsDAO.create(present4)
returnvalue =  santaPresentsDAO.create(present5)
print("Get All")
returnvalue = santaPresentsDAO.getAll()
print(returnvalue)
print("Find by id")
returnvalue = santaPresentsDAO.findById(present1['id'])
print(returnvalue)
print("Update")
returnvalue = santaPresentsDAO.update(present1)
print(returnvalue)
print("Delete")
returnvalue = santaPresentsDAO.delete(present1['id'])
print(returnvalue)
