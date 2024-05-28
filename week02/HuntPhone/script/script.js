
const loadData = async (searchText)=>{
    const url = `https://openapi.programming-hero.com/api/phones?search=${searchText}`
    const res = await fetch(url)
    const data = await res.json();
    const phones = data.data
    displayData(phones)
}



const displayData = (phones,isLine)=>{
    const productContainer = document.getElementById("product-container");
    
    if(isLine){
        productContainer.classList.remove("d-flex");
    }
    else{
        productContainer.classList.add("d-flex");
    }
    productContainer.textContent = "";
    // phones = phones.slice(0,8)
    phones.forEach(phone => {
        const itemPhone = document.createElement("div");
        itemPhone.innerHTML = `
        <div class="card">
            <img src="${phone.image}" class="card-img-top" >
            <div class="card-body">
                <h5 class="card-title">${phone.phone_name}</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="btn btn-primary">Show Details</a>
            </div>
        </div>
        `
        itemPhone.classList.add("mt-3","col-3")
        productContainer.appendChild(itemPhone)
    });
}

const searchField = ()=>{
    const searchValue = document.getElementById("search-field").value;
    loadData(searchValue)
    document.getElementById("search-field").value = "";
}

const showGrid = ()=>{
    displayData
}