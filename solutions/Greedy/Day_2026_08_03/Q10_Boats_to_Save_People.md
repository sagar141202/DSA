# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. The goal is to determine the minimum number of boats required to save all people. Each boat can carry a maximum weight equal to the limit. The problem can be solved using a greedy approach by sorting the weights of people in descending order and then assigning them to boats.

## Approach
The algorithm sorts the weights in descending order, then iterates through the weights, assigning each person to the first boat that has enough capacity. If no boat has enough capacity, a new boat is added. This approach ensures the minimum number of boats are used.

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
        
        int boats = 0;
        int left = 0, right = people.size() - 1;
        
        // Assign people to boats
        while (left <= right) {
            // If the heaviest and lightest person can be in the same boat
            if (people[left] + people[right] <= limit) {
                right--;
            }
            // Add a new boat
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
- Sort the weights in descending order to prioritize the heaviest people first.
- Use a two-pointer approach to assign people to boats, starting from the heaviest and lightest people.
- If the heaviest and lightest person can be in the same boat, move the right pointer to the next lightest person. Otherwise, add a new boat and move the left pointer to the next heaviest person.