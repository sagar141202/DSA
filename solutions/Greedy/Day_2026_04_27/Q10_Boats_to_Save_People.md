# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. Determine the minimum number of boats required to save all people, given that each boat can hold a maximum weight of limit and each person can only be in one boat. The weights of people are non-negative integers, and the limit is a positive integer.

## Approach
The problem can be solved using a greedy approach by sorting the weights of people in descending order and then assigning them to boats. We start by assigning the heaviest person to a boat and then try to assign the next heaviest person to the same boat if possible.

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
        
        int count = 0;
        int left = 0, right = people.size() - 1;
        
        while (left <= right) {
            // If the heaviest person can be assigned to the same boat as the lightest person, assign them together
            if (people[left] + people[right] <= limit) {
                right--;
            }
            // Increment the count of boats and move to the next heaviest person
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
Input: people = [3,5,3,4], limit = 5
Output: 4
```

## Key Takeaways
- Sort the weights of people in descending order to assign the heaviest people first.
- Try to assign the heaviest person to the same boat as the lightest person if possible to minimize the number of boats.
- Use two pointers, one at the start and one at the end of the sorted array, to keep track of the heaviest and lightest people.