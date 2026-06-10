# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people who need to be saved, and an integer representing the limit of each boat. Each boat can hold at most two people, and the sum of their weights cannot exceed the limit. The goal is to determine the minimum number of boats required to save all people.

## Approach
The problem can be solved using a greedy algorithm by sorting the people by their weights and then iterating over the sorted list, assigning the heaviest people to boats first. This approach ensures that the minimum number of boats is used.

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
        // Sort the people by their weights
        sort(people.begin(), people.end());
        
        // Initialize two pointers, one at the start and one at the end of the list
        int left = 0, right = people.size() - 1;
        
        // Initialize the count of boats
        int boats = 0;
        
        // Iterate over the list until the two pointers meet
        while (left <= right) {
            // If the heaviest person can be paired with the lightest person, do so
            if (people[left] + people[right] <= limit) {
                left++;
            }
            // Move the heaviest person to a boat
            right--;
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
```

## Key Takeaways
- Sort the people by their weights to ensure the heaviest people are assigned to boats first.
- Use two pointers to iterate over the sorted list, assigning people to boats based on their weights.
- The greedy algorithm ensures the minimum number of boats is used by always assigning the heaviest person to a boat.