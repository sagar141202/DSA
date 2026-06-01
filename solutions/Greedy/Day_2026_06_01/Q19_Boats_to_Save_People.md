# Boats to Save People

## Problem Statement
There are `numRescueBoats` boats available to save people, and each boat has a limited capacity. We also have a list of people with their respective weights. The goal is to determine the minimum number of boats required to save all the people. We can assume that each boat can carry a maximum weight of `limit`. The people can be paired in any order to fill the boats, but the total weight of each pair should not exceed the `limit`. If the total weight of a pair exceeds the `limit`, then the two people cannot be in the same boat.

## Approach
The algorithm uses a greedy approach by sorting the people in descending order of their weights and then pairing the heaviest person with the lightest person. This approach ensures that the minimum number of boats are used. The two-pointer technique is used to pair the people.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        // Sort the people in ascending order of their weights
        sort(people.begin(), people.end());
        
        // Initialize two pointers, one at the start and one at the end
        int left = 0, right = people.size() - 1;
        
        // Initialize the count of boats
        int boats = 0;
        
        // Continue the process until the two pointers meet
        while (left <= right) {
            // If the total weight of the people at the two pointers does not exceed the limit, pair them
            if (people[left] + people[right] <= limit) {
                left++;
            }
            // Move the right pointer to the left
            right--;
            // Increment the count of boats
            boats++;
        }
        
        // Return the minimum number of boats required
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
- The greedy approach can be used to solve this problem by pairing the heaviest person with the lightest person.
- The two-pointer technique is useful in this problem to pair the people.
- The time complexity is O(n log n) due to the sorting operation.