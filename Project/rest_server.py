from flask import Flask, url_for, request, redirect, abort, jsonify
from santaPresentsDAO import santaPresentsDAO

app = Flask(__name__, static_url_path='',static_folder='staticpages')


@app.route('/')
def index():
        return "hello World"

#get all
@app.route('/santaPresents')
def getAll():
        return jsonify(santaPresentsDAO.getAll())

# find by id
# curl http://127.0.0.1:5000/santaPresents/3
@app.route('/santaPresents/<int:id>')
def findById(id):

        return jsonify(santaPresentsDAO.findById(id))

#create
#curl -X POST -H Content-Type:application/json -d "{\"id\":1, \"name\":\"Test 1\", \"from_age\":12, \"price\":10}" http://127.0.0.1:5000/santaPresents
@app.route('/santaPresents', methods=['POST'])
def Create():

        if not request.json:
                abort(400)

        present = {
                "id": request.json["id"],
                "name": request.json["name"],
                "from_age": request.json["from_age"],
                "price": request.json["price"]
        }

        return jsonify(santaPresentsDAO.create(present))

# update
# curl -X PUT -H Content-Type:application/json -d "{\"name\":\"Test 2\", \"price\":999}" http://127.0.0.1:5000/santaPresents/2
@app.route('/santaPresents/<int:id>', methods=['PUT'])
def update(id):
        foundPresent = santaPresentsDAO.findById(id)
        print(foundPresent)
        if foundPresent == {}: # If found blank return 404 error
                return jsonify({}), 404
        currentPresent = foundPresent
        if 'name' in request.json:
                currentPresent['name'] = request.json['name']

        if 'from_age' in request.json:
                currentPresent['from_age'] = request.json['from_age']

        if 'price' in request.json:
                currentPresent['price'] = request.json['price']
        
        santaPresentsDAO.update(currentPresent)
        return jsonify(currentPresent)


#delete
# curl -X DELETE http://127.0.0.1:5000/santaPresents/1
@app.route('/santaPresents/<int:id>', methods=['DELETE'])
def Delete(id):
        santaPresentsDAO.delete(id)
        return jsonify({"done":True})

if __name__== "__main__":
        print("in if")
        app.run(debug=True)