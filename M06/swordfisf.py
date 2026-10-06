"""
This script prompts the user for their name and password.
If the name is not 'Joe', it continues to prompt for the name.
If the name is 'Joe', it asks for the password.
If the password is 'swordfish', it grants access.

while True:
    print('Who are you?')
    name = input('>')
  ❶ if name != 'Joe':
      ❷ continue
    print('Hello, Joe. What is the password? (It is a fish.)')
  ❸ password = input('>')
    if password == 'swordfish':
        ❹ break
❺ print('Access granted.')
"""
while True:
    print('Who are you?')
    name = input('>')
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input('>')
    if password == 'swordfish':
        break

print('Access granted.')