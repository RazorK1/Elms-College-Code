
//  replace this model URL with your own
// do not use mine tNewj2I6y
let modelURL = 
//"https://teachablemachine.withgoogle.com/models/tNewj2I6y/"; 
"https://teachablemachine.withgoogle.com/models/rS6IjP8ZH/";
setupModel(modelURL);
            

let model;

// This function sets up the model trained in Teachable Machine.
async function setupModel(URL) 
{
    console.log('Loading your model..');
    document.getElementById("output").innerHTML = 'Loading mobilenet..';
    // the model.json file stores a reference to the trained model
    const modelURL = `${URL}model.json`;
    // the metatadata.json file contains the text labels of your model and additional information
    const metadataURL = `${URL}metadata.json`;

    // Load your model 
    model = await tmImage.load(modelURL, metadataURL);
    console.log("Loaded your model");
    document.getElementById("output").innerHTML = 'Successfully loaded model. Click Predict or choose a new image.';
}


// This function uses the model we loaded to make a prediction on myImage 
async function predict() 
{
  const img = document.getElementById('myimage');
 
  const myModelPrediction = await model.predict(img);
   
   document.getElementById("output").innerHTML = myModelPrediction[0].className + ": " + myModelPrediction[0].probability.toFixed(2) * 100 + "% <br>" +
   myModelPrediction[1].className + ": " + myModelPrediction[1].probability.toFixed(2) * 100 + "%";
   console.log(myModelPrediction);
}


 // This is the file chooser that loads a new file into myimage
const file = document.getElementById('uploadedImage');
file.addEventListener('change', onFileSelected);

function onFileSelected(event) 
{
  const selectedFile = event.target.files[0];
  const reader = new FileReader();
  const image = document.getElementById("myimage");
  reader.onload = function (event) {
    image.src = event.target.result;
  };
  reader.readAsDataURL(selectedFile);
}   
