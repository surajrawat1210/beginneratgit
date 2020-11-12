'''
The Minion Game
Kevin and Stuart want to play the 'The Minion Game'.
Game Rules
Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
Scoring
A player gets +1 point for each occurrence of the substring in the string .

'''
def minion_game(s):
    S_length = len(s)
    player1, player2 = 0, 0

    for i in range(S_length):
        if s[i] in "AEIOU":
            player1 += S_length - i
        else:
            player2 += S_length - i

    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart", player2)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)