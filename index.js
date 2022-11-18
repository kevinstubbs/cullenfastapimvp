// this was once commented out and included in index.html script tag due to one image in a batch giving a CORS error

 //handle read and process photos
async function loaded(reader) {
    // photos = document.getElementById('photos');
    // console.log(photos);
    // console.log(reader);

    // used to work
    // https://hf.space/embed/jph00/pets/+/api/predict/
    const response = await fetch('https://7504cc1e81cca145.gradio.app/run/predict', {
      method: "POST", body: JSON.stringify({ "data": [reader.result] }),
      headers: { "Content-Type": "application/json" }
    });
    const json = await response.json();
    // console.log(reader);
    console.log("json", json);
   
   // storing data from API call
    const label = json['data'][0]['confidences'][0]['label'];
    const conf = 100*(json['data'][0]['confidences'][0]['confidence']).toPrecision(4);
    console.log(label);
    console.log(conf);
    // displaying data from API call
    const div = document.createElement('div');
    div.innerHTML = `<br/><img src="${reader.result}" width="300"> <p>${label}</p> <p>${conf}<p>`
    document.body.append(div);
    
  }

  // read files uploaded
  function read(file) {
    console.log(file);
    const reader = new FileReader();
    // console.log(file);
    reader.addEventListener('load', () => loaded(reader))
    reader.readAsDataURL(file);
    // console.log(file);
  }
  photos.addEventListener('input', () => { [...photos.files].map(read) });

    // call python script integration attempts
  // const result = require('subprocess').result
  




  /// test button javascript
var testEl = document.querySelector('#testbtn');

var testfunction = function(event) {
  event.preventDefault();


  console.log('test worked');
  alert('test worked');


};

testEl.addEventListener('click', testfunction);


// python bridge
reportname= 'report_13-Nov-2022.pdf'

var testEl2 = document.querySelector('#testbtn2');
var testfunctionpython = function(event) {
  event.preventDefault();
  // window.open('http://127.0.0.1:8000/docs', '_blank').focus();
  window.open(`http://127.0.0.1:8000/static/${reportname}`, '_blank').focus();
  
};
testEl2.addEventListener('click', testfunctionpython);













// caption input
var captionButton = document.getElementById('cabtionbtn');

// captionButton.addEventListener('click', function(){
//   const input = document.getElementById("captionText").value;
  
// });

// var testfunctioncaption = function(event) {
//   event.preventDefault();
//   alert("Input: "+ input);
  
// }
if(captionButton){
  captionButton.addEventListener('click', swapper, false);
  const input = document.getElementById("captionText").value;
  alert("Input: "+ input);
}
// captionButton.addEventListener('click', function(){
//   // event.preventDefault();
//   const input = document.getElementById("captionText").value;
//   alert("Input: "+ input);
// });

const btn= document.getElementById("btn");

btn.addEventListener('click', function(){
  var name = document.getElementById("myName").value;
  alert("Name: "+ name);
});