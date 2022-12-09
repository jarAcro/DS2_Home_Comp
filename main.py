# Chase Jarvis
# Student ID: 002312909

import csv
import datetime


# HashTable class using chaining.
class ChainingHashTable:

    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=40):
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


hash_table = ChainingHashTable()


class Package:
    def __init__(self, id, address, city, state, zip, delivery_status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_status = delivery_status

        self.timeDelivered = datetime.time(8, 0)
        self.timeLoaded = datetime.time(8, 0)

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (
            self.id, self.address, self.city, self.state, self.zip, self.delivery_status, self.timeLoaded,
            self.timeDelivered)


# Time complexity O(n)
def load_package_data(filename):
    with open(filename) as package:
        package_data = csv.reader(package, delimiter=',')
        for packages in package_data:
            pID = packages[0]
            pAddress = packages[1]
            pCity = packages[2]
            pState = packages[3]
            pZip = packages[4]
            pDelivery_status = packages[5]

            packages = Package(pID, pAddress, pCity, pState, pZip, pDelivery_status)
            hash_table.insert(packages)


# Time complexity O(n)
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
# Time complexity O(n^2)
def deliver(truck_list, truck_time):
    total_miles = 0.0
    while truck_list:
        min_so_far = 50.0  # the minimum distance at this point
        min_package = None  # initializing the minimum package to Nothing
        current_location = 0  # current location initialized to 0
        for id in truck_list:
            package = hash_table.search(
                id)  # iterating through hashtable, if the id is found the package is added to variable "package"
            address = package.address  # address of the package object
            index = distance_dict.get(
                address)  # assigns the index value of address from the distance dictionary to the "index" variable
            distance = distance_between(current_location,
                                        index)  # utilizes the "distance_between" function to check the distance between the current location and the next closes index
            if min_package is None:  # if minimum package is equal to nothing
                min_so_far = distance
                min_package = package  # minimum distance so far assigned to the distance
            elif distance < min_so_far:  # check if distance number is less than minimum distance
                min_so_far = distance  # the minimum distance is equal to the distance of "distance"
                total_miles = total_miles + float(distance)
                min_package = package  # min package is assigned to none at the beginning, here it is assigned to the package id

        time_to_location = datetime.timedelta(minutes=((float(min_so_far) * 60) / 18))
        truck_time = (datetime.datetime.combine(datetime.datetime.today(), truck_time) + time_to_location).time()
        min_package.timeDelivered = truck_time
        truck_list.remove(int(min_package.id))
    return round(total_miles, 2), truck_time


# Time complexity O(1)

def distance_between(loc1, loc2):
    if loc1 < loc2:
        return distances[loc2][loc1]
    else:
        return distances[loc1][loc2]


# time complexity O(n)
def user_interface():
    while True:
        print("****************************************")
        user_input = input(
            " User Interface:\n------------------------------\n For information on ALL packages, please enter 1.\n "
            "For information on ONE package, please enter 2.\n "
            "Enter 'done' to exit.\n ****************************************\n")

        if user_input == "done":
            print("Thank you, Take care now!")
            exit()

        if user_input == '1':

            user_hour = int(input("Please put in hours:\n"))
            user_min = int(input("Please put in minutes:\n"))

            user_time = datetime.datetime(2022, 8, 21, user_hour, user_min).time()
            print("ID,_____Package Address__________Delivery Deadline, Time Loaded,_Time delivered__Package Status")
            for packs in range(1, 41):
                p = hash_table.search(packs)
                if user_time < p.timeLoaded:
                    status = "The package is at the hub"
                elif user_time > p.timeDelivered:
                    status = 'The package has been Delivered'
                else:
                    status = 'The package is en route'

                print(p, packs, status)

        if user_input == '2':
            user_hour = int(input("Please put in hours:\n"))
            user_min = int(input("Please put in minutes:\n"))

            user_time = datetime.datetime(2022, 8, 21, user_hour, user_min).time()

            pack_id = int(input("Please give package ID\n"))
            p = hash_table.search(pack_id)

            if user_time < p.timeLoaded:
                status = "The package is at the hub."
            elif user_time > p.timeDelivered:
                status = 'The package has been Delivered.'
            else:
                status = 'The package is en route.'
            print(
                "ID,_____Package Address__________Delivery Deadline, ____Time Loaded,_Time delivered__Package Status_______All trucks distance")
            print(p, status)

        if user_input not in ['1', '2', 'done']:
            print("Invalid input, Please enter 1, 2, or 'done'.")
            user_interface()


# step 1 of the program flow is assigning the data structures and filling those data structure with the packages in the appropriate trucks.
distance_dict = {}
distances = []


# Truck assignments.
truck1_list = [14, 34, 22, 23, 29, 24, 26, 11, 12, 33, 17, 40, 30, 1, 21, 7]  # 16
truck2_list = [28, 32, 37, 10, 27, 8, 3, 13, 18, 19, 36, 6, 20, 16, 38, 15]  # 16
truck3_list = [31, 9, 35, 39, 2, 4, 5, 25]  # 8

# loading the data from the csv files.
load_package_data("WGUPSPackageFile.csv")
load_distance_data('WGUPSDistanceTable.csv')

# the calculation for time stamping the truck deliveries.
total_miles1, time1_finished = deliver(truck1_list, datetime.time(8, 0))
for p in truck2_list:
    package = hash_table.search(p)
    package.timeLoaded = datetime.time(9, 5)
total_miles2, time2_finished = deliver(truck2_list, datetime.time(9, 5))

for p in truck3_list:
    package = hash_table.search(p)
    package.timeLoaded = time1_finished

total_miles3, time3_finished = deliver(truck3_list, time1_finished)
all_miles = round(total_miles1 + total_miles2 + total_miles3, 2)
print('All miles traveled by all trucks: ', all_miles)
# the last step in the program is the user interface
user_interface()
