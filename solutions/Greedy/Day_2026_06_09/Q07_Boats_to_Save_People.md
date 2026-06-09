# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. The goal is to determine the minimum number of boats required to save all people, where each boat can hold at most two people and the total weight of the two people cannot exceed the limit of the boat. The weights of the people are distinct.

## Approach
The problem can be solved using a greedy approach by sorting the weights of the people in descending order and then assigning the heaviest people to boats first. This ensures that the minimum number of boats are used to save all people.

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
        // Sort the weights of the people in descending order
        sort(people.rbegin(), people.rend());
        
        int left = 0, right = people.size() - 1;
        int boats = 0;
        
        // Assign the heaviest people to boats first
        while (left <= right) {
            if (people[left] + people[right] <= limit) {
                // If the total weight does not exceed the limit, assign both people to the same boat
                right--;
            }
            // Increment the boat count and move to the next heaviest person
            boats++;
            left++;
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
- The greedy approach is used to solve the problem by assigning the heaviest people to boats first.
- The time complexity is O(n log n) due to the sorting operation.
- The space complexity is O(1) as no extra space is used.