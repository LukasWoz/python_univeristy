# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import xml.sax
import xml.dom.minidom

class BookHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs):
        self.current = name
        if name == "book":
            print(f"-- Book {attrs['id']}--")

    def characters(self, content):
        if self.current == "author":
            self.author = content
        elif self.current == "title":
            self.title = content
        elif self.current == "genre":
            self.genre = content
        elif self.current == "price":
            self.price = content
        elif self.current == "publish_date":
            self.publish_date = content
        elif self.current == "description":
            self.description = content

    def endElement(self, name):
        if self.current == "author":
            print(f"Author: {self.author}")
        elif self.current == "title":
            print(f"Title: {self.title}")
        elif self.current == "genre":
            print(f"Genre: {self.genre}")
        elif self.current == "price":
            print(f"Price: {self.price}")
        elif self.current == "publish_date":
            print(f"Publish date: {self.publish_date}")
        elif self.current == "description":
            print(f"Description: {self.description}")
        self.current = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # sax
    '''
    handler = BookHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse('example.xml')
    '''


    # dom
    domtree = xml.dom.minidom.parse('example.xml')
    group = domtree.documentElement
    books = group.getElementsByTagName('book')

    for book in books:
        print(f"-- Book {book.getAttribute('id')} --")

        author = book.getElementsByTagName('author')[0].childNodes[0].nodeValue
        title = book.getElementsByTagName('title')[0].childNodes[0].nodeValue
        genre = book.getElementsByTagName('genre')[0].childNodes[0].nodeValue
        price = book.getElementsByTagName('price')[0].childNodes[0].nodeValue
        publish_date = book.getElementsByTagName('publish_date')[0].childNodes[0].nodeValue
        description = book.getElementsByTagName('description')[0].childNodes[0].nodeValue

        print(f"Author: {author}")
        print(f"Title: {title}")
        print(f"Genre: {genre}")
        print(f"Price: {price}")
        print(f"Publish date: {publish_date}")
        print(f"Description: {description}")

    books[0].getElementsByTagName('author')[0].childNodes[0].nodeValue = "Changed name"
    books[0].getElementsByTagName('title')[0].childNodes[0].nodeValue = "Changed title"

    books[0].setAttribute("id", "bk99")

    '''
    new_book = domtree.createElement("book")
    new_book.setAttribute("id", "bk1000")

    author = domtree.createElement("author")
    author.appendChild(domtree.createTextNode("Adam Mickiewicz"))
    title = domtree.createElement("title")
    title.appendChild(domtree.createTextNode("Pan Tadeusz"))
    genre = domtree.createElement("genre")
    genre.appendChild(domtree.createTextNode("Epic poetry"))
    price = domtree.createElement("price")
    price.appendChild(domtree.createTextNode("12.7"))
    publish_date = domtree.createElement("publish_date")
    publish_date.appendChild(domtree.createTextNode("1834-06-28"))
    description = domtree.createElement("description")
    description.appendChild(domtree.createTextNode("Pan Tadeusz, or the last inn in Lithuania - an epic poem by Adam Mickiewicz published in two volumes"))

    new_book.appendChild(author)
    new_book.appendChild(title)
    new_book.appendChild(genre)
    new_book.appendChild(price)
    new_book.appendChild(publish_date)
    new_book.appendChild(description)
    group.appendChild(new_book)
    '''
    
    domtree.writexml(open('example_edited.xml', 'w+'))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
