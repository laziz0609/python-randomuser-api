import requests
import json


def get_randomuser_full_data() -> dict:
    url = 'https://randomuser.me/api/'

    response = requests.get(url)
    data = response.json()

    return data['results'][0]


def check_gender(user: dict) -> bool:
    if user["gender"].lower() == "male":
        return True
    
    return False


def get_user_data(user: dict) -> dict[str, str]:
    full_name = user['name']['first'] + ' ' + user['name']['last']
    phone = user['phone']
    email = user['email']
    age = user['dob']['age']
    nat = user['nat']
    gender = user['gender']
    country = user['location']['country']


    data = {
        "full_name": full_name,
        "phone": phone,
        "email": email,
        "age": age,
        "nat": nat,
        "gender": gender,
        "country": country
    }
    return data


def main() -> None:
    males: list[dict[str, str | int]] = []
    females: list[dict[str, str | int]] = []
    while len(males) < 10 or len(females) < 10:
            
            print(i)
            user_data = get_randomuser_full_data()
            if check_gender(user_data):
                if len(males) < 10:
                    males.append(get_user_data(user_data))
            
            else:
                if len(females) < 10:
                    females.append(get_user_data(user_data))

    users = {"males": males, "females": females}
    
    with open('users.json', 'w') as jsonfile:
        jsonfile.write(json.dumps(users, indent=4))


main()
