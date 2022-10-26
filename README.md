## Purpose

The purpose of this repo is to display two proof of concepts: 

1. Using a website to upload photos and view the classification of the photos using an AI algorithm API call using javascript. 
2. Using a python script that uses docxtpl library to populate a word document template 

## Usage 

To use this repo:

1. Open the index.html file in your browser. Select 'catTest.jpg', 'dogTest.jpg', 'dunnoTest.jpg' or any photos of cats or dogs on your computer to view the breed of the animal and the confidence of the answer.
2. Run the python script to create a word document and pdf (output in reports folder) that populated a template (photoExhibitionTemplate2.docx) with a table of photos (from ./images folder) and text. 


## End goal
The end goal is to get photos from the Egnyte API, seemlessly pass them to a custom (to be built) AI algorithm on a similar API as this application uses (hugging faces), and use the results to generate a downloadable word document. 

## Immediate struggles
1. Using javascript and python together
    - Passing the results of the huggingfaces AI API in index.html or index.js through the python script, index.js, to generate a word document. 

## Things I have tried
1. Using require in JS (slightly preferred)
2. Using flask


## Other Struggles
1. Getting Egnyte API to work (need to understand call back url more) 
2. Encountering CORS errors. 




