# PYTHON MongoDB 
Python can be used in database applications
One of the most popular NoSQL database is MongoDB.

## MongoDB
    MongoDB stores data in JSON-like documents, which makes the database very flexible and scalable
#### Prerequisites
* You can download a free MongoDB database at [MongoDB Website](https://www.mongodb.com/ "MongoDB Website")
* Or get started right away with a MongoDB cloud service at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/ "MongoDB Atlas") 
\\- From the CLi you can insert the following `pip install pymongo`

### Test PyMongo
- To test if the installation was successful, or if you already have "pymongo" installed, create a Python page with the following content: 
- From the example:-  `demo_mongodb_test.py` is executed with no errors, "pymongo" is installed and ready to be used.

# PYTHON MongoDB Create Database (Folder)
### Creating a Database
- To create a database in MongoDB, start by creating a MongoClient object, then specify a connection URL with the corrected ip address and the name of the database you want to create.
MongoDB will create the database if it doesn't exist, and make a connection to it.
  * Note: In MongoDB, a database is not created until it gets content
- MongoDB waits until you have created a collection (table), with at least one document (record) before it actually, creates the database (and collection)

### Check if Database Exists
* Remainder: In MongoDB, a database is not created until it gets content, so if it's you first-time creating a DB, you should complete the next two chapters, i.e (create collection and create document) before you check if the DB exists.


# PYTHON MongoDB Create Collection (Folder)
* A `collection` in MongoDB is the same as a table in `SQL` databases

## Create A Collection
- To create a collection in MongoDB, use the database object and specify the name of the collection you will create.
- MongoDB will create the collection if it doesn't exist.
Example:- `create_customers_collection.py`

*   *Important: In MongoDB, a collection is not created until it gets content!*

- MongoDB waits until you have inserted a document before it actually creates the collection.

## Check if Collection Exists
* Remember: In MongoDB, a collection is not created until it gets content, so if this is your first time creating a collection, you should complete the next chapter (create document) before you check if the collection exists!
- To check if a collection exists in a database by listing all collections: Example=> `print(mydb.list_collection_names())`


# PYTHON MongoDB Insert Document (Folder)
* A `document` in MongoDB is the same as a `record` in SQL databases.

## Insert Into Collection
- To insert a record, or document as it is called in MongoDB, into a collection, we use the `insert_one()` method.
- The first parameter of the `insert_one()` method is a dictionary containing the name(s), and value(s) of each field in the document you want to insert.
Example:- `insert_method_collection.py`

## Return the `_id` Field
- The `insert_one()` method returns a InsertOneResult object, which has a property, `insert_id`, that holds the id of the inserted document.
Example:- `mongo_insert_id.py`
- In the example above, no `_id` field was specified, so MongoDB assigned a unique_id for the record (document)
* If you don't specify an `_id` field, then MongoDB will add one for you and assign an unique id for each document

## Insert Multiple Documents
- To insert multiple docs into a collection in MongoDB, we use the `insert_many()` method.
- The first parameter of the `insert_many()` method is a list containing dictionaries with the data you want to insert:
Example: `mongo_insert_many.py`

## Insert Multiple Documents, with specified IDs
- If you do not want MongoDB to assign unique IDs for your doc, you can specify the _id field when you insert the document(s).
- Remember that the values has to be unique. Two documents cannot have the same _id.
Example:- `mongo_insert_ids.py`


# PYTHON MongoDB Find (Folder)
- In MongoDB, we use the `find` and `findOne` methods to find data in a collection
- Just like the `SELECT` statement is used to find data in a table in a MySQL database.

## `Find One`
- To select data from a collection in MongoDB, we can use the `find_one()` method.
- The `find_one()` method returns the first occurrence in the selection.
Example:- `mongo_find_one.py`

## `Find All`
- To select data from a table in MongoDB, we can also use the `find()` method, which returns all occurrences in the selection.
The first parameter of the `find()` method is a query object. 
- In the Example, we use an empty query object, which selects all documents in the collection.
*No parameters in the `find()` method gives you the same result as `SELECT *` in MySQL.* 
Example:- `mongo_find_all.py`

### Return Only Some Fields
- The second parameter of the `find()` method is an object describing which fields to include in the result.
- This parameter is optional, and if omitted, all fields will be included in the result.
Example: `mongo_find_some_fields.py`

- Specifying both 1 and 0 values in the same object is NOT allowed (except if one the fields is the _id field.) 
If you specify a field with the value 0, all other fields get the value 1, and vice-versa:
* Example:- `mongo_exclude_address.py` --> This will exclude "address" from the result
* Example:- `mongo_error_diff_fields.py` --> This will give an error if two different values are specified.


# PYTHON MongoDB Query (Folder)
### Filter The Result
- When finding docs in a collection, you can filter the result by using a query object.
- The first argument of the `find()` method is a query object, and is used to limit the search
Example:- `mongo_filter_query_find.py`

### Advanced Query
- To make advanced queries you can use modifiers as values in the query object.
E.g. to find the documents where the "address" field starts with the letter "S" or higher (alphabetical), use the greater than modifier: `{"$gt": "S"}`
Example:- `mongo_advanced_filter.py`

### Filter With Regular Expressions
- You can also use regular expressions as a modifier.
* Regular Expressions can be used to query strings.

- To find only the documents where the "address" field starts with letter "S", use the regular expression `{"$regex": "^S"}`:
Example:- `mongo_filter_with_regExp.py`

# PYTHON MongoDB Sort (folder)
#### Sort the Result (Ascending)
- Use the `sort()` method to sort the result in ascending or descending order. 
- The method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction).
Example:- `mongo_sort_result_ascending-default.py`

#### Sort Descending
Use the value -1 as the second parameter to sort descending.

*   `sort(*name*, 1)` #ascending
*   `sort(*name*, -1)` #descending
Example:- `mongo_sort_result_descending.py`

# PYTHON MongoDB Delete Document (Folder)
### Delete Document
- To delete one document, we use the `delete_one` method.
- The first parameter of the `delete_one()` method is a query object defining which document to delete.

* NOTE: If the query finds more than one document, only the first occurrence is deleted.
Example: `mongo_delete_document.py`

#### Delete Many Documents
To delete more than one document, `delete_many()` method is used.
- The first parameter of the `delete_many()` method is a query object defining which documents to delete.
Example:- `mongo_delete_many().py` *Delete all documents were the address starts with the letter S*

#### Delete All Documents in a Collection
- To delete all documents in a collection, pass an empty query object to the `delete_many()` method.
Example:- `mongo_delete_all_docs.py` *Delete all document in the "customers" collection*


# PYHTON MongoDB Drop Collection (Folder)
#### Delete Collection
You can delete a table, or collection as it is called in MongoDB, by using the `drop()` method.
Example:- `mongo_drop_collection.py`


# PYTHON MongoDB Update (Folder)
### Update Collection
You can update a record, or document as it is called in MonogDB, by using the `update_one()` method.
- The first parameter of the `update_one()` method is a query object defining which document to update.
*Note: If the query find more than one record, only the first occurrence is updated.*
- The second parameter is an object defining the new values of the document.
Example:- `mongo_update_one().py` *Change the address from "Valley 345" to "Canyon 123"*

### Update Many
- To update all documents that meets the criteria of the query, use the `update_many()` method.
Example:- `mongo_update_many.py` *Update all document where the address starts with the letter "S"*


# PYTHON MongoDB Limit (Folder)
#### Limit the result
To limit the result in MongoDB, we use the `limit()` method.
The `limit()` method takes one parameter, a number defining how many documents to return
Consider you have a "customers" collection:

	### Customers
	`
	{'_id': 1, 'name': 'John', 'address': 'Highway37'}
	{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
	{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
	{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
	{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
	{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
	{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
	{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
	{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
	{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
	{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
	{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
	{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
	{'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}
	`
Example:- `mongo_limit.py` *Limit the result to only return 5 documents*