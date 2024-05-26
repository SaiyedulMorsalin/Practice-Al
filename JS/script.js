const loadUsers = ()=>{
    const url = "https://jsonplaceholder.typicode.com/users";
    fetch(url)
    .then(res =>res.json())
    .then(data =>{
        displayUsers(data);
    })
}

const displayUsers = (users)=>{
    console.log(users);
    for(const user of users){
        console.log("Name: ",user.name)
        console.log("Email: ",user.email)
    }
}

// https://jsonplaceholder.typicode.com/posts  --> object of array