import os
import json
import http.client

def lambda_handler(event, context):
    
    card_view_request = json.loads(event['body'])

    # Prepare API headers
    headers = {
        'x-api-key': os.environ.get('MORPH_API_KEY'),
        'x-api-secret': os.environ.get('MORPH_API_SECRET')
    }

    # Prepare API endpoint
    conn = http.client.HTTPSConnection('api.runmorph.dev')
    url = f"/v0/requests/{card_view_request['id']}/response"

    # Prepare the card view to be sent
    body = {
        "card_view": {
            "cards": [
                {
                    "title": "My First Python Card 🐍",
                    "contents": [
                        {
                            "type": "text",
                            "label": "Environment",
                            "value": "AWS Lambda"
                        },
                        {
                            "type": "text",
                            "label": "Language",
                            "value": "Python"
                        },
                        {
                            "type": "status",
                            "label": "System",
                            "value": "Operational",
                            "color": "SUCCESS"
                        }
                    ],
                    "actions": [
                        {
                            "type": "OPEN_URL_IN_IFRAME",
                            "label": "Open Morph in iFrame",
                            "url": "https://runmorph.dev/"
                        }
                    ]
                }
            ]
        }
    }

    # Make the POST request
    conn.request('POST', url, body=json.dumps(body), headers=headers)

    # Get the response
    res = conn.getresponse()

    # Check if the HTTP status code indicates an error
    if 200 <= res.status < 300:
        return {
            'statusCode': res.status,
            'body': 'Card created',
        }
    
    return {
        'statusCode': res.status,
        'body': 'Error from Morph endpoint',
    }
