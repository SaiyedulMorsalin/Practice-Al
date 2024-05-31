const defaultDataContainer = document.getElementById("data-container");
const searchBtn = document.getElementById("search-btn");
let isDefault = true;
const playerCount = document.getElementById("player-cnt");
let cnt = 0;

searchBtn.addEventListener('click', () => {
    const searchValue = document.getElementById("search-value").value;
    isDefault = false;
    defaultDataLoad(searchValue, isDefault);
    document.getElementById("search-value").value = "";
    defaultDataContainer.textContent = "";
});

const defaultDataLoad = async (searchValue, isDefault) => {
    const res = await fetch(`https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p=${searchValue}`);
    const data = await res.json();
    const players = data.player;
    if (players == null) {
        alert("Please Insert A Valid Name");
    } else {
        defaultDataDisplay(players, isDefault);
    }
};

defaultDataLoad("", isDefault);

const defaultDataDisplay = (players, isDefault) => {
    defaultDataContainer.classList.add("p-2");
    if (isDefault) {
        players = players.slice(0, 12);
    }
    players.forEach(player => {
        const dataItem = document.createElement("div");
        dataItem.classList.add("col-md-3", "p-2");
        const playerDescription = player.strDescriptionEN ? player.strDescriptionEN.slice(0, 50) : "No Data Found";
        const pName = player.strPlayer ? player.strPlayer : "No Name Found";
        const pNationality = player.strNationality ? player.strNationality : "No Data Found";
        const pTeam = player.strTeam ? player.strTeam : "No Data Found";
        const pSport = player.strSport ? player.strSport : "No Data Found";
        const pId = player.idPlayer ? player.idPlayer : alert("User Id Not Found!! Please Try Again...");

        dataItem.innerHTML = `
        <div class="card">
            <img src="${player.strThumb ? player.strThumb : "https://st3.depositphotos.com/9998432/13335/v/450/depositphotos_133351928-stock-illustration-default-placeholder-man-and-woman.jpg"}" class="card-img-top" alt="...">
            <div class="card-body">
                <h4 class="card-title">${pName}</h4>
                <h6>Nationality: ${pNationality}</h6>
                <h6>Team: ${pTeam}</h6>
                <h6>Sport: ${pSport}</h6>
                <h6>Salary: ${player.strWage ? player.strWage : "No Data Found"}</h6>
                <p class="card-text">${playerDescription}</p>
                <button onclick="viewDetails(${pId},'${pName}')" type="button" class="btn btn-primary">
                    Details
                </button>
                <button id="add-btn" class="btn btn-primary" onclick="addPlayer('${pName}', '${pTeam}', '${pSport}', this)">Add Player</button>
            </div>
        </div>
        `;
        defaultDataContainer.appendChild(dataItem);
    });
}

let CNT = 0;
const addPlayer = (playerName, playerTeam, playerSport, button) => {
    const accordionContainer = document.getElementById("acc-body");

    if (CNT < 11) {
        CNT += 1;
        playerCount.innerText = `${cnt += 1}`;
        const playerAddName = document.createElement("div");
        playerAddName.innerHTML = `
            <h4>${playerName}</h4>
            <h6>Team: ${playerTeam}</h6>
            <h6>Sport: ${playerSport}</h6>
        `;
        button.innerText = "Added";
        button.style.color = "black"
        button.disabled = true;

        accordionContainer.appendChild(playerAddName);
    } else {
        alert("You Can't Add More Than 11");
    }
}

const viewDetails = async (pId,pName)=>{
    
    const res = await fetch(`https://www.thesportsdb.com/api/v1/json/3/lookupplayer.php?id=${pId}`);
    let data = await res.json();
    const player = data.players[0];
    // showModalDetails(player)
    showPhoneDetails(player)
    
}

const showPhoneDetails = (player) => {
    console.log(player);
    const pName = document.getElementById('show-detail-name');
    pName.innerText = player.strPlayer ? player.strPlayer : "No Name Found";
    const pDescription = player.strDescriptionEN ? player.strDescriptionEN.slice(0, 250) : "No Data Found";
    const pNationality = player.strNationality ? player.strNationality : "No Data Found";
    const pTeam = player.strTeam ? player.strTeam : "No Data Found";
    const pSport = player.strSport ? player.strSport : "No Data Found";
    const pImage = player.strThumb ? player.strThumb : "https://st3.depositphotos.com/9998432/13335/v/450/depositphotos_133351928-stock-illustration-default-placeholder-man-and-woman.jpg";
    const showDetailContainer = document.getElementById('show-detail-container');

    showDetailContainer.innerHTML = `
        <img src="${pImage}" alt="" />
        <h6 class="mt-2">Nationality: ${pNationality}</h6>
        <h6>Team: ${pTeam}</h6>
        <h6>Sport: ${pSport}</h6>
        <h6>Salary: ${player.strWage ? player.strWage : "No Data Found"}</h6>
        <p class="card-text py-2">${pDescription}</p>
    `
    show_details_modal.showModal();
}