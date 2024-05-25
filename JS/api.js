// API -->Application Programming Interface.
//objects-->

// const user = {
//     id:1,
//     name:"sagir",
//     title:"munsi",
//     job:'Moulovi'
// };

// console.log(JSON.stringify(user));
// // console.log(JSON.parse(user))
// console.log(user);



const shop ={
    owner:"Alia",
    address:{
        street:"Khocukhet",
        city:"Rang",
        country:"BD"
    },
    products:["Laptop","mic","monitor","keyboard"],
    revenue:60000,
    isOpen:true,
    isNew:false
}
console.log(shop);
const shopJSON = JSON.stringify(shop);
console.log(shopJSON);