# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. Each boat can carry at most two people, and the sum of their weights cannot exceed the limit. The goal is to determine the minimum number of boats required to save all people. The weights of the people are non-negative integers, and the limit of each boat is a positive integer.

## Approach
The problem can be solved by sorting the weights in descending order and using a two-pointer technique to assign people to boats. The idea is to assign the heaviest person to a boat and then try to assign the lightest person to the same boat if possible.

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
        // Sort the weights in descending order
        sort(people.rbegin(), people.rend());
        
        // Initialize two pointers, one at the start and one at the end
        int left = 0, right = people.size() - 1;
        
        // Initialize the count of boats
        int boats = 0;
        
        // Iterate until the two pointers meet
        while (left <= right) {
            // If the heaviest person can be assigned to a boat with the lightest person
            if (people[left] + people[right] <= limit) {
                // Move the right pointer to the next person
                right--;
            }
            // Move the left pointer to the next person
            left++;
            // Increment the count of boats
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
Input: people = [3,5,3,4], limit = 5
Output: 4
```

## Key Takeaways
- Sort the weights in descending order to prioritize the heaviest people.
- Use a two-pointer technique to assign people to boats efficiently.
- The time complexity is O(n log n) due to the sorting operation.