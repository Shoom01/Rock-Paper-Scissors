botMove = ""
let playerMove = ""
let result = ""

function botMove() {
    const botAnswers = ["rock", "paper", "scissors"]
    let position = Math.floor(Math.random() * 3);
    botMove = botAnswers[position]
}

function myFunction(t1) {
    playerMove = t1
}

function startGame() {
    if (botMove == playerMove) {
        result = "Draw"
    } else if (botMove == "rock" && playerMove == "paper"){
        result = "Win"
    } else if (botMove == "paper" && playerMove == "scissors"){
        result = "Win"
    } else if (botMove == "scissors" && playerMove == "rock"){
        result = "Win"
    } else{
        result = "Lose"
    }
    alert(result) 
}

// function callBoth(){
//     botMove()
//     startGame()
// }


// Scoreboard
// Input validation
// Make is look good
// Swap between 3 pictures (RPS) then have result in the middle with each move on sides (maybe)