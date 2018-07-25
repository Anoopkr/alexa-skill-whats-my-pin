from botocore.vendored import requests
import os
def lambda_handler(event, context):
	print(event)
	if event['request']['type'] == "LaunchRequest":
		return on_launch(event, context)
	if event['request']['type'] == "IntentRequest":
		return find_my_pin(event, context)
	return "Thank you"

def find_my_pin(event, context):
	placename = event['request']['intent']['slots']['place']['value']
	print(placename)
	url = 'http://api.geonames.org/postalCodeSearchJSON?placename='+placename+'&maxRows=10&username=' + os.environ['username']
	response = requests.get(url)
	try:
		result = response.json()
	except ValueError:
		result = response.text
	output = {}
	output['response'] = {}
	output['response']['outputSpeech'] = {
		"type": "PlainText",
		"text": result['postalCodes'][0]['postalCode'],
		"ssml": "<speak>SSML text string to speak</speak>"
		}	
	print(output)
	return output
def on_launch(event, context):
	output = {}
	output['response'] = {}
	output['response']['outputSpeech'] = {
		"type": "PlainText",
		"text":  "Welcome to PIN Code Finder developed by Anoop kumar",
		"ssml": "<speak>SSML text string to speak</speak>"
		}	
	return output
