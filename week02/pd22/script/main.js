// const loadDefault = async ()=>{
//     const res = await fetch("https://www.themealdb.com/api/json/v1/1/categories.php");
//     const data = await res.json();
//     const categories = data.categories;
//     displayCategories(categories);
// }


// loadDefault()


const foodContainer = document.getElementById("food-container");
foodContainer.style.padding = "0";


const search = async ()=>{
    const searcValue = document.getElementById("search-value").value;
    const res = await fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${searcValue}`);
    const data = await res?.json();
    document.getElementById("search-value").value ="";
    // console.log(data)
    displayCategories(data.meals)

}

/* <a class="cat-link text-center" data-bs-toggle="modal" data-bs-target="#exampleModal" onclick="showModal('${category.strCategory}')"  >
                <div class="card ">
                <img src="${category.strCategoryThumb}" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">${category.strCategory}</h5>
                </div>
                </div>
                
            </a> */

const displayCategories = (meals)=>{
    const foodContainer = document.getElementById("food-container");
    foodContainer.textContent = "";
    foodContainer.innerHTML=`<h2 class="text-center mb-5">Meals</h2>`
    // categories = categories.slice(0,12)
    meals.forEach(meal => {
        let foodItem = document.createElement("div");
        // foodItem.classList.add("col-md-3","c");
        const mealName = meal.strMeal ? meal.strMeal.slice(0,10): "Unknown Meal";
        foodItem.classList.add("col-md-3","c");
        foodItem.innerHTML = `
                <a class="meal-link" onclick="showPage(${meal.idMeal},'${mealName}')">
                    <div class="card ">
                    <img src="${meal.strMealThumb}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">${mealName}</h5>
                    </div>
                    </div> 
                </a>
        `;
        foodContainer.appendChild(foodItem);
    });
}


const showPage = async (mealId,mealName) =>{
    console.log(typeof mealId,mealId)
    const res = await fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${mealId}`);
    const data = await res.json();
    const meal = data.meals;
    console.log("meal search by id",meal);
    const foodContainer = document.getElementById("food-container");
    foodContainer.textContent = "";
    const banner = document.getElementById("banner");
    banner.textContent = "";
    foodContainer.innerHTML=`<h2 class="text-center mb-3">${mealName}</h2>`;
    const foodItem = document.createElement("div");
    foodItem.classList.add("col-md-8","c","col-sm-3");
    const noMealIngredient = "Unknown Ingredient";
    const mealIngredient1 = meal[0].strIngredient1? meal[0].strIngredient1.slice(0,10):noMealIngredient;
    const mealIngredient2 = meal[0].strIngredient2? meal[0].strIngredient2.slice(0,10):noMealIngredient;
    const mealIngredient3 = meal[0].strIngredient3? meal[0].strIngredient3.slice(0,10):noMealIngredient;
    const mealIngredient4 = meal[0].strIngredient4? meal[0].strIngredient4.slice(0,10):noMealIngredient;
    const mealIngredient5 = meal[0].strIngredient5? meal[0].strIngredient5.slice(0,10):noMealIngredient;
    const mealIngredient6 = meal[0].strIngredient6? meal[0].strIngredient6.slice(0,10):noMealIngredient;
    foodItem.innerHTML = `
            <div class="card ">
            <img src="${meal[0].strMealThumb}" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title mb-3 intgredient ">Ingredients:</h5>
                <div class="list">
                    <ul class="list-container">
                        <li><i class="fa-solid fa-check m-2"></i>${mealIngredient1}</li>
                        <li><i class="fa-solid fa-check m-2"></i>${mealIngredient2}</li>
                        <li><i class="fa-solid fa-check m-2"></i>${mealIngredient3}</li>
                        <li><i class="fa-solid fa-check m-2"></i>${mealIngredient4}</li>
                        <li><i class="fa-solid fa-check m-2"></i>${mealIngredient5}</li>
                        <li><i class="fa-solid fa-check m-2"></i>${mealIngredient6}</li>
                    </ul>
                </div>
            </div>
            </div> 
        `;
    foodContainer.appendChild(foodItem);
}


// const showModal = async (categoryName)=>{
//     const res = await fetch(`https://www.themealdb.com/api/json/v1/1/filter.php?c=${categoryName}`);
//     const data = await res.json();
//     const meals = data.meals
//     meals.forEach(meal =>{
//         console.log(meal);
//     })
    
    
// }