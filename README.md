# exercise
The file consists of create, read, change, delete functions.

create function:-
it creates a new key pair and stores in db
An appropriate error("error-key already exists") will return, if create function is invoked for an existing key.
The key is always less than or equal to 32character.
An error("error-value should be less than 32characters") will throw if key exceeds 32char

read function:-
it read the value using a key
error message:"error-key not exist..Enter a valid key"

delete function:-
it can be performed by providing the key(it removes key pair from db).

change function:-
it updates a new key pair in db.
