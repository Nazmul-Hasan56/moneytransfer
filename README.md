Install python virtual env by following commands:
    1. sudo apt install python3(3.8 or 3.7+)
    2. sudo apt install python3-pip
    3. pip install virtualenv
    4. python3 -m virtualenv Env

Active virtual Env && run project:
    1. source Env/bin/activate
    2. go to the directory moneytransfer/moneytransferplatform
    3. make migrations using (python3 manage.py makemigrations)
    4. migrate using (python3 manage.py migrate)
    5. after than install django rest framework, requests and django cron tab
    6. add cron tab using (python3 manage.py crontab add)
    7. then run the server (python3 manage.py runserver)
  
  Api's:
    1. User create api: POST http://127.0.0.1:8000/api/v1/users
          requestBody {
              "name" : <name>, (max 50 char)
              "password": <password> (minimum 8 char),
              "mobileNumber" : <mobileNumber> (max 14 char, min 11 char),
              "balance": Decimal
          }
          
     2. send money transaction api: POST http://127.0.0.1:8000/api/v1/users/<userUUID>/transactions
          requestBody [
              {
                "recieverId": <receiverUUID>, get other user uuid from profile table,
                "amount": Decimal
              },
              {
                "recieverId": <recieverUUID>,
                aomunt: Decimal
              }
          ]
          
      3. Get user transactions api: GET http://127.0.0.1:8000/api/v1/users/<userId>/transactions
      
      4. add schedule user for schedule transaction api: POST http://127.0.0.1:8000/api/v1/users/<userId>/schedulers
            requestBody {
              "recieverId": <recieverUUID>, get other user uuid from profile table,
              "amount": Decimal
            }
            
       For running test case:
          1. run python3 manage.py runserver in one tab
          2. in another tab after activate virtual env and got to moneytransfer/moneytransferplatform directory
          3. then run python3 manage.py test
