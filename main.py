from flask import Flask, jsonify
from random import randint
import boto3
import os

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({
        'status': 'ok'
    })

@app.route('/record', method=['POST'])
def record():

    bucketName = os.getenv('BUCKET')

    number = randint(1000, 100000)

    path = 'record-' + str(number) + '.log'

    # falta a credencial aqui
    s3 = boto3.client('s3')

    try:
        s3.put_object(
            Bucket=bucketName, # type: ignore
            Key=path,
            Body=str(number)
        )

    except Exception as e:
        print("Something happened: ", e)
        return jsonify({
            'status': 'failed'
        }) 

    return jsonify({
        'status': 'ok'
    })
