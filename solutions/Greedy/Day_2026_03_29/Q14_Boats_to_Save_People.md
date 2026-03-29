# Boats to Save People

## Problem Statement
Given an array of integers representing the weights of people and an integer representing the limit of each boat, determine the minimum number of boats required to save all people. Each boat can carry a maximum weight of limit. The problem can be solved by using a two-pointer technique to pair the heaviest people with the lightest people. The constraints are: 1 <= people.length <= 5 * 10^4, 1 <= people[i] <= 10^5, and people[i] <= limit <= 3 * 10^4.

## Approach
The algorithm sorts the array of people's weights in ascending order and uses two pointers, one at the start and one at the end of the array, to pair the heaviest people with the lightest people. If the sum of their weights exceeds the limit, the heaviest person is assigned to a boat. The process continues until all people are assigned to boats.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int numRescueBoats(vector<int>& people, int limit) {
    // Sort the array of people's weights in ascending order
    sort(people.begin(), people.end());
    
    int count = 0;
    int left = 0, right = people.size() - 1;
    
    // Use two pointers to pair the heaviest people with the lightest people
    while (left <= right) {
        if (people[left] + people[right] <= limit) {
            // If the sum of their weights does not exceed the limit, pair them
            left++;
        }
        // The heaviest person is assigned to a boat
        right--;
        count++;
    }
    
    return count;
}
```

## Test Cases
```
Input: people = [1,2], limit = 3
Output: 1
Input: people = [3,2,2,1], limit = 3
Output: 3
```

## Key Takeaways
- Sort the array of people's weights in ascending order to efficiently pair the heaviest people with the lightest people.
- Use a two-pointer technique to traverse the array and assign people to boats.
- The time complexity is O(n log n) due to the sorting operation.