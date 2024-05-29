const loadDefault = async ()=>{
    const res = await fetch("https://www.themealdb.com/api/json/v1/1/categories.php");
    const data = await res.json()
    const categories = data.categories;
    displayCategories(categories)
}


loadDefault()




const search = ()=>{
    const searcValue = document.getElementById("search-value").value;
    console.log(searcValue);
    document.getElementById("search-value").value ="";
}



const displayCategories = (categories)=>{
    const foodContainer = document.getElementById("food-container");
    categories = categories.slice(0,12)
    categories.forEach(category => {
        const foodItem = document.createElement("div");
        foodItem.classList.add("col-md-3","c");
        foodItem.innerHTML = `
            <a class="cat-link text-center" onclick="showModal()"data-bs-toggle="modal" data-bs-target="#exampleModal">
                <div class="card ">
                <img src="${category.strCategoryThumb}" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">${category.strCategory}</h5>
                </div>
                </div>
            </a>
        `
        foodContainer.appendChild(foodItem)
        console.log(category)
    });
}

const showModal = ()=>{
    const modalContainer = document.getElementById("modal-container");
    const modalitem = document.createElement("div");
    modalitem.innerHTML = `
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                ...
            </div>
            
        </div>
    </div>
    </div>
    
    `;
    modalContainer.appendChild(modalitem)
}