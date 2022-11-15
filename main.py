import csv
import datetime


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
    def __init__(self, id, address):
        self.id = id
        self.address = address
        self.timeDelivered = datetime.time(8, 0)
        self.timeLoaded = datetime.time(8, 0)

    def __str__(self):
        return "%s, %s" % (self.id, self.address)

    def __repr__(self):
        return "%s, %s" % (self.id, self.address)


def load_package_data(filename):
    with open(filename) as package:
        package_data = csv.reader(package, delimiter=',')
        for packages in package_data:
            pID = packages[0]
            pAddress = packages[1]

            packages = Package(pID, pAddress)
            hash_table.insert(pID, packages)


def load_distance_data(filename):
    with open(filename) as file:
        distance_data = csv.reader(file, delimiter=",")
        count = 0
        for distance in distance_data:
            distance_dict[distance[0]] = count
            count += 1
            distance.pop(0)
            distances.append(distance)


def deliver(truck_list, truck_time):
    while truck_list:
        min_so_far = 50
        min_package = None
        current_location = 0
        for id in truck_list:
            package = hash_table.search(id)
            address = package.address
            index = distance_dict[address]
            distance = distance_between(current_location, index)
            if min_package is None:
                min_package = package
                min_so_far = distance
            else:
                if distance < min_so_far:
                    min_so_far = distance
                    min_package = package

        # time = distance/speed

        time_to_location = datetime.timedelta(minutes=((float(min_so_far) * 60) / 18))  #
        truck_time = (datetime.datetime.combine(datetime.datetime.today(), truck_time) + time_to_location).time()
        print(truck_time)
        truck_list.pop(int(id))


def distance_between(loc1, loc2):
    if loc1 < loc2:
        return distances[loc2][loc1]
    else:
        return distances[loc1][loc2]


# use nearest neighbor

truck1_list = ['1', '2']
truck2_list = [3]
truck3_list = []

# Greedy Algorithm
# def greedy_algo:

hash_table = ChainingHashTable()
load_package_data("WGUPSPackageFile.csv")

# print(hash_table.table)
distance_dict = {}
distances = []
load_distance_data('WGUPSDistanceTable.csv')
# print(distances)
deliver(truck1_list, datetime.time(8, 0))
