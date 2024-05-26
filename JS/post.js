
const loadPost = () =>{
    const url = "https://jsonplaceholder.typicode.com/posts";
    fetch(url)
    .then(res =>res.json())
    .then(data =>{
        displayPosts(data)
    })
}


/*
1. get the container element where you want to add the new elements.
2. create child element
3. set inner text or innerHTML
4. appendChild



*/


function displayPosts  (posts){
    const postContainer = document.getElementById("post-container");
    for(const post of posts){
        const div = document.createElement('div');
        div.innerHTML = `
            <h4>User-${post.id}</h4>  
        `;
        postContainer.appendChild(div);
    }
    
}

//https://jsonplaceholder.typicode.com/posts




// HTTP Status Code......
//     200 -->>OK
//     301 -->>Moved Parmanently
//     302 -->>Moved Parmanently
//     404 -->>Not Found
//     500 -->>Internal Server Error
//     503 -->>Service Unavailable
