import unittest
import requests

class ApiTest(unittest.TestCase):

	def test_addUserProfile(self):
		url = "http://127.0.0.1:8000/api/v1/users"

		payload = "{\n\t\"name\": \"Nazmul Hasan23\",\n\t\"password\": \"aA1!aA1!\",\n\t\"mobileNumber\": \"01676807169\",\n\t\"balance\": 0\n}"
		headers = {
			'Content-Type': "application/json",
			'cache-control': "no-cache",
			}

		response = requests.request("POST", url, data=payload, headers=headers)

		print(response.text)
	
	def test_getTransactions(self):
		url = "http://127.0.0.1:8000/api/v1/users/b14fb71a-06e9-433a-a825-37089c2d8431/transactions" #pass userUUid from profile table

		payload = ""
		headers = {
			'Authorization': "Token 8c69c64a3a4a39f0b5268321ff57439c6d5ea0a6",  #pass user token
			'cache-control': "no-cache",
			}

		response = requests.request("GET", url, data=payload, headers=headers)

		print(response.text)

	def test_transaction(self):
		url = "http://127.0.0.1:8000/api/v1/users/e423c480-6e08-4f6e-8622-bbb85daf07a6/transactions" #pass userUUid from profile table
		#pass different userUUID as receiver id 
		payload = "[\n\t{\n\t\t\"recieverId\": \"b9899b63-4510-4ee6-af52-f56f58af3f0f\",\n\t\t\"amount\": 100\n\t},\n\t{\n\t\t\"recieverId\": \"9e4b2b16-cee7-44b3-a456-6279a00ff698\",\n\t\t\"amount\": 100\n\t}\n]"
		headers = {
			'Authorization': "Token eb762b21bef6204ea0d2ab66245852823cbc14f0",  #passs requested user token from token table
			'Content-Type': "application/json",
			'cache-control': "no-cache",
			}

		response = requests.request("POST", url, data=payload, headers=headers)

		print(response.text)

	def test_addScheduleTransactionUser(self):
		url = "http://127.0.0.1:8000/api/v1/users/b14fb71a-06e9-433a-a825-37089c2d8431/schedulers" #pass userUUid from profile table

		payload = "{\n\t\"recieverId\": \"26a933b5-fd92-4bfd-80df-0f2f93044ee2\",\n\t\"amount\": \"100\"\n}" #pass schedule transaction receiver id
		headers = {
			'Authorization': "Token 8c69c64a3a4a39f0b5268321ff57439c6d5ea0a6", #pass requested user tokens from token table
			'Content-Type': "application/json",
			'cache-control': "no-cache",
			}

		response = requests.request("POST", url, data=payload, headers=headers)

		print(response.text)


if __name__ == 'main':
	unittest.main()