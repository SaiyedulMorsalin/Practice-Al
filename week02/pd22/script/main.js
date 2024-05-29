const loadDefault = async ()=>{
    const res = await fetch("https://www.themealdb.com/api/json/v1/1/categories.php");
    const data = await res.json();
    const categories = data.categories;
    displayCategories(categories);
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
        let foodItem = document.createElement("div");
        // foodItem.classList.add("col-md-3","c");
        foodItem.classList.add("col-md-3","c")
        foodItem.innerHTML = `
            <a class="cat-link text-center" data-bs-toggle="modal" data-bs-target="#exampleModal" onclick="showModal('${category.strCategory}')"  >
                <div class="card ">
                <img src="${category.strCategoryThumb}" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">${category.strCategory}</h5>
                </div>
                </div>
                
            </a>
            
        `;
        foodContainer.appendChild(foodItem);
        // console.log(category)
    });
}

const showModal = async (categoryName)=>{
    const res = await fetch(`https://www.themealdb.com/api/json/v1/1/filter.php?c=${categoryName}`);
    const data = await res.json();
    const meals = data.meals
    meals.forEach(meal =>{
        console.log(meal);
    })
    
    
}