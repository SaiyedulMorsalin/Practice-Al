const showPage = async (mealId,mealName) =>{
//     // console.log(typeof mealId,mealId)
//     const res = await fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${mealId}`);
//     const data = await res.json();
//     const meal = data.meals;
//     console.log("meal search by id",meal);
//     const foodContainer = document.getElementById("food-container");
//     foodContainer.textContent = "";
//     const banner = document.getElementById("banner");
//     banner.textContent = "";
//     foodContainer.innerHTML=`<h2 class="text-center mb-3">${mealName}</h2>`;
//     const foodItem = document.createElement("div");
//     foodItem.classList.add("col-md-8","c","col-sm-3");
//     const noMealIngredient = "Unknown Ingredient";
//     const mealIngredient1 = meal[0].strIngredient1? meal[0].strIngredient1.slice(0,10):noMealIngredient;
//     const mealIngredient2 = meal[0].strIngredient2? meal[0].strIngredient2.slice(0,10):noMealIngredient;
//     const mealIngredient3 = meal[0].strIngredient3? meal[0].strIngredient3.slice(0,10):noMealIngredient;
//     const mealIngredient4 = meal[0].strIngredient4? meal[0].strIngredient4.slice(0,10):noMealIngredient;
//     const mealIngredient5 = meal[0].strIngredient5? meal[0].strIngredient5.slice(0,10):noMealIngredient;
//     const mealIngredient6 = meal[0].strIngredient6? meal[0].strIngredient6.slice(0,10):noMealIngredient;
//     foodItem.innerHTML = `
//             <div class="card ">
//             <img src="${meal[0].strMealThumb}" class="card-img-top" alt="...">
//             <div class="card-body">
//                 <h5 class="card-title mb-3 intgredient ">Ingredients:</h5>
//                 <div class="list">
//                     <ul class="list-container">
//                         <li><i class="fa-solid fa-check m-2"></i>${mealIngredient1}</li>
//                         <li><i class="fa-solid fa-check m-2"></i>${mealIngredient2}</li>
//                         <li><i class="fa-solid fa-check m-2"></i>${mealIngredient3}</li>
//                         <li><i class="fa-solid fa-check m-2"></i>${mealIngredient4}</li>
//                         <li><i class="fa-solid fa-check m-2"></i>${mealIngredient5}</li>
//                         <li><i class="fa-solid fa-check m-2"></i>${mealIngredient6}</li>
//                     </ul>
//                 </div>
//             </div>
//             </div> 
//         `;
//     foodContainer.appendChild(foodItem);
// }