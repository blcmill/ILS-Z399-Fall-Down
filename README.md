# Fall-Down
This is a draft for our game jam game. Our game theme is "Black and White."

For our game, you play as a ball and have to fall down a sort of maze.  The game scrolls upward and you have to avoid getting stuck at the top of the frame.

We created a level generator python file that creates random, downward-scrolling levels.

---

As of now, there are a few to-dos.

In level-generator.py:
* Add walls to the sides of the levels; this is necessary in order to prevent the player from going out of bounds off the sides. To do this, we can do modulo division within the inner for loop and check to see if y is equal to width - 1 or zero and in that case write a "1" to the text_file.
* Make the holes wider. My current solution for making holes makes them one unit wide, but it would be good if we replaced two or three blocks with an empty space instead of one. This algorithm will probably be a little more complex than the wall-adding one.

In game.py:
* Add a win condition. My code has the player dying when they contact an enemy. We can change this to make the win condition when the player touches an "enemy" which could be replaced with a goal-post.  We can add a line in level-generator to create an enmy in the final line to make the win condition when the player reaches the bottom.
* Add graphics. Hank sent me a nice graphic of a ball which could be used for the player, which I will add to this repo.  It would also be nice if we could fill the background with an image of black text on a white background, as our original theme was going to be the player falling through text. It would be cool if we could get the platforms to be text instead, but that might be too complex.
* Add music. Anyone with music can add it to the project as long as it isn't distracting.
* Trigger player death when they reach the top of the frame. I don't think this is happening right now but it definitely should.

---

Most of these to-dos can be done pretty simply or during class, so don't stress out too much. This should be fun! (-:
