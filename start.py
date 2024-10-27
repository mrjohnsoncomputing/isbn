import requests

def get_book_from_isbn(isbn):
  request = "https://openlibrary.org/isbn/{}.json".format(isbn)
  result = requests.get(request).json()
  return result

def print_raw_book_data(book):
  for key in book:
    print(key.capitalize() + ":", book[key])  

def print_book_data(book):
  keys = ["full_title", "number_of_pages", "publish_date"]
  print("Author:", get_author(book))
  for key in keys:
    print(key.capitalize() + ":", book[key])

def get_author_code(book):
  author_code = book["authors"][0]["key"]
  return author_code

def get_author(book):
  code = get_author_code(book)
  request = "https://openlibrary.org{}.json".format(code)
  result = requests.get(request).json()
  return result["name"]

def test_book_api():
  the_salt_path = "9781405937184"
  book = get_book_from_isbn(the_salt_path)
  print_book_data(book)

