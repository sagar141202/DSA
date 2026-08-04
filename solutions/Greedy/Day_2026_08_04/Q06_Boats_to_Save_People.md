# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. The goal is to determine the minimum number of boats required to save all people, where each boat can hold a maximum weight of limit. The people can be divided into boats in any order, but the total weight of people in each boat should not exceed the limit.

## Approach
The approach is to use a two-pointer technique, sorting the people by their weights in descending order. We then try to put the heaviest person with the lightest person in the same boat, and if the total weight exceeds the limit, we put the heaviest person in a separate boat.

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
        // Sort the people by their weights in descending order
        sort(people.rbegin(), people.rend());
        
        int left = 0, right = people.size() - 1;
        int boats = 0;
        
        // Try to put the heaviest person with the lightest person in the same boat
        while (left <= right) {
            if (people[left] + people[right] <= limit) {
                // If the total weight does not exceed the limit, move both pointers
                left++;
                right--;
            } else {
                // If the total weight exceeds the limit, move only the left pointer
                left++;
            }
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
- Sort the people by their weights in descending order to maximize the chance of putting two people in the same boat.
- Use a two-pointer technique to try to put the heaviest person with the lightest person in the same boat.
- If the total weight exceeds the limit, put the heaviest person in a separate boat.