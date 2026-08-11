# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. The goal is to determine the minimum number of boats required to save all people, with each boat able to carry a maximum weight of limit. The people can be divided into boats in any order, but the weight of each boat must not exceed the limit.

## Approach
The greedy approach involves sorting the weights of people in descending order and then assigning the heaviest people to boats first. This ensures that the minimum number of boats are used, as the heaviest people are assigned to boats before the lighter ones.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.rbegin(), people.rend());
        int light = people.size() - 1, heavy = 0;
        int boats = 0;
        while (light >= heavy) {
            if (people[heavy] + people[light] <= limit) {
                light--;
            }
            heavy++;
            boats++;
        }
        return boats;
    }
};
```

## Test Cases
```
Input: people = [1,2], limit = 3
Output: 1
Input: people = [3,2,2,1], limit = 3
Output: 3
```

## Key Takeaways
- Sorting the weights of people in descending order allows us to assign the heaviest people to boats first, minimizing the number of boats required.
- Using two pointers, one at the start and one at the end of the sorted array, enables us to efficiently assign people to boats.
- The time complexity of O(n log n) is due to the sorting operation, while the space complexity of O(1) is because we only use a constant amount of space to store the pointers and the count of boats.