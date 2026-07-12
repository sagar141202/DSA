# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. The goal is to determine the minimum number of boats required to save all people. Each boat can carry a maximum weight equal to the limit. The problem can be solved using a greedy approach, where we sort the weights of people in descending order and then try to fill each boat with the heaviest people first.

## Approach
The algorithm sorts the weights in descending order, then iterates through the weights, assigning each person to a boat. If a boat is full, a new boat is added. The greedy approach ensures the minimum number of boats are used.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int numRescueBoats(vector<int>& people, int limit) {
    // Sort the weights in descending order
    sort(people.rbegin(), people.rend());
    int light = people.size() - 1;
    int heavy = 0;
    int boats = 0;
    
    // Iterate through the weights, assigning each person to a boat
    while (light >= heavy) {
        if (people[heavy] + people[light] <= limit) {
            light--;
        }
        heavy++;
        boats++;
    }
    
    return boats;
}
```

## Test Cases
```
Input: people = [1,2], limit = 3
Output: 1
Input: people = [3,2,2,1], limit = 3
Output: 3
```

## Key Takeaways
- Sort the weights in descending order to prioritize the heaviest people.
- Use a two-pointer approach to assign people to boats efficiently.
- The greedy approach ensures the minimum number of boats are used by filling each boat with the heaviest people first.