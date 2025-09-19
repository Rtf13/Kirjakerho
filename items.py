import db
def add_item(title, meeting, place, genre, book_type, description, user_id):
    sql = """INSERT INTO items (title, meeting, place, genre, book_type, description, user_id) VALUES (?, ?, ?, ?, ? ,? ,?)"""
    db.execute(sql, [title, meeting, place, genre, book_type, description, user_id])
