const getUser = ()=>{
    const url = "https://jsonplaceholder.typicode.com/users"
    fetch(url)
    .then(res =>res.json())
    .then(data =>{
        displayUser(data)
        
    })
}

const displayUser = (users)=>{
    let cnt =1;

    console.log(users);
    // console.log(cnt+=1);
}