from flask import Flask, jsonify, request, Response

app = Flask(__name__)

books = [
    {
        'name': 'The first name',
        'price': 7.99,
        'isbn': 123123123
    },
    {
        'name' : 'The second name',
        'price': 9.77,
        'isbn': 321321900
    }
]

def validBookObject(bookObject):
    if ("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return False

@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()
    if(validBookObject(request_data)):
        new_book = {
            "name": request_data['name'],
            "price": request_data['price'],
            "isbn": request_data['isbn']
        }
        books.insert(0, new_book)
        Response("", 201, "")
        return "True"
    else:
        return "False"

#GET /store
@app.route('/books')
def get_books():
    return jsonify({'books': books})

#GET /books/123123123
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    print(type(isbn))
    for book in books:
        if book["isbn"] == isbn:
            return_value = {
                'name': book["name"],
                'price': book["price"]
            }
    return jsonify(return_value)

app.run(port=5000)
