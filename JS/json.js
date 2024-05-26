// JavaScript Object Notation -->JSON
// JSON.stringify()
// JSON placeholder,GET data, Display data on UI...
// console.log("fatching");
// fetch('https://jsonplaceholder.typicode.com/todos/1')
// .then(response => response.json())
// .then(json => console.log(json))

// fetch("https://jsonplaceholder.typicode.com/todos/1")
// .then(res =>res.json())  //.json is not similar but close to JSON.parse
// .then(data =>{
//     console.log(data)
// })

// fetch("https://jsonplaceholder.typicode.com/todos/1")
// .then(res=>res.json())
// .then(data =>{
//     console.log("HI")
// })



function loadData(){
    const url = "https://jsonplaceholder.typicode.com/todos/1";
    fetch(url)
    .then(response =>response.json())
    .then(data=>{
        console.log(data);
    })
}

// const div = document.createElement("div");
// div.classList.add=("container");
// const html = `
//     <h4>User Information</h4>
//     <h5>Name: UserName:</h5>
//     <h6>title:UserTitle</h6>
//     <h6>description:UserDescription<h6>

// `;

const helloWorld = ()=>{
    const div = document.body.appendChild(document.createElement("div"));
    div.classList.add("contaner");
    
    div.innerHTML = `
        <h2>Name:UserName</h2>
        <h4>Title:UserTitle</h4>
        <h4>Id:UserID</h4>
        <h4>Description:UserDescription</h4>
    `;
    const h2 = document.createElement("h2");
    h2.innerText = "Hello World"
    console.log(div)
}

