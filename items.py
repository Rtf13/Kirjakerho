import db
def add_item(title, meeting, place, genre, book_type, description, user_id):
    sql = """INSERT INTO items (title, meeting, place, genre, book_type, description, user_id) VALUES (?, ?, ?, ?, ? ,? ,?)"""
    db.execute(sql, [title, meeting, place, genre, book_type, description, user_id])

def get_items():
    sql = "SELECT id, title FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.id,
                    items.title,
                    items.description,
                    items.meeting,
                    items.place,
                    items.book_type,
                    items.genre,
                    users.username,
                    users.id user_id

                FROM items, users
                WHERE items.user_id = users.id AND
                      items.id = ? """

    return db.query(sql,[item_id])[0]



def update_item(item_id, title, meeting, place, genre, book_type, description):
    sql = """UPDATE items SET title = ?,
                              description = ?,
                              meeting = ?,
                              place = ?,
                              book_type = ?,
                              genre = ?
                           WHERE id = ?"""
    db.execute(sql, [title, description, meeting, place, book_type, genre, item_id] )


def remove_item(item_id):
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])

def find_items(query):
    sql = """SELECT id, title
             FROM items
             WHERE title LIKE ? OR description LIKE ?
             OR genre LIKE ? OR place LIKE ?
             ORDER BY id DESC """
    like = "%" + query + "%"
    return db.query(sql, [like, like, like, like])