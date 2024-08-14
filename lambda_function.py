# lambda_function.py
from flask import jsonify
from app import app

def lambda_handler(event, context):
    with app.test_request_context(path=event['path'], method=event['httpMethod']):
        response = app.full_dispatch_request()
        return {
            'statusCode': response.status_code,
            'headers': dict(response.headers),
            'body': response.get_data(as_text=True)
        }
