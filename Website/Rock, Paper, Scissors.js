botMove = ""
let playerMove = null
let result = ""
let playerScore = 0
let botScore = 0


function botTurn() {
    const botAnswers = ["rock", "paper", "scissors"]
    let position = Math.floor(Math.random() * 3);
    botMove = botAnswers[position]
}

function myFunction(t1) {
    playerMove = t1
}

function startGame() {
    
    if (playerMove == null){
        alert("Please select a move before playing!")
    } else{
        botTurn()

        if (botMove == playerMove) {
        result = "Drew"
        } else if (botMove == "rock" && playerMove == "paper"){
        result = "Win"
        } else if (botMove == "paper" && playerMove == "scissors"){
        result = "Win"
        } else if (botMove == "scissors" && playerMove == "rock"){
        result = "Win"
        } else{
        result = "Lose"
        }


        if (result == "Win") {
            playerScore = playerScore + 1
        } else if (result == "Lose"){
            botScore = botScore + 1
        }

        document.getElementById("playerScore").innerText = playerScore
        document.getElementById("botScore").innerText = botScore

        alert("The bot went " + botMove + " and you went " + playerMove + " so you " + result) 
    }

}
