# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. Each boat can hold at most two people, and the sum of their weights cannot exceed the limit. The goal is to determine the minimum number of boats required to save all people. The weights of people are non-negative integers, and the limit of each boat is a positive integer. For example, if the weights of people are [1, 2, 2, 3] and the limit of each boat is 3, the minimum number of boats required is 3.

## Approach
The algorithm uses a greedy approach, sorting the weights of people in descending order and then assigning the heaviest people to boats first. This ensures that the minimum number of boats is used, as the heaviest people are paired with the lightest people whenever possible. The time complexity is O(n log n) due to the sorting step.

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
        // Sort the weights of people in descending order
        sort(people.rbegin(), people.rend());
        int left = 0, right = people.size() - 1;
        int boats = 0;
        
        // Assign the heaviest people to boats first
        while (left <= right) {
            if (people[left] + people[right] <= limit) {
                // If the heaviest and lightest people can be in the same boat, move both pointers
                right--;
            }
            // Move the left pointer to the next heaviest person
            left++;
            // Increment the number of boats
            boats++;
        }
        return boats;
    }
};
```

## Test Cases
```
Input: people = [1, 2, 2, 3], limit = 3
Output: 3
Input: people = [1, 2, 4, 5], limit = 6
Output: 3
```

## Key Takeaways
- The greedy approach is used to minimize the number of boats required.
- Sorting the weights of people in descending order ensures that the heaviest people are paired with the lightest people whenever possible.
- The two-pointer technique is used to efficiently assign people to boats.