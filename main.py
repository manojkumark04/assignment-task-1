import pymongo as py

myclient = py.MongoClient("mongodb://127.0.0.1:27017/")
db = myclient["guvicrudtask"]
mycollection = db["crudcollection"]

"""1.Creating a collection"""

directory = [{
    "Name": "Stwie",
    "Phone_number": "9465194691",
    "Place": "Mumbai"},
{
    "Name": "Peter",
    "Phone_number": "9846469845",
    "Place": "chennai"},
{
    "Name": "Chris",
    "Phone_number": "8514984626",
    "Place": "Qhaque"},
{
    "Name": "Joe",
    "Phone_number": "9978956464",
    "Place": "Pune"},
{
    "Name": "Brian",
    "Phone_number": "9865194691",
    "Place": "Nagpur"},
]

# tele = mycollection.insert_many(directory)

"""2.Inserting into a collection"""

file_6 = {
    "Name": "Jerome",
    "Phone_number": "9589245155",
    "Place": "Delhi"}

# file = mycollection.insert_one(file_6)

"""2.Retrieving collection"""

peter = mycollection.find_one({"Name":"Peter"})
# print(peter)

record = mycollection.find({})
# for family in record:
#     print(family)

"""4.Updating a collection"""

query = {"Phone_number":"9465194691"}
newnum = {"$set":{"Phone_number":"9888898881"}}

# ewcard = mycollection.update_one(query,newnum)
#
# print(ewcard)

"""5.Deleting a collection"""

# delall = mycollection.delete_many({})

# delchris = mycollection.delete_one({"Name": "Chris"})

# print(delchris)
# print(delall)





