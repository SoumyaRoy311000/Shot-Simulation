# What This Code Does

This set of python script helps you visualise how fowards in the top 5 league for a particular season have scored goals with respect to how much was expected of them, by running a Monte Carlo simulation for 10,000 iterations of all the shots they took that season based on xG.

It also provides with a percentile ranking of the actual value of the goal scored compared to the most frequent outcome from the simulation.

# Requirements

To install the required dependencies run the following in terminal: `pip install -r requirements.txt`

# Running The Code

## Step 1:

Run the PlayerFinder.py script to generate the latest PlayerIDs.csv : `python -u PlayerFinder.py`

## Step 2:

After PlayerIDs.csv is generated, run the ShotSimulator.py script to search for the Player of your choice: `python -u ShotSimulator.py`

When asked for the seaon, choose the starting year. For eg. if you want for the 2021-22 season, enter 2021.

## Please Note:

Step 1 is not required as PlayerIds.csv is already provided.
You may have to generate one after transfer windows to account for all the player transfers.
