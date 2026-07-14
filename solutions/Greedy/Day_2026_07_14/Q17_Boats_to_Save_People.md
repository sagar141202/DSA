# Boats to Save People

## Problem Statement
We have a certain number of people that need to be saved, and we have a certain number of boats with limited capacity. Each person has a specific weight, and each boat has a specific capacity. We need to determine the minimum number of boats required to save all the people. The constraint is that we can't put more people in a boat than its capacity, and we can't put a person in a boat if their weight exceeds the boat's capacity.

## Approach
The approach is to sort the people by their weights in descending order and the boats by their capacities in descending order. Then, we use a two-pointer technique to assign people to boats, starting with the heaviest person and the boat with the largest capacity.

## Complexity
- Time: O(n log n + m log m)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        // Sort people by weight in descending order
        sort(people.rbegin(), people.rend());
        
        // Initialize two pointers, one at the start and one at the end
        int left = 0, right = people.size() - 1;
        int boats = 0;
        
        // Assign people to boats using two-pointer technique
        while (left <= right) {
            // If the heaviest person can be put in the same boat as the lightest person, do so
            if (people[left] + people[right] <= limit) {
                right--;
            }
            // Move to the next boat
            left++;
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
- Sort the people and boats by their weights and capacities in descending order to maximize the number of people that can be put in each boat.
- Use a two-pointer technique to assign people to boats, starting with the heaviest person and the boat with the largest capacity.
- This greedy approach ensures that we use the minimum number of boats required to save all the people.