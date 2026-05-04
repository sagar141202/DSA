# Boats to Save People

## Problem Statement
We have a certain number of people that need to be saved, and a limited number of boats with different capacities. Each boat can only carry a certain number of people, and we need to find the minimum number of boats required to save all the people. The people are represented by an array of integers, where each integer is the weight of a person. The boats are represented by an integer, which is the capacity of each boat. We need to assign each person to a boat such that the total weight of people in each boat does not exceed its capacity. The goal is to minimize the number of boats used.

## Approach
The problem can be solved using a greedy algorithm, where we first sort the people by their weights in descending order. Then, we iterate over the people and assign each person to the first boat that has enough capacity to hold them. If no such boat exists, we create a new boat.

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
        // Sort the people by their weights in descending order
        sort(people.rbegin(), people.rend());
        
        int count = 0;
        int left = 0, right = people.size() - 1;
        
        while (left <= right) {
            // If the heaviest person can be paired with the lightest person, pair them
            if (people[left] + people[right] <= limit) {
                left++;
                right--;
            } 
            // Otherwise, the heaviest person needs their own boat
            else {
                left++;
            }
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
- Sort the people by their weights in descending order to prioritize the heaviest people.
- Use a two-pointer technique to assign people to boats, starting from the heaviest and lightest people.
- The time complexity is O(n log n) due to the sorting, and the space complexity is O(1) since we only use a constant amount of space.