# Basketball Movement Clustering – Eclipse Analytics Submission

Dhruv Sood
A18321957
d2sood@ucsd.edu

This is my submission for the Eclipse Basketball Consulting Challenge.

## What I Did

I worked with SportVU tracking data from the Raptors vs Hornets game (Jan 1, 2016).  
The dataset tracks every player and the ball at 25 frames per second.

I pulled a few possessions, took the player positions frame-by-frame, and used KMeans clustering to group different types of movement. Then I added the ball's path on top in red to give context.

## What the Plot Shows

- Clusters of player movement — likely showing roles like cutters, perimeter players, or help defense
- The red line is the ball's movement during the possession
- Helps show spacing and how players move relative to the ball

## File

- `player_movement_clustering.ipynb` – code + plot + explanation all in one

## Notes

Focused on making the visualization clean and intuitive. Code is in Colab and uses Python basics (no advanced packages).
