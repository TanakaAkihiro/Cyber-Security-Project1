from simplebank.models import User

def initialize_database():
    user = User(username='bob', password='squarepants')
    user.save()

    user = User(username='alice', password='redqueen')
    user.save()

if __name__ == "__main__":
    initialize_database()
