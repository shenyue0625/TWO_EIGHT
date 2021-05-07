# Two_Eight_Card_Game

----Abstract:

This is a card game called Two Eight, which allows 4 players (include dealer) to play in one round. Each player holds 2 and cards and the players with higher points than the dealer wins the game. There is s a special calculation rule for the player who gets cards 2 and 8, that's where the game’s name is derived from. The detailed rules are defined below. This game can be used for gambling or for fun.



----Detailed instructions:

1.	This is a card game using only 40 number cards.  No face cards, like J,Q,K.
2.	There are four players.  One of the players is the dealer.  The dealer compares his/her points with each of the other three players.  Players play and bet against the dealer, not against each other.
3.	Each hand holds two cards, which is randomly dealt. Matching pairs have the highest value, with 10+10 being the highest to A+A as the lowest.  Unpaired hands are the sum of their values, minus ten for any value ten or greater.  So, 8+5=13 and 13-10=3 points.  Also, 7+3=10 and 10-10=0.  And 2+5=7 (no “minus ten” since 7<10).  The exception for Unpaired hands are 2+8, which beats all other unpaired hands but loses to all matching pairs.  (The “minus ten” rule does not apply to 2+8 hands.)
4.	The order of greatness of the hands is: 10+10; 9+9; ...; 1+1; 2+8; then 9 points... 1 point; 0 point.  Players calculate winning points themselves.
5.	Betting:  Stakes can be put hierarchically from rank 1 to rank 20. 0 to 7 points cover only stake in rank 1. 8 points cover rank 1 and 2. 9 points cover rank 1,2,3. hand 2+8 cover rank 1 to 4; hand 1+1 cover 11 ranks, from rank 1 to 11. So on and so forth, hand 9+9 cover 19 ranks, hand 10+10 cover 20 ranks.  Betting and drinking are done by players in real life, outside the program.
6.	You can use this game for gambling; also you can use it for fun.
7.	Please run gui_2_8.py to get a GUI then hit deal card button to deal cards for four players.
8.	The author of this game is Xu Yang. All rights reserved. You cannot spread this game without the permission of author.



----Project organization:

This repository contains 6 python files, 40 card pictures and 1 readme file. You can go to TWO_EIGHT folder to find them, and you can find the main python files at the bottom of the folder. There are 3 classes in our project, which are Card, Hand and Deck. The str_real_card.py file is to convert string card to real card picture, and it works with gui_2_8.py file to simulate a graphic user interface for players. The test_two_eight.py file contains several test cases in order to meet project requirements.



----Program operation: 

Please clone this repository and start your python IDE. Then run gui_2_8.py to get a GUI, then hit deal card button to deal cards for four players.



----User Stories:

1.	As a player, I want to test how lucky I am by play a game so I can be a better player.
2.	As a player, I want to change my player identity between player and dealer so I can experience different roles.
3.	As a player, I want the system can simulate a square game table so I can simulate a real table.
4.	As a player, I want the system to distribute one player's cards on one side of the table so I can clearly see each player’s cards.
5.	As a player, I want to get two cards at one round so I can play eight-two.
6.	As a player, I want to bet on my stake so I can practice betting.
7.	As a player, I want to bet any number of ranks that I want so I can improve my betting.
8.	As a player, I want to compare my cards counts with dealer so I can learn the game better.
9.	As a player, I want the system to show all players' cards when we compare counts so I can see other players’ hands.
10.	As a player, I want the system can determine whether I win the game so I can learn the rules.
11.	As a player, I want the system to calculate how many stakes that I win or lose so I can learn betting rules..
12.	As a player, I want the system to calculate which player won the biggest bet, so I do not get in arguments with my friends.
13.	As a player, I want the system to calculate which player lost the most bet so that I can gloat.
14.	As a player, I want the system to collect all dealt cards after the game ends so that the next round can be played.
15.	As a player, I want the system to shuffle all cards before the next round starts so that cards are random.
