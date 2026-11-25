const myForm = document.getElementById("registration-form");

myForm.addEventListener(
    
"submit", 
async function (e)
{
    e.preventDefault();
    const formdata = new FormData(myForm);

    console.log("Registration form submitted");

    const userData = Object.fromEntries(formdata.entries());

    const requestBody = JSON.stringify(userData);
    
    const url = "http://127.0.0.1:8000/api/auth/register";

    const response = await fetch(url, {
        method: "POST",
        headers:{"Content-Type": "application/json"},
        body:requestBody

    })

    console.log("Registration status:", response.status);

    const result = await response.json();

    if (response.ok){

        document.getElementById("form-message").textContent = "Account created successfully!";

        myForm.reset();



    }else{

        document.getElementById("form-message").textContent = `Registration failed (HTTP ${response.status}).`;

    }
}

);