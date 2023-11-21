import json
import requests
import pandas

base_url = "http://localhost:3002/people"

headers = {
    'Content-Type': 'application/json'
}

test_data = 'test_data.json'
test_data_2 = 'test_data_2.json'

#Task 1: Create a file in your directory containing valid JSON data for your server, import it, and send it to the API using a POST request.
def import_and_send_data(file_name):
    json_file = open(file_name)
    data = json.load(json_file)

    people_response = requests.post(base_url, json=data, headers=headers)
    return people_response

task_1 = import_and_send_data(test_data)
print("Task 1 Response: ", task_1.json())


#Task 2: Send a get request to your API and filter the data until you find the data you posted
def get_and_filter_data_by_id(id):
    get_response = requests.get(base_url)
    all_people = get_response.json()

    filtered_people = [person for person in all_people if person['id'] == id]
    return filtered_people

task_2 = get_and_filter_data_by_id('21')
print("Task 2 Response: ", task_2)


#Task 3: Update the data using a PATCH and PUT request
def update_data_with_patch(id, update_data):
    update_url = f"{base_url}/{id}"
    patch_response = requests.patch(update_url, json=update_data)
    return patch_response

def update_data_with_put(id, update_data):
    update_url = f"{base_url}/{id}"
    put_response = requests.put(update_url, json=update_data)
    return put_response

patch_update_data = {"fullName": "Test PATCH"}

put_update_data = {
    "id": "21",
    "fullName": "Test PUT",
    "email": "test1@example.com",
    "job": "Cowboy",
    "dob": "01/01/2023"   
}

task_3_patch = update_data_with_patch(21, patch_update_data)
print("Task 3 Response: ", task_3_patch.json())

task_3_put = update_data_with_put(21, put_update_data)
print("Task 3 Response: ", task_3_put.json())


#Task 4: Remove the data using a DELETE request
def remove_data(id):
    delete_url = f"{base_url}/{id}"
    delete_response = requests.delete(delete_url)
    return delete_response

task_4 = remove_data('21')
print("Task 4 Response: ", task_4)


#Task 6: When importing the data, add some validation to ensure the data is structured how you would expect. Correct data types, etc.
def validate_data(data):
    for person in data:
        for key in ["fullName", "email", "job", "dob"]:
            if key not in person:
                print(f"Invalid data structure. Missing key: {key}")

            expected_type = str
            if not isinstance(person[key], expected_type):
                print(f"Invalid data type for key {key}. Expected {expected_type}, got {type(person[key])}")


#Task 5: Create a json file with various example of people data, within the data create several duplicates, import this data, remove duplicates and POST to the API
def import_remove_duplicates_and_send_data(file_name):
    json_file = open(file_name)
    data = json.load(json_file)

    validate_data(data) #Task 6

    for person_data in data:
        unique_data = dict(person_data)
        requests.post(base_url, json=unique_data, headers=headers)
    
    return "Data sent successfully"

task_5 = import_remove_duplicates_and_send_data(test_data_2)
print("Task 5 Response: ", task_5)
