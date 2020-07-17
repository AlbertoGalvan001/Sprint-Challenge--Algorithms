#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) The while loop is dependent on the size of n, this would be Linear 0(n).

b) The for loop will run through the size of n 0(n), but the while loop will run through half, so it's quasilinear 0(n log n)

c) The function will run n times, returning the sum of the number of bunny ears for n bunnies, so it's also Linear 0(n)

## Exercise II

Something like a binary search tree except when it returns false(egg didn't break), then it jumps up by 1 level until it reaches the highest point the egg did not break.

1. Find the middle floor of the building and drop the egg from that point. If it breaks, ignore all the floors above and proceed to the half of the bottom floors, till it finds False(the egg didn't break).

2. Once that is found, set the max_floor(temp value) to be that one level and jump up to the next floor.

3. For each floor the new egg is dropped from, set the temp value to that floor until the egg finally breaks.

4. Return that temp value, which should be the floor below the one where it broke.
