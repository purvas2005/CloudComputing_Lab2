from database import get_db

def checkout_logic():
    db = get_db()
    db.row_factory = None  

    # Compute total fee directly in SQL for efficiency
    row = db.execute("SELECT SUM(fee) FROM events").fetchone()
    total = row[0] or 0

    return total
