import requests

PARAMETERS = {
    'amount': 20,
    'type': 'boolean'
}

response = requests.get('https://opentdb.com/api.php',params=PARAMETERS)
data = response.json()
quizz = data['results']
question_data = quizz

