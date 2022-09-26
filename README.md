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
> Feature 4 Docs
* Get author's books `/author/Author+Name/books`
* Get book by ISBN `/books/:BOOK_ISBN`