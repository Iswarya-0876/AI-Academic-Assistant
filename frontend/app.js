const API = "http://127.0.0.1:8000";


// ================= REGISTER =================

async function register(){


    const username =
    document.getElementById("username").value;


    const email =
    document.getElementById("email").value;


    const password =
    document.getElementById("password").value;



    let response =
    await fetch(
        API + "/api/auth/register",
        {

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },


            body:JSON.stringify({

                username: username,

                email: email,

                password: password

            })

        }
    );



    let data =
    await response.json();



    console.log(data);



    if(response.ok){

        alert("Registration successful");

        window.location.href =
        "/frontend/index.html";

    }

    else{

        alert(
            data.detail ||
            "Registration failed"
        );

    }

}





// ================= LOGIN =================


async function login(){


    const email =
    document.getElementById("email").value;



    const password =
    document.getElementById("password").value;



    let response =
    await fetch(
        API + "/api/auth/login",
        {


            method:"POST",


            headers:{

                "Content-Type":
                "application/json"

            },


            body:JSON.stringify({

                email:email,

                password:password

            })

        }

    );




    let data =
    await response.json();



    console.log(data);



    if(response.ok){


        localStorage.setItem(
            "token",
            data.access_token || data.token
        );



        window.location.href =
        "/frontend/dashboard.html";


    }


    else{


        alert(

            data.detail ||
            "Invalid login"

        );

    }


}





// ================= UPLOAD PDF =================


async function uploadPDF(){


    let file =
    document.getElementById("pdf").files[0];



    let form =
    new FormData();



    form.append(
        "file",
        file
    );



    let response =
    await fetch(

        API + "/api/upload",

        {

            method:"POST",

            body:form

        }

    );



    let data =
    await response.json();



    console.log(data);



    alert(
        "PDF uploaded successfully"
    );


}





// ================= ASK AI =================


async function askAI(){


    let question =
    document.getElementById("question").value;



    if(question.trim()=="")
    return;



    addMessage(
        question,
        "user"
    );



    document.getElementById("question").value="";



    let response =
    await fetch(

        API + "/api/query",

        {


            method:"POST",


            headers:{

                "Content-Type":
                "application/json"

            },


            body:JSON.stringify({

                question:question

            })

        }

    );



    let data =
    await response.json();



    addMessage(

        data.answer ||
        "No response",

        "bot"

    );


}





// ================= CHAT UI =================


function addMessage(text,type){


    let box =
    document.createElement("div");



    box.className =
    type;



    box.innerHTML =
    text;



    document
    .getElementById("messages")
    .appendChild(box);



}






function newChat(){


    document
    .getElementById("messages")
    .innerHTML =
    "";


}