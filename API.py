import requests

uri = "https://ec.europa.eu/esco/api/search?language=en&type=skill&text="
keyword = input("Enter Job Title: ")
keyword.replace(" ", "+")

response = requests.get(uri + keyword)

if response.status_code == 200:
    try:
        global data
        data = response.json()
    except ValueError:
        print(response.text)
else:
    print('Error:', response.status_code)

titles = [result['title'] for result in data['_embedded']['results']]

#Print Skills (The JSON result has skill in the value of key named "title")
for skill in titles:
    print(skill)