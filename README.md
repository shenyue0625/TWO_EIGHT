# Two_Eight_Card_Game
  
1. This is a card game using only 40 number cards.No face cards,like J,Q,K.
2. Four players, one of them is gam dealer.Game dealer compare his/her point with the other three players.
3. Each hand holds two cards, which is dealt using random method. 
   The value of the hand is the sum of the two numbers of the cards, except same rank hands and 2 & 8 hand.
   If the value is greater than 10, then the point is sum minus 10,like 8+5 is 3 points, 4+6 (3+7;1+9) is 0.
4. The order of greatness of the hands is: 10+10;9+9; ... ;1+1; 2+8; then 9 points;...1 point; 0 point.
5. Stake can be put hierachically from rank 1 to rank 20. 0 to 7 points cover only stake in rank 1. 8 points cover
   rank 1 and 2. 9 points cover rank 1,2,3. hand 2+8 cover rank 1 to 4; hand 1+1 cover 11 ranks, from rank 1 to 11.
   So on and so fforth, hand 9+9 cover 19 ranks, hand 10+10 cover 20 ranks.
6. You can use this game for gambling, also you can use it for fun.
7. Please run gui_2_8.py to get a GUI then hit deal card button to deal cards for four players.
8. The author of this game is Xu Yang. All rights researved. You can not spread this game without the permission of author. 


--User Stories:

1. As a player, I want to test how lucky I am by play a game.
2. As a player, I want to change my player identity between player and dealer.
3. As a player, I want the system can simulate the a square game table.
4. As a player, I want the system to distribute one player's cards on one side of the table.
5. As a player, I want to get two cards at one round.
6. As a player, I want to bet on my stake.
7. As a player, I want to bet any number of ranks that I want.
8. As a player, I want to compare my cards counts with dealer.
9. As a player, I want the system to show all players' cards when we compare counts.
10. As a player, I want the system can determine whether I win the game.
11. As a player, I want the system to calculate how many stake that I win or loose.
12. As a player, I want the system to calculate which player win the most bet.
13. As a player, I want the system to calculate which player loose the most bet.
14. As a player, I want the system to collect all dealt cards after the game ends.
15. As a player, I want the system to shuffle all cards before the next round starts.
