import secrets
import string

#TEST CASE INFORMATION
json1 = {
  "Entity": "Goverment",
  "name": "Bill",
  "category": "EV Insfracture",
  "quotes": [25000, 12000, 30000],
  "Size": 8,
}

entity = input("Position in Company or Goverment: ")
name2 = input("First and Last Name: ")
category2 = input("Project Category: ")
projectName2 = input("Project Name: ")

#TEST CASE INFORMATION
json1 = {
  "Entity": entity,
  "name": name2,
  "category": category2,
  "quotes": [25000, 12000, 30000],
  "Size": 8,
}


def smartContract(json1):
  verification_Code = ''.join((secrets.choice(string.ascii_letters) for i in range(json1["Size"]))).upper()
  return f"Your Validation Code is:  {verification_Code}"




if __name__ == '__main__':
  user1 = smartContract(json1)
  print(user1)