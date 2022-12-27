import os
os.environ.setdefault("DEFAULT_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from simplebank.models import User, Account

def initialize_database():
    user1 = User(username='bob', password='squarepants')
    user1.save()

    user2 = User(username='alice', password='redqueen')
    user2.save()

    account1 = Account(owner=user1, iban='345768134765')
    account1.save()

    account2 = Account(owner=user2, iban='987566013649')
    account2.save()

if __name__ == "__main__":
    initialize_database()
