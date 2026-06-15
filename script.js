async function findRoute(){

const source=document.getElementById("source").value;

const destination=document.getElementById("destination").value;

const response=await fetch("http://127.0.0.1:8000/find-route",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
source:source,
destination:destination
})

});

const data=await response.json();

let html="";

data.routes.forEach(route=>{

html+=`

<div class="card">

<h2>${route.type}</h2>

<p><b>Mode:</b> ${route.mode}</p>

<p><b>Time:</b> ${route.time}</p>

<p><b>Cost:</b> ${route.cost}</p>

</div>

`;

});

document.getElementById("result").innerHTML=html;

}