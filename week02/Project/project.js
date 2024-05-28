
const loadData = async ()=>{
    const res = await fetch("https://fakestoreapi.com/products");
    const data = await res.json();
    displayData(data)
}
loadData() 

const displayData = (data)=>{
    const productContainer = document.getElementById("item-container");
    data.forEach(product => {
        const productItem = document.createElement("div");
        productItem.classList.add("col-md-3","product")
        productItem.innerHTML = `
            <div class="card">
                <img src="${product.image}" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">${product.title}</h5>
                    <p class="card-text">Some quick example text to build on the card title and make up
                        the bulk
                        of the
                        card's content.</p>
                    <h6>
                    <a href="#" class="btn btn-primary">Details</a>
                    <a href="#" onclick="addCart(${product})" class="btn btn-primary">Add Cart</a>
                </div>
            </div>
        `
        productContainer.appendChild(productItem)
        // console.log(product)
    });
}

const addCart = (product) =>{
    // console.log(product)
}



// const addToCart = ()=>{
//     const cart = document.getElementById("cart-body");
//     cart.innerHTML = `
//         <p>Sub Total: <strong class="cart-value">${10}</strong></p>
//         <p>Discount: <strong class="cart-value">${0}</strong></p>
//         <p>Tax: <strong class="cart-value">${0}</strong></p>
//         <p>Shipping: <strong class="cart-value">${0}</strong></p>
//         <p>Total: <strong class="cart-value">${0}</strong></p>
//         <button class="btn btn-primary mx-auto ">Checkout</button>
//     `

// }
