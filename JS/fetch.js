fetch("www.themealdb.com/api/json/v1/1/random.php")
.then(res =>res.json())
.then(data =>{
    console.log(data);

})
