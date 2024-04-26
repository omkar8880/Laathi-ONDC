# from firebase_functions import https_fn
# from firebase_admin import initialize_app
from analyzeBody import *
# from cryptic import *
import requests
import flask
import json
import datetime
import base64
import logging
from flask import Flask, jsonify, request
from http import HTTPStatus
from dotenv import load_dotenv
import os
# from cryptic_utils import create_authorisation_header

# import amansubprocess23

# initialize_app()
import pytz
from datetime import datetime
current_datetime = datetime.now().astimezone(pytz.timezone('Asia/Kolkata'))
current_datetime_iso8601 = current_datetime.strftime(
                "%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
print(current_datetime_iso8601)
# timestamp = datetime.utcnow().isoformat() + 'Z'
# print(timestamp)

load_dotenv()

app = flask.Flask(__name__)
logging.basicConfig(filename='my_log3.log',level=logging.DEBUG)


@app.route('/test')
def test():
    return 'Hello, Omkar!'

# def create_authorization_header(username):
#     password = 'abcd1234'
#     # Combine the username and password with a colon and encode as bytes
#     credentials = f"{username}:{password}".encode('utf-8')

#     # Encode the credentials using base64
#     encoded_credentials = base64.b64encode(credentials).decode('utf-8')

#     # Create the Authorization header value
#     header_value = f"Basic {encoded_credentials}"

#     # Return the header as a dictionary
#     return header_value

# @app.get("/")
@app.route('/get_request', methods=["POST"])

# @app.get("/")
def get_request():
    # return "Hello"
    requestData = flask.request.json
    print(requestData)

    apiBody = str(requestData)
    url = "https://ondc-catch.free.beeceptor.com"

    print("started")

    # try:
    response = requests.post(url, json=apiBody)
    response.raise_for_status()  # Raise an exception for HTTP errors
    print("ended")
    try:
        return response.text, response.status_code
    except requests.exceptions.RequestException as e:
            # Handle network-related errors
            print("An error occurred:", str(e))
            return "Internal Server Error", 500  # Consider returning a more specific status code
    except requests.exceptions.HTTPError as e:
            # Handle HTTP errors (e.g., 4xx or 5xx responses)
            print("HTTP error:", str(e))
            return "Bad Request", 400  # Consider returning a more specific status code

# def create_authorisation_header(apiBody, secret_key):
#     # Your code here
#     # Use apiBody and secret_key to create the authorization header
#     # Example:
#     authorization_header = f"Bearer {apiBody}:{secret_key}"
#     return authorization_header
@app.route("/subscribe" ,methods=["POST"])
def handle_subscribe():
    logging.debug("Within subscribe")
    requestData = flask.request.json
    url = "https://staging.registry.ondc.org/subscribe"
    mynewheader = {
        'Content-Type':'application/json',
        }
    response = requests.post(url, headers=mynewheader, json=requestData)#json.dumps(myjson))#requestData)

    response_data = {
        "response_text": response.text,
        "status_code": response.status_code,
        "request_data": requestData
    }
    return response_data, requestData

@app.post("/lookup")
def handle_lookUp():
    logging.debug("Within lookUp")
    requestData = flask.request.json
    url = "https://staging.registry.ondc.org/lookup"
    mynewheader = {
        'Content-Type':'application/json',
        }
    response = requests.post(url, headers=mynewheader, json=requestData)#json.dumps(myjson))#requestData)

    response_data = {
        "response_text": response.text,
        "status_code": response.status_code,
        "request_data": requestData
    }
    return response_data, requestData

@app.post("/vlookup")
def handle_vlookUp():
    logging.debug("Within vlookUp")
    requestData = flask.request.json
    url = "https://staging.registry.ondc.org/vlookup"
    mynewheader = {
        'Content-Type':'application/json',
        }
    response = requests.post(url, headers=mynewheader, json=requestData)#json.dumps(myjson))#requestData)

    response_data = {
        "response_text": response.text,
        "status_code": response.status_code,
        "request_data": requestData
    }
    return response_data, requestData


@app.route("/search" , methods=["POST"])
def handle_search():
    logging.debug("Within handle_search()")
    requestData = flask.request.json
    # print(requestData)
    myauth=request.headers.get('Authorization')
    logging.debug(f"Value of myauth: {myauth}")
    mynewheader = {
        'Authorization': myauth,
        'Content-Type':'application/json',
        }
    # time_str = datetime.datetime.utcnow().isoformat()
    # # requestData["context"]["timestamp"] = time_str[:23] + "Z"
    # apiBody = str(requestData)
    # auth_header = create_authorization_header(str(requestData))
    # header = {"Authorization": my_string2, "Content-Type": "application/json"}
    # urlOld = "https://pilot-gateway-1.beckn.nsdl.co.in/search"
    url = "https://staging.gateway.proteantech.in/search"
    # swaggerhuburl = "https://virtserver.swaggerhub.com/ONDC/ONDC-Protocol-Retail/1.0.29/search"


    response = requests.post(url, headers=mynewheader, json=requestData)#json.dumps(myjson))#requestData)

    response_data = {
        "response_text": response.text,
        "status_code": response.status_code,
        "request_data": requestData
    }
    return response_data, requestData

    # try:
    #     response = requests.post(url, headers=mynewheader, json=requestData)#json.dumps(myjson))#requestData)
    #     print("search 2 new")
    #    # print(response.json())
    #     # Process the response if needed
    #     return response.text, response.status_code,
    # except requests.exceptions.RequestException as e:
    #     # Handle the request exception
    #     logging.debug("search error")
    #     return str(e), 5000

@app.route("/on_search", methods=["POST","GET"])
def handle_onsearch():
    requestData = flask.request.json
    # handle_search()
    print(requestData)
    return "Hello2"

# @app.route("/on_search", methods=["POST"])
# def handle_onsearch():
#     requestData = flask.request.json
#     # handle_search()
#     print(requestData)
#     return "Hello2"


# @app.post("/post_request")
# def post_request():
#     requestData = flask.request.json
#     apiBody = analyzeJSON(requestData)
#     mycontext = requestData.get("context", {})
#     myaction = mycontext.get("action")
#     if (myaction == "search"):
#         print(1)
#         time_str = datetime.datetime.utcnow().isoformat()
#         apiBody["context"]["timestamp"] = time_str[:23] + "Z"
#         auth_header = create_authorisation_header(str(apiBody))
#         # print(verify_authorisation_header(newBody,str(requestData),"N3xvGkOY7Gj40M2tOyZHHxK2kxVz+G1Ooa7gYenFdAs="))
#         header = {"Authorization":auth_header, "Content-Type": "application/json"}
#         url = "https://pilot-gateway-1.beckn.nsdl.co.in/search"
#         try:
#             response = requests.post(url, json=apiBody,headers=header)
#             print(2)
#             print(response.json())
#             # Process the response if needed
#             return response.text, response.status_code
#         except requests.exceptions.RequestException as e:
#             # Handle the request exception
#             print(3)
#             return str(e), 500
#     else:
#         print(apiBody)
#         print("on-search triggered")
#         url = "https://ondc-catch.free.beeceptor.com"
#         dict = {"status":"ACK"}
#         dict2 = {"ack":dict}
#         responseBody = {"message":dict2}
#         try:
#             response = requests.post(url, json=apiBody)
#             # Process the response if needed
#             return json.dumps(responseBody)
#         except requests.exceptions.RequestException as e:
#             # Handle the request exception
#             return str(e), 500
#     return json.dumps(apiBody)



# @app.post("/next_request")
# def next_request():
#     requestData = flask.request.json
#     apiBody = str(requestData)
#     # apiBody = str(analyzeJSON(requestData))
#     newBody = create_authorisation_header(apiBody)
#     #"laJsPb2pLe9R8Ssl/XAyE+JN2jjapFiZaOGqb3lPfqU3fG8aQ5jsaPjQza07JkcfEraTFXP4bU6hruBh6cV0Cw==")
#     url = "https://pilot-gateway-1.beckn.nsdl.co.in"
#     header = {"Authorization":newBody}

#     try:
#         response = requests.post(url, json=requestData, headers=header)
#         # Process the response if needed
#         return response.text, response.status_code
#     except requests.exceptions.RequestException as e:
#         # Handle the request exception
#         return str(e), 500

# @https_fn.on_request()
# def api(req: https_fn.Request) -> https_fn.Response:
#     with app.request_context(req.environ):
#         return app.full_dispatch_request()

# app.run()
# print("I'm in main")
# get_request()


# order is important!! The following command should be at the end of the file!!
if __name__ == "__main__":
    app.run(debug = True , port = 5000)
