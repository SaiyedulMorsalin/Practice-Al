
const api = async ()=>{

};

const search = async ()=>{
    const searchValue = document.getElementById("searcing").value;
    console.log(searchValue)
    
    if(searchValue == " " || searchValue == ""){
        alert("search result is empty!!")
    }
    else{
        const card = document.getElementById("card");
        const url = `https://openapi.programming-hero.com/api/phones?search=${searchValue}`
        const res = await fetch(url);
        const data = await res.json();
        console.log(data.data)
        if(data == null){
            alert("Not FOUNd")
        }
        else{
            addCardItem (data.data)
        }
        

        
    }

    document.getElementById("searcing").value=""
};

const addCardItem = (data)=>{
        const cardContainer = document.getElementById("card-container");
        cardContainer.classList.add("border-none")
        for(phone of data){
            const cardItem = document.createElement("div");
            cardItem.classList.add("card-item","col-md-4","gap-3","mb-3");
            cardItem.innerHTML = `
                <div class ="card">
                    <img src=${phone.image} class="card-img-top" alt = "...">
                    <div class="card-body">
                        <h5 class="card-title">${phone.phone_name}</h5>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                        <a href="#" class="btn btn-primary">Buy Now</a>
                        <a onclick = "addToCart()" id = "add-cart" href="#" class="btn btn-primary">Add to Cart</a>
                    </div>
                </div>`;
            cardContainer.appendChild(cardItem);
        }
}
const showMore = (data) =>{
    for(let i=0;i<9;i++){
        addCardItem(data);
    }
}
const addToCart = ()=>{
    let  addCart = document.getElementById("add-cart");
    addCart.innerText = "Added to Card";

}