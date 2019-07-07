An implementation of CFB Success Rate for College Basketball.  Will be using Beautiful Soup on sports-reference.com.  Unlike college football, where you have to calculate success rate by traversing through play-by-play data for games, we can determine success rate just looking at available box scroes.


A play is determined to be successful in the following situations.
A field goal is made (both 2 and 3 pointers).
The defense gives up a foul.

A play is determiend to be unsuccessful in the following situations.
A missed field goal attempt (both 2 and 3 pointers)
The ball is stolen
Turnovers, where the following is recorded as a turnover.
-Offensive Fouls
-Out of bounds
-mismanaged handling
