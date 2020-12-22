import  mysql.connector
import dbconfig as cfg

class santaPresentsDAO:
    db = ''
    def __init__(self):
        self.db = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['username'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
)
    # Create function with SQL insert commands
    def create(self, present):
        cursor = self.db.cursor()
        sql ='INSERT INTO santaPresents (id, name, fromAge, price) values (%s, %s, %s, %s)' 
        values = [
            present['id'],
            present['name'],
            present['fromAge'],
            present['price']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    #  Display all wwith SQL select * command
    def getAll(self):
        cursor = self.db.cursor()
        sql='SELECT * FROM santaPresents'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            resultAsDict = self.convertToDict(result) # Convert tuple values to dict objects for html inputs
            returnArray.append(resultAsDict) # Add dict to array

        return returnArray

    # Convert tuple values to dict objects for html inputs
    def convertToDict(self, result):
        colnames = ['id', 'name', 'fromAge', 'price']
        present = {}

        if result: # Sanity check no null values being passed in
            for i, colName in enumerate(colnames): # Go through colnames one by one to determine if exists
                value = result[i]
                present[colName] = value # Take colName and make equal to value from tuple
            return present

    # Used to find the present based on input id
    def findById(self, id):
        cursor = self.db.cursor()
        sql='SELECT * FROM santaPresents WHERE id= %s'
        values = [id]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)

    # Update fields based on values entered
    def update(self, present):
        cursor = self.db.cursor()
        sql ='UPDATE santaPresents SET name = %s, fromAge = %s, price = %s WHERE id =%s'
        values = [
            present['name'],
            present['fromAge'],
            present['price'],
            present['id']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return present

    # Delete selected row based on id
    def delete(self, id):
        cursor = self.db.cursor()
        sql='DELETE FROM santaPresents WHERE id= %s'
        values = [id]
        cursor.execute(sql, values)

        return  {}
        print('delete done')

santaPresentsDAO = santaPresentsDAO()