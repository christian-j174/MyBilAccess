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

def smartContract(json1):
  verification_Code = ''.join((secrets.choice(string.ascii_letters) for i in range(json1["Size"]))).upper()
  return f"Your Validation Code is:  {verification_Code}"


# print(code1)

if __name__ == '__main__':
  user1 = smartContract(json1)
  print(user1)