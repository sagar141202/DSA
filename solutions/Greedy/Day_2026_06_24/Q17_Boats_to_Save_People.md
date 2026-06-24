# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. The goal is to determine the minimum number of boats required to save all people, with each boat able to hold a maximum weight of limit. The people can be divided into boats in any order, but the total weight of people in each boat cannot exceed the limit.

## Approach
The approach is to sort the people by their weights in descending order and then use a two-pointer technique to assign people to boats. We start by assigning the heaviest person to a boat and then try to assign the lightest person to the same boat if possible.

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
        // Sort people by their weights in descending order
        sort(people.rbegin(), people.rend());
        
        int count = 0;
        int left = 0, right = people.size() - 1;
        
        // Assign people to boats
        while (left <= right) {
            // If the heaviest person can be assigned to the same boat as the lightest person
            if (people[left] + people[right] <= limit) {
                right--;
            }
            // Increment the boat count and move to the next heaviest person
            count++;
            left++;
        }
        
        return count;
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
- Sort the people by their weights in descending order to prioritize the heaviest people.
- Use a two-pointer technique to assign people to boats, starting with the heaviest person and trying to assign the lightest person to the same boat if possible.
- The time complexity is O(n log n) due to the sorting, and the space complexity is O(1) since we only use a constant amount of space.