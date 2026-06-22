const API="http://127.0.0.1:8000";



async function uploadPDF(){


let file =
document.getElementById("pdfFile").files[0];


if(!file){

alert("Select PDF first");

return;

}



let formData =
new FormData();


formData.append(
"file",
file
);



let response =
await fetch(

API+"/api/upload",

{

method:"POST",

body:formData

}

);



let data =
await response.json();



alert(data.message);



}




async function sendMessage(){


let question =
document.getElementById(
"question"
).value;



if(question==="") return;



document.getElementById(
"chatBox"
).innerHTML +=

`
<p>
<b>You:</b>
${question}
</p>
`;



let response =
await fetch(

API+"/api/query",

{

method:"POST",

headers:{

"Content-Type":"application/json"

},


body:JSON.stringify({

question:question

})


}

);



let data =
await response.json();



document.getElementById(
"chatBox"
).innerHTML +=


`

<p>

<b>AI:</b>

${data.answer}

</p>


`;



}