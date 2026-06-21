const API =
"http://127.0.0.1:8000";



async function login(){


let email =
document.getElementById(
"email"
).value;



let response =
await fetch(
API+"/api/auth/login",
{

method:"POST",

headers:{
"Content-Type":
"application/json"
},

body:JSON.stringify({

email:email

})

});


let data =
await response.json();



localStorage.setItem(
"token",
data.token
);


window.location =
"dashboard.html";


}







async function uploadPDF(){


let file =
document
.getElementById("pdf")
.files[0];


let form =
new FormData();


form.append(
"file",
file
);



await fetch(
API+"/api/upload",
{

method:"POST",

body:form

});


alert(
"PDF Uploaded"
);



}







async function askAI(){


let question =
document.getElementById(
"question"
).value;



let response =
await fetch(
API+"/api/query",
{

method:"POST",

headers:{

"Content-Type":
"application/json"

},

body:JSON.stringify({

question:question

})

});


let data =
await response.json();



document
.getElementById("answer")
.innerHTML =
data.answer;


}