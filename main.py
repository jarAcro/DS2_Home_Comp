import csv
import datetime


# ARE MY DATA TYPES RIGHT???
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
    def insert(self, package):
        # get the bucket list where this item will go.
        bucket = int(package.id) % 10
        bucket_list = self.table[bucket]

        bucket_list.append(package)  # insert the item to the end of the bucket list.
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = int(key) % 10
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for package in bucket_list:
            if package.id == str(key):
                return package
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


hash_table = ChainingHashTable()


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
            hash_table.insert(packages)


def load_distance_data(filename):
    with open(filename) as file:
        distance_data = csv.reader(file, delimiter=",")
        count = 0
        for distance in distance_data:
            distance_dict[distance[0]] = count
            count += 1
            distance.pop(0)
            distances.append(distance)


# use nearest neighbor greedy algo
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
        time_to_location = datetime.timedelta(minutes=((float(min_so_far) * 60) / 18))
        truck_time = (datetime.datetime.combine(datetime.datetime.today(), truck_time) + time_to_location).time()

        truck_list.pop()


def distance_between(loc1, loc2):
    if loc1 < loc2:
        return distances[loc2][loc1]
    else:
        return distances[loc1][loc2]


truck1_list = [2, 4, 14, 19, 16, 13, 15, 5, 7, 8, 9, 10, 11, 12, 17, 18]  # 16
truck2_list = [1, 3, 6, 25, 28, 32, 36, 38, 29, 30, 31, 34, 37, 40, 20, 21]  # 16
truck3_list = [22, 23, 24, 26, 27, 33, 35, 39]  # 8

load_package_data("WGUPSPackageFile.csv")

# print(hash_table.table)
distance_dict = {}
distances = []
load_distance_data('WGUPSDistanceTable.csv')
# print(distances)
deliver(truck1_list, datetime.time(8, 0))
print()
