# Project Docs

## Pull Reuquests
1. All pull request must have a tag with the feature you're working on
2. All pull requests will be reviewed by one other person before being merged to develop

## Generating secret key
1. Navigate to the project directory in the command line
2. `python manage.py shell`
3. `from django.core.management import utils`
4. `print(utils.get_random_secret_key())`
5. Copy the printed key
6. Create a new file in the project director called `.env`
7. In the file write `SECRET_KEY=your_key` paste the key you copied from the command line instead of `your_key`

----
> Feature 4 Docs
* Get author's books `/author/Author+Name/books`
* Get book by ISBN `/books/:BOOK_ISBN`