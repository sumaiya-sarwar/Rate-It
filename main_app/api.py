# import requests
# from django.shortcuts import render
# from .models import Book

# API_KEY = "AIzaSyAqpuvSILVryCqlHAu8RaZ5NWH8QwOF8wk"

# # url = f"https://www.googleapis.com/books/v1/volumes?q=search+terms&key={API_KEY}"



# # def get_books(request):
# #     response = requests.get(url).json()
    
# def get_books(query):
#     print("API_FUNCTION_CALLED")
#     url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={API_KEY}"
#     response = requests.get(url)

#     books = []

#     if response.status_code == 200:
#         response = response.json()
#         items = response["items"]
#         for item in items:
#             img = "" #placeholder
#             description = ''
#             volumeInfo = item["volumeInfo"]
#             print(volumeInfo)
            
#             # Title
#             title = volumeInfo["title"]
#             print("Title: ", title)

#             # Authors
#             author = volumeInfo["authors"] # author variable has to be changed to an array?
#             print("Author: ", author[0])

#             # Image
#             try:
#                 imageLinks = volumeInfo["imageLinks"]
#                 img = imageLinks["thumbnail"]
#             except:
#                 print("No imageLinks")

#             # Description
#             try:
#                 description = volumeInfo["description"]
#                 print("Description: ", description)
#             except:
#                 print("No description")

#             book = Book(img, title, author, description)
#             book.save()
#             Book.objects.all().values()
#             books.append(book)
#     else:
#         print(f"API Call Error: {response.status_code}")

#     print(books)
#     # return books