# Boats to Save People

## Problem Statement
There are `numRescueBoats` boats available to save people from a sinking ship, and each boat can hold a maximum of `limit` people. The people are waiting on the ship with different weights, represented by the array `people`. The goal is to determine the minimum number of boats required to save all the people, given that each boat can carry a maximum weight of `limit`. The people can be paired up in any order to fill the boats, but the weight of each pair must not exceed the limit.

## Approach
The approach to solve this problem is to use a greedy algorithm, sorting the people by their weights in descending order and then pairing up the heaviest people with the lightest people. This way, we can minimize the number of boats required.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int numRescueBoats(vector<int>& people, int limit) {
    // Sort the people in descending order of their weights
    sort(people.rbegin(), people.rend());
    
    int left = 0, right = people.size() - 1;
    int boats = 0;
    
    // Pair up the heaviest people with the lightest people
    while (left <= right) {
        if (people[left] + people[right] <= limit) {
            // If the pair's weight does not exceed the limit, increment the left pointer
            left++;
        }
        // Increment the right pointer and the number of boats
        right--;
        boats++;
    }
    
    return boats;
}
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
- Sort the people by their weights in descending order to pair up the heaviest people with the lightest people.
- Use two pointers, one starting from the beginning and one from the end of the array, to pair up the people and minimize the number of boats required.
- The time complexity of the solution is O(n log n) due to the sorting operation.