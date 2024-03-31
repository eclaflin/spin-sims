# Overview

- Roulette table is arranged in 2 sections: inside and outside
  - Inside area contains the 36 numbered squares, each either red or black
  - Outside area contains boxes that cover a broader range of numbers (e.g. odd or even)
  - At the top of the table, there are zero or double-zero boxes 

![alt text](img/table_anatomy.png)

- Each square of the board (including zero/double-zero) are referred to as "pockets"
  - So in the American roulette board (i.e. with a double-zero), there are 38 pockets (36 numbered plus two "zero" pockets)
- The inside board can be further divided to represent combinations of pockets that correspond to different bet types, according to:

| Grouping | Description                                              |
| -------- | -------------------------------------------------------- |
| Split    | 2 numbers, either from adjacent rows or adjacent columns |
| Street   | 3 numbers, corresponding to a complete row of the table  |
| Corner   | 4 numbers, as formed by a 2x2 matrix of pockets          |
| Six Line | 6 numbers, as formed by combining 2 adjacent streets     |
| Top Line | 5 numbers, as formed by combining the first two rows (i.e. the "zero" row and adjacent) | 

# Grid Implementation

From this understanding of the board and possible coverages of multiple pockets, we can start to form a coordinate-grid to represent every space on the table that a bet can "occupy" (i.e. every option that a player can select).

![alt text](img/table_grid.png)

This creates a grid that is 11 rows by 27 columns (rows and columns assume the table is oriented "east-west", with zero/double-zero positioned on the left side of the frame)

However, within this xy coordinate-grid, not every coordinate will represent a valid position.  In fact, according to the rules there will only be a total of 170 valid inputs

![alt text](img/table_grid_valid.png)

Based on this, we can say that each grid coordinate has a number of properties, including:
- Inside or outside
- Pocket(s) covered
  - Can be one or many
- Grouping
  - as noted above this can include split, street, corner etc.
  - These map (1-1???) to payouts
- Payout odds 

For the purposes of a UI, we would also say that a coordinate "object" would also need to serve as a "container" for that may or may not hold a users' bet 

So assuming a east-west = x and north-south=y, ascending numbering scheme like this:

![alt text](img/table_grid_valid_numbered.png)

We could show = the coordinate (4,7) as 

| Inside Outside? | Pockets | Grouping | Payout Odds | 
| --------------- | ------- | -------- | ----------- |
| Inside | [1,2,3,4,5,6] | Six-Line | 5:1 |

# Pockets

In order to instantiate the coordinate grid, we may want to start by defining the concept of a "pocket".  Reason being is that a pocket is 1-1 with a result of a spin, whereas the nature of multi-pocket betting options means that a coordinate could be  one-to-many with the actual result of a spin.

Potential attributes of a pocket then could be:
- Corresponding number of wheel
- Color
- Even or odd 
- Dozen
- Hi or low 

So for example attributes of the 13 pocket could look like:

| Number | Color | Even-Odd | Dozen | Hi-Lo | 
| ------ | ----- | -------- | ----- | ----- |
| 13 | Black | Odd | 2nd 12 | Hi | 

With this scheme, "outside" pockets could be said to represent a list of numbers, but would not be specific to color, Additionally, they would only be specific to even-odd, dozen, or hi-lo if they are in fact those specific pockets (i.e. they are 1 to zero or one with even-odd, dozen, and hi-lo).

Based on this, a potential class-based approach to pockets could be:

- Parent class `Pocket`
  - `NumberedPocket` inherits from `Pocket`
  - `OutsidePocket` inherits from `Pocket`

Based on on the one to zero or many relationship of pocket to winning result, a different approach may be to have separate *methods* between outside and inside pockets in order to calculate whether the result of a spin corresponds to a "win" for a given pocket

In theory, this would make outside pockets more reusable because of the inherent *inability* to split/line-bet outside pockets.

So actually, you could have:

- Parent class `Pocket`, which has a grid position attribute corresponding to the "central" grid coordinate for the pocket
  - Child class `InsidePocket`, which is one-to-one with a number result of a spin 
  - Child class `OutsidePocket`, which is one-to-many with a number result of a spin 




