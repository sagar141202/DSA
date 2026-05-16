# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. The goal is to determine the minimum number of boats required to save all people, with each boat able to carry a maximum weight equal to the limit. The people are saved in a greedy manner, where the heaviest person is saved first, and each boat can only be used once. The weights array is not guaranteed to be sorted, and the limit is a positive integer.

## Approach
The algorithm uses a two-pointer technique to assign the heaviest person to a boat and then tries to fill the remaining capacity with the lightest person. This greedy approach ensures the minimum number of boats are used. The people are sorted in descending order of their weights to prioritize the heaviest people.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int numRescueBoats(vector<int>& people, int limit) {
    // Sort the people array in descending order
    sort(people.rbegin(), people.rend());
    
    int count = 0;  // Initialize the count of boats
    int left = 0, right = people.size() - 1;  // Initialize two pointers
    
    while (left <= right) {
        // If the heaviest person can be paired with the lightest person
        if (people[left] + people[right] <= limit) {
            right--;  // Move the right pointer
        }
        // Increment the count and move the left pointer
        count++;
        left++;
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
Input: people = [3,5,3,4], limit = 5
Output: 4
```

## Key Takeaways
- Sort the people array in descending order to prioritize the heaviest people.
- Use a two-pointer technique to assign people to boats and minimize the number of boats used.
- The greedy approach ensures the minimum number of boats are used by filling each boat to its maximum capacity.