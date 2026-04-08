# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. The goal is to determine the minimum number of boats required to save all people, where each boat can carry a maximum weight of limit. The people can be assigned to the boats in any order, but the total weight of the people in each boat cannot exceed the limit.

## Approach
The approach is to sort the people by their weights in descending order and then assign them to the boats using a two-pointer technique. We start by assigning the heaviest person to a boat and then try to assign the lightest person to the same boat if possible.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int numRescueBoats(vector<int>& people, int limit) {
    // Sort the people by their weights in descending order
    sort(people.rbegin(), people.rend());
    
    int boats = 0;
    int left = 0, right = people.size() - 1;
    
    while (left <= right) {
        // If the heaviest person can be assigned to a boat with the lightest person
        if (people[left] + people[right] <= limit) {
            // Move the lightest person to the next position
            right--;
        }
        // Move the heaviest person to the next position
        left++;
        // Increment the number of boats
        boats++;
    }
    
    return boats;
}

int main() {
    vector<int> people = {1, 2, 2, 3};
    int limit = 3;
    cout << numRescueBoats(people, limit) << endl;
    return 0;
}
```

## Test Cases
```
Input: people = [1, 2, 2, 3], limit = 3
Output: 3
Input: people = [3, 2, 2, 1], limit = 3
Output: 3
Input: people = [3, 5, 3, 4], limit = 5
Output: 4
```

## Key Takeaways
- Sort the people by their weights in descending order to assign the heaviest people first.
- Use a two-pointer technique to assign people to the boats, starting from the heaviest and lightest people.
- Increment the number of boats for each assignment, regardless of whether one or two people are assigned to the boat.