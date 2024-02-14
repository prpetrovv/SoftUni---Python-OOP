from hash_table import HashTable

table = HashTable()

table["name"] = "Petar"
table["age"] = 26

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))
