const defultDataContainer = document.getElementById("data-container");
const searchBtn = document.getElementById("search-btn");
let isDefault = true;
const playerCount = document.getElementById("player-cnt");
let cnt = 0;

const searchOption = () =>{
    const searchValue = document.getElementById("search-value").value;
    
    isDefault = false;
    defaultDataLoad(searchValue,isDefault)
    document.getElementById("search-value").value = "";
    defultDataContainer.textContent = "";
}



const defaultDataLoad = async (searchValue,isDefault)=>{
    const res = await fetch(`https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p=${searchValue}`);
    const data = await res.json();
    const players = data.player
    if(players == null){
        alert("Please Insert A Valid Name")
    }
    else{
        defaultDataDisplay(players,isDefault);
    }
    // console.log(players,"fetch")
    
}
defaultDataLoad("",isDefault)


const defaultDataDisplay = (players,isDefault)=>{
    defultDataContainer.classList.add("p-2",);
    // console.log(players)
    if(isDefault){
        players = players.slice(0,12);
        // console.log("this is default value",isDefault);
    }
    players.forEach(player => {
        const dataItem = document.createElement("div");
        dataItem.classList.add("col-md-3","p-2")
        const playerDescription = player.strDescriptionEN?player.strDescriptionEN.slice(0,50):"No Data Found";
        const pName = player.strPlayer ?player.strPlayer:"No Name Found";
        const pNationality = player.strNationality?player.strNationality:"No Data Found";
        const pTeam = player.strTeam?player.strTeam:"No Data Found";
        const pSport = player.strSport?player.strSport:"No Data Found";
        const pId = player.idPlayer ? player.idPlayer : alert("User Id Not Found!! Please Try Again...")

        dataItem.innerHTML = `
        <div class="card">
            <img src="${player.strThumb ? player.strThumb:"https://st3.depositphotos.com/9998432/13335/v/450/depositphotos_133351928-stock-illustration-default-placeholder-man-and-woman.jpg"}" class="card-img-top" alt="...">
            <div class="card-body">
                <h4 class="card-title">${pName}</h4>
                <h6>Nationality: ${pNationality}</h6>
                <h6>Team: ${pTeam}</h6>
                <h6>Sport: ${pSport}</h6>
                <h6>Salary: ${player.strWage?player.strWage:"No Data Found"}</h6>
                <p class="card-text">${playerDescription}</p>
                <button onclick="viewDetails(${pId})" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                    Details
                </button>
                <button href="#" id="add-btn" class="btn btn-primary" onclick ="addPlayer('${pName}', '${pTeam}', '${pSport}',this)">Add Player</button>
            </div>
        </div>
        `;
        defultDataContainer.appendChild(dataItem);
        // console.log(player.strWage)
    });
}
let CNT = 0;
const addPlayer = (playerName,playerTeam,playerSport,button)=>{
    const accordionContainer = document.getElementById("acc-body");
    
    if(CNT < 11){
        CNT +=1;
        playerCount.innerText = `${cnt+=1}`
        const playerAddName = document.createElement("div");
        playerAddName.innerHTML = `
            <h4>${playerName}</h4>
                <h6>Team: ${playerTeam} </h6>
                <h6>Sport: ${playerSport}</h6>
        `;
        button.innerText ="Added";
        button.disabled = true;
        
        accordionContainer.appendChild(playerAddName)
    }
    else{
        alert("You Can't Add More Than 11")
    }
    
}



const viewDetails = async (userId)=>{

        const modalContainer = document.getElementById("moadal-container");
        const res = await fetch(`https://www.thesportsdb.com/api/v1/json/3/lookupplayer.php?id=${userId}`)
        const data = await res.json();
        const player = data.players[0];
        const playerDescription = player.strDescriptionEN?player.strDescriptionEN.slice(0,150):"No Data Found";
        const pName = player.strPlayer ?player.strPlayer:"No Name Found";
        const pNationality = player.strNationality?player.strNationality:"No Data Found";
        const pTeam = player.strTeam?player.strTeam:"No Data Found";
        const pSport = player.strSport?player.strSport:"No Data Found";
        console.log(player)
        const modalItem = document.createElement("div")
        modalItem.innerHTML = `
            <!-- Modal -->
            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered">
                    <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        
                    </div>
                    <div class="modal-body">
                    <div class="card">
                    <img src="${player.strThumb ? player.strThumb:"https://st3.depositphotos.com/9998432/13335/v/450/depositphotos_133351928-stock-illustration-default-placeholder-man-and-woman.jpg"}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h4 class="card-title">${pName}</h4>
                        <h6>Nationality: ${pNationality}</h6>
                        <h6>Team: ${pTeam}</h6>
                        <h6>Sport: ${pSport}</h6>
                        <h6>Salary: ${player.strWage?player.strWage:"No Data Found"}</h6>
                        <p class="card-text">${playerDescription}</p>
                    </div>
                </div>
                    </div>
                    
                    </div>
                </div>
            </div>
        `
        modalContainer.appendChild(modalItem);
    

    
    console.log(userId);
}
