# Morph Card View POC • AWS Lambda • Python

This repository contains the Python code for an AWS Lambda function designed to create Morph Card View response when receiving Morph's `card_view.requested` webhook event.

## Prerequisites

Before you begin, ensure you have the following:

-  AWS Account with access to AWS Lambda and API Gateway.
-  Python 3.7 or higher.

## Getting Started

### Step 1 • Create a Lambda Function

1. Create a new blank Python Lambda function in the AWS Management Console.
2. Copy and paste the code from the Python file (`function_lambda.py`) into the Lambda code editor.

### Step 2 • Environment Variables

In the Configuration tab, go to the Environment variables section and click on "Edit". Then, add two new variables:

1. `MORPH_API_KEY`: This should be the API key provided by Morph.
2. `MORPH_API_SECRET`: This should be the API Secret associated with your Morph API Key.

_You can find your API key and secret from your [Morph Account](https://app.runmorph.dev/account)._

### Step 3 • Create an API Gateway Trigger:

In the Configuration tab, go to the Trigger section and click on "Add trigger". 

1. Select "API Gateway" and choose the HTTP API option (this is simpler to set up).
2. Click on "Set Permissions" when asked to give API Gateway permission to invoke Lambda function.

_You should now have the URL endpoint of your Lambda API Gateway._

### Step 4 • Subscribe to Morph Webhook Events:

Go to the [Morph Webhooks](https://app.runmorph.dev/webhooks) dashboard and create a new webhook subscription:

1. Select `Card View • Requested` event type
2. Paste the URL of your Lambda API Gateway endpoint in the provided URL field.
3. Create the webhook subscription
   
## Testing

Connect to Morph Playground and click on `Send Request` directly. You will now see the card generated from your AWS Lambda:

<img width="1252" alt="Capture d’écran 2023-11-13 à 18 17 20" src="https://github.com/run-Morph/card-view-poc-aws-python/assets/18643714/ba6b08d6-f9d6-483f-8fc0-f4c823c9e575">


If you encounter any issues, please reach out to [Henri Chabrand](mailto:henri.chabrand@gmail.com).

## Resources

-  [Morph API Documentation](https://runmorph.dev/)

## License

This project is open-source and is distributed under the [MIT License](https://opensource.org/licenses/MIT).
