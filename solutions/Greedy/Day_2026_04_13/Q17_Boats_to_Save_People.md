# Boats to Save People

## Problem Statement
There are `numRescueBoats` boats available to save people, and each boat can only hold a certain weight limit. We have a list of people with their respective weights, and we want to determine the minimum number of boats required to save all the people. The weight limit of each boat is the maximum weight it can hold. We can assume that each person will be assigned to the first boat that can accommodate them. The goal is to find the minimum number of boats needed to rescue all the people.

## Approach
We will use a greedy algorithm to solve this problem, sorting the people by their weights and then assigning them to the boats. The idea is to always assign the heaviest person to the boat that can accommodate them.

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
            // If the heaviest person can be assigned to the same boat as the lightest person
            if (people[left] + people[right] <= limit) {
                right--;
            }
            // Move to the next boat
            count++;
            left++;
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
- Sort the people by their weights to prioritize the heaviest people.
- Use two pointers, one for the heaviest person and one for the lightest person, to assign them to the boats efficiently.
- The greedy algorithm ensures that we use the minimum number of boats required to rescue all the people.