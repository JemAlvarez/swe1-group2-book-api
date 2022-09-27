# Project Docs

## Pull Reuquests
1. All pull request must have a tag with the feature you're working on
2. All pull requests will be reviewed by one other person before being merged to develop

## Generating secret key
1. Navigate to the project directory in the command line
2. Create a new file in the project director called `.env`, in the file write `SECRET_KEY=your_key`
3. In command line run `python manage.py shell`
4. In command line run `from django.core.management import utils`
5. In command line run `print(utils.get_random_secret_key())`
6. Copy the printed key
7. In the `.env` file paste the key you copied from the command line instead of `your_key`

----
## Features Usage
> Feature 1 Docs
* Retrieve List of Books by Genre `/books?genre=parameter` `(GET)`
* Retrieve List of Top Sellers (This will retrieve top 10 books by default in descending order) `/books?top=` `(GET)`
    * Retrieve List of Top X Sellers (Retrieve an specific quantity in descending order) `/books?top=quantity` `(GET)`
* Retrieve List of Books for a particular rating and higher (In descending rating order) `/books?min_rating=parameter` `(GET)`
* Retrieve List of X books at a time from Y position in the recordset `/books?retrieve=X&startpos=Y` `(GET)`
    * If no startpos value if used, it will retrieve X books starting from recordset position 1

> Feature 4 Docs
* Get author's books `/author/Author+Name/books` `(GET)`
* Get book by ISBN `/books/:BOOK_ISBN` `(GET)`
* Create book `books/` `(POST)`
    * Needs authentication test admin account `administrator:password`
        * In postman go to `Authorization>Type>Basic Authorization>Put the above info here`
    * Needs body with json data for the book fields
* Create author `author/` `(POST)`
    * Needs authentication test admin account `administrator:password`
        * In postman go to `Authorization>Type>Basic Authorization>Put the above info here`
    * Needs body with json data for the book fields