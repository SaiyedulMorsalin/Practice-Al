
const loadComments = ()=>{
    const url = "https://jsonplaceholder.typicode.com/comments";
    fetch(url)
    .then(res =>res.json())
    .then(data =>console.log(data))
    .catch(error =>console.log("error hapend",error))
}

const loadComments2 = async ()=>{
    const res = await fetch("https://jsonplaceholder.typicode.com/comments");
    const data = await res.json();
    console.log(data)
}