const { onRequest } = require('firebase-functions/v2/https');

const express = require('express');
const bodyParser = require('body-parser');

const sendPostRequest = require('./service/postRequest');
const analyzeBody = require("./integration/analyzeBody");

const app = express();

app.use(bodyParser.json());

//GET request from ondc
app.get('/api', (req, res) => {
  const requestData = req.body;
  console.log("request data: ", requestData);
  res.send('Hello from Laathi!');
});

//POST request from ondc
app.post('/api', (req, res) => {
  const requestData = req.body;
  console.log(requestData);
  res.status(200).json({ message: 'Request processed successfully from Laathi' });
});

//read POST requests from laathi app to send search,select etc apis to ondc
app.post('/app/sendapis', (req, res) => {
  const requestData = req.body;
  console.log("from laathi app : ", requestData);
  analyzeBody(requestData);
});

//Testing api
app.post('/testing/api', (req,res) => {
  const requestData = req.body;
  console.log("request body :",requestData);
  sendPostRequest('https://ondc-catch.free.beeceptor.com', requestData)
    .then(response => {
      res.status(200).send("POST sent successfully!");
    })
    .catch(error => {
      console.error(error);
      res.status(500).send("POST request failed!");
    });
});

exports.laathi = onRequest(app);
