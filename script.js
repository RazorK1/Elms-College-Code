let net;
loadMobileNet();
          
async function loadMobileNet() {
  console.log('Loading mobilenet..');
  document.getElementById("output").innerHTML = 'Loading mobilenet..';

  // Load the model.
  net = await mobilenet.load();
  console.log('Successfully loaded model.');
  document.getElementById("output").innerHTML = 'Successfully loaded model. Click Predict or choose a new image.';
}

// This function uses the model we loaded to make a prediction on myImage 
async function predict() {
  const img = document.getElementById('myimage');
  const netPrediction = await net.classify(img);
console.log(netPrediction);

const predictionsFormatted = netPrediction.map(prediction => prediction.className + " : " + (prediction.probability * 100).toFixed(2) + '%');

document.getElementById("output").innerHTML = predictionsFormatted.join("<br>");
  
}

 // This is the file chooser that loads it into myimage
const file = document.getElementById('uploadedImage');
file.addEventListener('change', onFileSelected);

function onFileSelected(event) {
  const selectedFile = event.target.files[0];
  const reader = new FileReader();
  const image = document.getElementById("myimage");
  reader.onload = function (event) {
    image.src = event.target.result;
  };
  reader.readAsDataURL(selectedFile);
}      
