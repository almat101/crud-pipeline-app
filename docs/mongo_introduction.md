# **An Introduction to MongoDB**

### **What is a NoSQL Database?**

A **NoSQL database** (which stands for "not only SQL") is a type of database that doesn't use the traditional table-based relational model. Instead of organizing data into rows and columns, NoSQL databases offer more flexible data models. This makes them great for handling large volumes of unstructured or semi-structured data, which is common in modern web applications.

Think of it like this: A traditional SQL database is like a spreadsheet, with a fixed number of columns for every row. A NoSQL database, specifically a document database like MongoDB, is more like a filing cabinet filled with folders. Each folder (a **document**) can hold different types of information and is not restricted to a rigid structure.

In MongoDB, the two main components are:

* **Document**: This is the basic unit of data. It is a set of key-value pairs, similar to a JSON object. For example, a single product record would be a document.  
* **Collection**: This is a group of documents. It's the equivalent of a table in a relational database. All documents in a collection are related, but they don't have to have the exact same structure.


In MongoDB, collections and documents serve different purposes, and the choice to use a collection is appropriate in this case. Here's why:

- What is a Collection?
   - A collection in MongoDB is analogous to a table in a relational database.
   It is a container for storing multiple documents (records).
   Collections group related data together, making it easier to query and manage.
- What is a Document?
   - A document in MongoDB is a single record stored in a collection.
   It is a JSON-like object (BSON) that contains key-value pairs.
   Each document is independent and can have a flexible schema.
Why Use a Collection in This Case?
1. Storing Multiple Products:
   - Your scraper retrieves multiple products, each represented as a dictionary (document).
   A collection (raw_products) is the appropriate container to store all these product documents together.
2. Logical Grouping:
   - All the scraped product data belongs to the same category (e.g., "raw products").
   Storing them in a single collection makes it easier to query, update, or delete related data.
   Scalability:
   - Collections are designed to hold many documents, making them ideal for storing large datasets like product listings.
   Querying:
   - Using a collection allows you to query all products or filter specific ones (e.g., by title, price, or city) efficiently.
   Why Not Use a Single Document?
3. Limited Use Case:
   - A single document would only make sense if you were storing a single product or a small, fixed dataset.
   In your case, each product is independent, and storing them as separate documents in a collection is more appropriate.
4. Querying Challenges:
   - If all products were stored in a single document (e.g., as an array), querying individual products would be more complex and less efficient.
5. Scalability Issues:
   - MongoDB has a document size limit of 16 MB. If you store all products in a single document, you could quickly hit this limit as the dataset grows.
6. Conclusion
   - Using a collection (raw_products) to store multiple documents (individual products) is the correct and scalable approach for your use case. It aligns with MongoDB's design philosophy and makes querying, updating, and managing the data much easier.

### **Basic Commands for Your Database**

First we have to create the docker-compose.yml service for mongodb:
```yml
  mongodb:
    image: mongo
    container_name: mongodb
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db
```

1. Into the scraper code we have to add this import and this code at the beginning of the code(not in /scrape endpoint):
   ```python
      from pymongo import MongoClient


      #### MONGO DB connection creation ####
      client = MongoClient("mongodb://localhost:27017/")
      db = client["products_db"]
      collection = db["raw_products"]
   ```
   This code is creating a client that connects to your local mongodb server(which is running in docker using the docker-compose).
   Then is creating(or select if it exist) the database.
   Finally is creating (or selcect) the collection.

2. After the scrape of the products is ended, you can use this code to insert the raw_data into the collection of mongodb:

```python
   try:
      collection.insert_many(raw_data)
      return {"message": "Scrape success and data saved.", "result": raw_data}
   except Exception as e:
      logger.error(f"Error saving data to mongodb: {e}")
      return {f"message": "error saving data to mongodb", "error" : str(e)}
```
`insert_many` is used when you want to add several documents to MongoDB in a single operation, making it efficient for bulk inserts. It only accepts a list of dictionaries, not a single dictionary or a dictionary of elements or a list ecc.

**RECAP(List vs Dictionary in Python)**:

- List:

   Is an ordered collection of elements.
   Each element can be any type (number, string, dictionary, etc.).
   Elements are accessed by their index (position).
   Example:

   ```python
   my_list = [1, 2, 3]
   products_list = [{"name": "Laptop", "price": 1000},{"name": "Monitor", "price": 200}]
   ```
   In the context of MongoDB, you use a list of dictionaries to represent multiple documents.
- Dictionary:

   Is an unordered collection of key-value pairs.
   Each key is unique and maps to a value.
   Example:

   my_dict = {"name": "Laptop", "price": 1000}
   In MongoDB, a dictionary represents a single document.

- Why Not the Same?
   - A list is like a row of boxes, each box can hold anything (including dictionaries).
   A dictionary is like a single box with named compartments (keys).

- For MongoDB’s insert_many:
   - You must provide a list of dictionaries (each dictionary is a document).
   You cannot provide a single dictionary, because that would be just one document, not many.



You would use the following commands in the mongosh shell to interact with them.
3. Connect to your database:  
   First, open mongosh and use the following command to switch to your database.  
   ```sh
   use products_db
   ```
   You can confirm you're in the correct database by typing db and pressing Enter.  
2. View collections: 
   To see the raw_products collection you've already created, use this command.  
   ```sh
   show collections
   ```

3. Show all elements:
   ```sh
   db.raw_products.find()
   ```

4. Count all elements:
   ```sh
   db.raw_products.countDocuments()
   ```

5. Insert data:  
   You can insert new documents into your raw_products collection.  
   ```sh
   db.raw_products.insertOne({  
       productName: "Laptop",  
       brand: "Lenovo",  
       price: 275  
   })
   ```
6. Find data:  
   To find and view all documents in your collection, use a find query with an empty filter.  
   
   ```sh
   db.raw_products.find()
   ```

   To find a specific document, you can provide a filter.  
   ```sh
   db.raw_products.find({ brand: "Lenovo" })
   ```
7. Update data:  
   To update a document, you can use updateOne with a filter and a $set operator.  
   ```sh
   db.raw_products.updateOne( 
       { productName: "Laptop" },  
       { $set: { price: 300 } }  
   )
   ```
8. Delete data:  
   To remove a single document that matches your filter.  
   ```sh
   db.raw_products.deleteOne({ brand: "Lenovo" })  
   ```


## mongo ObjectID

The ObjectId in MongoDB serves a similar purpose to the auto-incrementing integer id that PostgreSQL (and other SQL databases) assigns to new rows in a table:

- MongoDB ObjectId:

  - Automatically generated for each new document if you don't provide an _id.
  - Uniquely identifies each document in a collection.
  - Is a 12-byte hexadecimal value (not an integer).

- PostgreSQL id:

  - Typically an integer, often set to auto-increment.
  - Uniquely identifies each row in a table.

Summary:
Both are unique identifiers for records, but ObjectId is a special type (not just an integer) and is generated differently. Their purpose—uniquely identifying each record—is the same.