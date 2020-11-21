from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='',static_folder='staticpages')

books=[
        {  "id":1, "Title":"Harry Potter", "Author": "JK", "Price":1000 },
        {  "id":2, "Title":"Some cook book ", "Author": "Mr. Angry Man", "Price":2000 },
        {  "id":3, "Title":"Python made easy", "Author": "Some Liar", "Price":1500 }
]
nextId=4

@app.route('/')
def index():
        return "hello World"

#get all
@app.route('/books')
def getAll():
        return jsonify(books)

# find by id
@app.route('/books/<int:id>')
def findById(id):
        foundBooks = list(filter (lambda t : t["id"]== id, books))
        if len(foundBooks) == 0:
                return jsonify({}), 204
        return jsonify(foundBooks[0])
        return "served by findById with id "+ str(id)

#create
#curl -X POST -H "content-type:application/json" -d "{\"Title\":\"test\", \"Author\":\"Some Guy\", \"Price\"":123} http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def Create():
        global nextId
        if not request.json:
                abort(400)

        book = {
                "id": nextId,
                "Title": request.json["Title"],
                "Author": request.json["Author"],
                "Price": request.json["Price"]
        }
        books.append(book)
        nextId += 1
        return jsonify(book)

# update
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
        foundBooks = list(filter (lambda t: t["id"] == id, books))
        if len(foundBooks) == 0:
                return jsonify({}), 404
        currentBook = foundBooks[0]
        if 'Title' in request.json:
                currentBook['Title'] = request.json['Title']

        if 'Title' in request.json:
                currentBook['Author'] = request.json['Author']

        if 'Title' in request.json:
                currentBook['Price'] = request.json['Price']

        return jsonify(currentBook)


#delete
@app.route('/books/<int:id>', methods=['DELETE'])
def Delete(id):
        foundBooks = list(filter (lambda t: t["id"] == id, books))
        if len(foundBooks) == 0:
                return jsonify({}), 404
        books.remove(foundBooks[0])

        return jsonify({"done":True})

if __name__== "__main__":
        print("in if")
        app.run(debug=True)