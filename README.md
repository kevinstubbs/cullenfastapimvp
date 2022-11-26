# To do
hugging faces api
fast api
9pm monday

# Table of Contents

- [Purpose](#purpose)
- [Usage](#usage)
- [EndGoal](#endgoal)
- [Struggles](#struggles)
- [Attempts](#attempts)
- [OtherStruggles](#otherstruggles)

## Purpose

The purpose of this repo is to display two proof of concepts: 

1. Interacting with a website to upload photos. The photos are sent to a placeholder AI algorithm API call using javascript, and the classification of the photos are displayed on the webpage along with the confidence of the answer. 
2. Using a python script that uses docxtpl library to populate a word document template. 

## Usage 

To use this repo:

pipenv run uvicorn fast:app --reload

1. Open the index.html file in your browser. Select 'catTest.jpg', 'dogTest.jpg', 'dunnoTest.jpg' or any photos of cats or dogs on your computer to view the breed of the animal and the confidence of the answer.
2. Run the python script to create a word document and pdf (output in reports folder) that populated a template (photoExhibitionTemplate2.docx) with a table of photos (from ./images folder) and hard coded text. 


## EndGoal
The end goal is to seemlessly pass photos (either uploaded or eventually with [Egnyte API](https://developers.egnyte.com/docs) call) to an AI algorithm on a similar API as this application uses (hugging faces), and use the results to generate a downloadable word document with the python script. 

## Struggles
1. Calling python script from javascript
    - Passing the results of the huggingfaces AI API in index.html through the python script, index.py, to generate a word document. 


# Testing endpoints with Postman
## Create a report with two images (as cURL)
curl --location --request POST 'http://127.0.0.1:8000/input_metadata' \
--header 'Content-Type: application/json' \
--data-raw '{
  "data": [{
      "folder_name": "images",
      "file_name": "catTest.jpg",
      "caption": "something smol"
  }, {
      "folder_name": "images",
      "file_name": "dogTest.jpg",
      "caption": "good boi"
  }]
}'

## As javascript vanilla Fetch
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "data": [
    {
      "folder_name": "images",
      "file_name": "catTest.jpg",
      "caption": "something smol"
    },
    {
      "folder_name": "images",
      "file_name": "dogTest.jpg",
      "caption": "good boi"
    }
  ]
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("http://127.0.0.1:8000/input_metadata", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));