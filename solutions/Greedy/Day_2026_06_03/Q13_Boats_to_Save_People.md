# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. The goal is to determine the minimum number of boats required to save all people. Each boat can hold at most two people, and the total weight of the two people cannot exceed the limit of the boat. The input array is not sorted, and the weights of people are positive integers.

## Approach
The algorithm uses a greedy approach, sorting the weights of people in descending order and then assigning the heaviest people to boats first. This ensures that the minimum number of boats is used, as the heaviest people are paired with the lightest people whenever possible. The greedy approach works because the problem has the optimal substructure property.

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
        
        // Assign people to boats
        while (left <= right) {
            // If the heaviest person can be paired with the lightest person, pair them
            if (people[left] + people[right] <= limit) {
                right--;
            }
            // Increment the number of boats and move to the next heaviest person
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
Input: people = [3,5,3,4], limit = 5
Output: 4
```

## Key Takeaways
- The greedy approach is used to solve the problem, as it has the optimal substructure property.
- Sorting the weights of people in descending order ensures that the minimum number of boats is used.
- The two-pointer technique is used to assign people to boats efficiently.