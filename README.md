# CowsAndBulls_game_python

<h1> Cows and Bulls </h1>
<h2>Point to remember</h2>
<ul>
    <li>generated number each digit is different</li>
</ul>
<h3>Working of game</h3>
<ol>
    <li>A random 4-digit number will be generated, player need to guess the random number with in his specified attempts</li>
    <li>if the player guessed 4-digit number and random generated number has same number in same position then it is cow, if the same number present but in different position it's bull<li>
    <li>if player guessed number doesnt match with any number of the randomly generated number then it's Bullshit</li>
    <li>Player will win the game if he find the random generated number exactly, need to match each number position also (mean cow need to be 4).
</ol>
<h3> Example</h3>
<p>if random number = 1345 and player_guess = 1469 here "1" is guesses by player in its correct position so cow, and "4" guessed by player is in random number but in different position so bull, "6" and "9"not there at all so no change in bull and cow.</p>
<p> At final, player gets 1 bull, 1 cow message for his guess number</p>
