from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


# ? Basic
@app.get("/books")
async def read_all_books():
    return BOOKS


# ? Pathname
@app.get("/books/{book_title}")
async def get_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


@app.get("/books/byauthor/{author}")
async def get_book_by_author(author: str):
    books_to_return = []

    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)

    return books_to_return


# ? Query parameter
# ! Do not forget "/" at the end of url otherwise query params won't work
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []

    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


# ? Pathname + Query parameter
# ! Do not forget "/" at the end of url otherwise query params won't work
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []

    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold() and \
                book.get("category").casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


# ? Post request: takes [Body()] which has to be imported
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


# ? Put request: takes [Body()] which has to be imported
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book


# ? Delete request: removes dictionary from "BOOKS"
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
