// capture URL
var urlToSend = window.location.href;

// send url to python program and then receives back a response 
fetch('https://europe-west1-skilled-creek-283412.cloudfunctions.net/TextClassFunction', {
  method: 'POST',
  body: JSON.stringify(urlToSend),
  headers:{
    'Content-Type': 'application/json'
  } })
.then(function (response){
	return response.text();
}).then(function (text) {
	alert(text);
})	

// catches errors
.catch(error => console.error('Error:', error));



