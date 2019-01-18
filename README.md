This REST API is made with python3.7 as well as  Flask the pre-requisits include Flask-RESTful, Flask-SQLAlchemy and Flask-JWT.

It  stores data on an sqlite database locally and to a more suited database  Postgresql online since this is the add-on extension I chose in Heroku.


To interact with my app deployed on Heroku  use postman or curl with the following url
https://simplestore-rest-api.herokuapp.com/ < place the designated endpoints here >

Step 1:
open postman or curl which ever you prefer

Step 2:
register a user using the above stated url with the endpoint /register
with the http verb POST
https://simplestore-rest-api.herokuapp.com/register

Step 3:
Authenticate the registered user  with the endpoint /auth
with the http verb POST
https://simplestore-rest-api.herokuapp.com/auth


Step 4:
create a store or stores  with the endpoint /store/<name>
with the http verb POST, where <name> represents whatever name you would like to call it 
each store is given an id in a sequence of 1,2,3,.... depending on when one is created that is to say 
the first store gets an id of 1

https://simplestore-rest-api.herokuapp.com/store/<name>


Step 5:
create an item  with the endpoint /item/<name>
with the http verb POST, specify the "price" and "store_id" in the body where store_id is the store id 
in which you want the item to be found.

https://simplestore-rest-api.herokuapp.com/item/<name>

Step 6:
retrieve a single created item  with the endpoint /item/<name>
with the http verb GET

https://simplestore-rest-api.herokuapp.com/item/<name>


Step 7:
retrieve all your created items with the endpoint /items
with the http verb GET

https://simplestore-rest-api.herokuapp.com/items


Step 8:
retrieve your created stores with the endpoint /stores
with the http verb GET, to see the created stores as well as the items stored wthin them

https://simplestore-rest-api.herokuapp.com/stores



items and stores can be deleted with the following endpoints respectively;

/item/<name>  that is to say https://simplestore-rest-api.herokuapp.com/item/<name>

/store/<name> that is to say https://simplestore-rest-api.herokuapp.com/store/<name>

 BUT with the http verb DELETE

