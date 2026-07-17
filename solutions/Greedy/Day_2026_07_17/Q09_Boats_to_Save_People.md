# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. The goal is to determine the minimum number of boats required to save all people, with each boat able to carry a maximum weight equal to the given limit. The weights of people must be sorted in descending order to maximize the utilization of each boat.

## Approach
The algorithm uses a two-pointer technique, starting from both ends of the sorted array. It assigns the heaviest person to a boat and then tries to assign the lightest person to the same boat if possible, to maximize the utilization of each boat. This process continues until all people are assigned to boats.

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
        // Sort the people array in descending order
        sort(people.rbegin(), people.rend());
        
        int count = 0;
        int left = 0, right = people.size() - 1;
        
        while (left <= right) {
            // If the heaviest person and the lightest person can be in the same boat
            if (people[left] + people[right] <= limit) {
                right--;
            }
            // Increment the boat count and move to the next heaviest person
            left++;
            count++;
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
- Sorting the people array in descending order is crucial to maximize the utilization of each boat.
- The two-pointer technique allows us to efficiently assign people to boats.
- This solution has a time complexity of O(n log n) due to the sorting operation.