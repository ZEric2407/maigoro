import sqlalchemy
import flask_sqlalchemy
import model

def save(instance):
    if not instance:
        return
    model.db.session.add(instance)
    model.db.session.commit()

def retrieve_all():
    transactions = model.db.session.query(model.TextTransaction).all()
    return transactions

if __name__ == "__main__":
    with model.app.app_context():
        for transaction in retrieve_all():
            print(transaction)