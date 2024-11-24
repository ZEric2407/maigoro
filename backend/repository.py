from model import *

def save(instance):
    if not instance:
        return
    db.session.add(instance)
    db.session.commit()

def save_all(instances):
    if not instances:
        return
    db.session.add_all(instances)
    db.session.commit()

def retrieve_all(is_landmark):
    cls = LandmarkTransaction if is_landmark else TextTransaction
    transactions = db.session.query(cls).all()
    return transactions

if __name__ == "__main__":
    from model import app
    with app.app_context():
        for transaction in retrieve_all(True):
            print(transaction)