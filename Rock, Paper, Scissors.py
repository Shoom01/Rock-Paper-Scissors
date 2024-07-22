import random

def get_bot_choice():
    BotAnswers = ['Rock', 'Paper', 'Scissors']
    Position = random.randint(0, 2)
    BotAnswer = BotAnswers[Position]
    print('Bot has made its decision')
    return BotAnswer


def get_player_choice():
    print("Rock, Paper or Scissors: ")
    PlayerResult = '0'
    PlayerAnswer = input().lower()
    while PlayerAnswer not in ['rock', 'paper', 'scissors']:
        print("Please choose Rock, Paper or Scissors")
    return PlayerAnswer

def get_result(BotAnswer, PlayerAnswer):
    if BotAnswer == 'Rock': 
        if PlayerAnswer == 'paper':
            PlayerResult = 1
        elif PlayerAnswer == 'rock':
            PlayerResult = 2
        else :
            PlayerResult = 3

    elif BotAnswer == 'Paper' and PlayerAnswer == 'rock':
        PlayerResult = 3
    elif BotAnswer == 'Paper' and PlayerAnswer == 'scissors':
        PlayerResult = 1
    elif BotAnswer == 'Paper' and PlayerAnswer == 'paper':
        PlayerResult = 2

    elif BotAnswer == 'Scissors' and PlayerAnswer == 'rock':
        PlayerResult = 1
    elif BotAnswer == 'Scissors' and PlayerAnswer == 'scissors':
        PlayerResult = 2
    elif BotAnswer == 'Scissors' and PlayerAnswer == 'paper':
        PlayerResult = 3
    return PlayerResult

def get_outcome(PlayerResult):
    if PlayerResult == 1:
        Outcome = 'Win'
    elif PlayerResult == 2:
        Outcome = 'Draw'
    elif PlayerResult == 3:
        Outcome = 'Loss'
    print('The game was a', Outcome, 'as the bot went', BotAnswer)

if __name__ == __main__:
    BotAnswer = get_bot_choice()
    PlayerAnswer = get_player_choice()
    PlayerResult = get_result(BotAnswer, PlayerAnswer)
    get_outcome(PlayerResult)


