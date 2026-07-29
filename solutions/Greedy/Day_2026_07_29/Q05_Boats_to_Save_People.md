# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. The goal is to determine the minimum number of boats required to save all people, with each boat able to hold a maximum weight equal to the given limit. The problem has the following constraints: 1 <= people.length <= 10^5, 1 <= people[i] <= 10^5, and 1 <= limit <= 10^5.

## Approach
The algorithm uses a two-pointer approach, sorting the people array in ascending order and then iterating through it with two pointers, one from the start and one from the end. The greedy strategy is to always try to put the heaviest person with the lightest person in the same boat.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int numRescueBoats(vector<int>& people, int limit) {
    // Sort the people array in ascending order
    sort(people.begin(), people.end());
    
    // Initialize two pointers, one from the start and one from the end
    int left = 0, right = people.size() - 1;
    int boats = 0;
    
    // Iterate through the array with the two pointers
    while (left <= right) {
        // If the heaviest person can be put in the same boat as the lightest person
        if (people[left] + people[right] <= limit) {
            // Move the left pointer to the next person
            left++;
        }
        // Move the right pointer to the next person
        right--;
        // Increment the number of boats
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
```

## Key Takeaways
- The two-pointer approach is useful for solving problems that involve finding pairs or combinations of elements in an array.
- Sorting the array in ascending or descending order can simplify the problem and make it easier to find a solution.
- The greedy strategy is often effective for solving problems that involve optimization or minimization.