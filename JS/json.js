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