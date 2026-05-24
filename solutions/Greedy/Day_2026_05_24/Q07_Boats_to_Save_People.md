# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people who need to be saved from a sinking ship. Each person can be saved using a boat, and each boat can hold a maximum weight. The goal is to determine the minimum number of boats required to save all people, given the maximum weight capacity of each boat. The weights of the people are represented by the array `people`, and the maximum weight capacity of each boat is represented by the variable `limit`. For example, if `people = [1,2,2,3]` and `limit = 3`, the minimum number of boats required is 3, as we can assign the people to boats as follows: boat 1 = [1,2], boat 2 = [2], boat 3 = [3].

## Approach
The algorithm uses a greedy approach, sorting the people by their weights in descending order and then assigning them to boats. We use two pointers, one starting from the heaviest person and one from the lightest person, to assign people to the same boat if possible. This approach ensures that we minimize the number of boats required. The time complexity of this approach is O(n log n) due to the sorting step.

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
    
    // Assign people to boats
    while (left <= right) {
        // If the heaviest person can be assigned to the same boat as the lightest person
        if (people[left] + people[right] <= limit) {
            // Assign them to the same boat
            right--;
        }
        // Increment the number of boats
        boats++;
        // Move to the next heaviest person
        left++;
    }
    
    return boats;
}
```

## Test Cases
```
Input: people = [1,2,2,3], limit = 3
Output: 3
Input: people = [3,2,2,1], limit = 3
Output: 3
Input: people = [3,5,3,4], limit = 5
Output: 4
```

## Key Takeaways
- The greedy approach can be used to solve this problem by sorting the people by their weights and assigning them to boats.
- The time complexity of the solution is O(n log n) due to the sorting step.
- The space complexity of the solution is O(1) as we only use a constant amount of space to store the pointers and the number of boats.