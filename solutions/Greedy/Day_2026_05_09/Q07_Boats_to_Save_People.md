# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. The goal is to determine the minimum number of boats required to save all people, with the constraint that the total weight of people in each boat cannot exceed the limit. The people can be assigned to boats in any order, but each person can only be in one boat.

## Approach
The algorithm uses a two-pointer technique, sorting the people by weight in descending order and assigning the heaviest people to boats first. This approach ensures that the minimum number of boats is used, as the heaviest people are assigned to boats before the lighter people.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int numRescueBoats(vector<int>& people, int limit) {
    // Sort the people by weight in descending order
    sort(people.rbegin(), people.rend());
    
    int boats = 0;
    int left = 0, right = people.size() - 1;
    
    while (left <= right) {
        // If the heaviest person can be paired with the lightest person, pair them
        if (people[left] + people[right] <= limit) {
            right--;
        }
        // Increment the boat count and move to the next heaviest person
        boats++;
        left++;
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
- Sort the people by weight in descending order to prioritize the heaviest people.
- Use a two-pointer technique to assign people to boats, starting with the heaviest people.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(n) for the sorting.