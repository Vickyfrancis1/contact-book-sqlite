import sqlite3
from contacts_lib import find_contact
from contacts_lib import add_contact
from contacts_lib import delete_contact

def make_test_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE contacts (id INTEGER PRIMARY KEY, name TEXT UNIQUE, phone TEXT)")
    conn.execute("INSERT INTO contacts (name, phone) VALUES ('Vick', '0801')")
    conn.commit()
    return conn

def test_finds_existing_case_insensitive():
    conn = make_test_db()
    assert find_contact(conn, " vick ") == ("Vick", "0801")
    
def test_missing_returns_none():
    conn = make_test_db()
    assert find_contact(conn, "Ngozi") is None
    
def test_add_new():
    conn = make_test_db()
    assert add_contact(conn, "leo", "0802") is True
    assert find_contact(conn, "Leo") == ("Leo", "0802")
    
def test_add_duplicate_rejected():
    conn = make_test_db()
    assert add_contact(conn, "VICK", "0999") is False
    
def test_delete_existing():
    conn = make_test_db()
    assert delete_contact(conn, "vick") is True
    assert find_contact(conn, "Vick") is None
    
def test_delete_missing():
    conn = make_test_db()
    assert delete_contact(conn, "Ngozi") is False