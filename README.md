# contact-book-sqlite

A command-line contact book backed by an SQLite database.

## Features

- Add, search, list and delete contacts
- Case-insensitive search that ignores extra spaces
- The database itself rejects duplicate names
- Logic separated from the menu and covered by pytest tests (using an in-memory database)

## Setup

```
python contacts_db.py
```

This creates `contacts.db` with the `contacts` table.

## Run

```
python contact_book_db.py
```

## Run the tests

```
pip install pytest
python -m pytest test_contacts_lib.py
```

## Author

Victor Amuta
