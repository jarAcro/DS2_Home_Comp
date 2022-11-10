import csv


# HashMap
# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=39):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    def insert(self, key, item):
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True
        # insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for key_value in bucket_list:
            if str(key_value[0]) == key:
                return key_value[1]
            return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])


class Package:
    def __init__(self, id, address, city, state, zipCode, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s, &s" % (self.id, self.address, self.city, self.state, self.zipCode, self.status)


def load_package_data(filename):
    with open(filename) as package:
        package_data = csv.reader(package, delimiter=',')
        next(package_data)  # skips the header
        for packages in package_data:
            pID = packages[0]
            pAddress = packages[1]
            pCity = packages[2]
            pState = packages[3]
            pZip = packages[4]
            deliverStatus = "Delivered"
            packages = Package(pID, pAddress, pCity, pState, pZip, deliverStatus)
            hash_table.insert(pID, packages)


# Greedy Algorithm
# def greedy_algo:


hash_table = ChainingHashTable()
load_package_data("WGUPSPackageFile.csv")

for i in range(len(hash_table.table) + 1):
    print('Packages: {} and address: {}'.format(i + 1, hash_table.search(i + 1)))
