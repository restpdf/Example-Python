import requests

apiKey = ''

response = requests.post(
    'https://api.restpdf.io/v1/pdf',
    headers = {
        'X-API-KEY'   : apiKey,
        'content-type': 'application/json'
    },
    json= {
        "output": "data",
        "url": "https://www.google.co.uk"
    }
)

if response.status_code == 200:
    with open('google.pdf', 'wb') as file:
        file.write(response.content)
else:
    print("There was an error converting the PDF")