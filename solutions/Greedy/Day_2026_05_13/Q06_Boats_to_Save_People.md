# Boats to Save People

## Problem Statement
Given an array of integers representing the weights of people and an integer representing the limit of each boat, determine the minimum number of boats required to save all people. Each boat can hold at most two people, and the sum of their weights cannot exceed the limit. The people are represented by their weights, and the weights are non-negative integers.

## Approach
The problem can be solved using a greedy algorithm by sorting the people's weights in descending order and then assigning them to boats. We start by assigning the heaviest person to a boat and then try to assign the next heaviest person to the same boat if possible. The algorithm continues until all people are assigned to boats.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int numRescueBoats(vector<int>& people, int limit) {
    // Sort the people's weights in descending order
    sort(people.rbegin(), people.rend());
    
    int left = 0, right = people.size() - 1;
    int boats = 0;
    
    // Assign people to boats
    while (left <= right) {
        // If the heaviest person can be assigned to the same boat as the lightest person, assign them together
        if (people[left] + people[right] <= limit) {
            right--;
        }
        // Increment the boat count and move to the next heaviest person
        left++;
        boats++;
    }
    
    return boats;
}

int main() {
    vector<int> people = {1, 2};
    int limit = 3;
    cout << numRescueBoats(people, limit) << endl;
    return 0;
}
```

## Test Cases
```
Input: people = [1, 2], limit = 3
Output: 1
Input: people = [3, 2, 2, 1], limit = 3
Output: 3
Input: people = [3, 5, 3, 4], limit = 5
Output: 4
```

## Key Takeaways
- Sort the people's weights in descending order to prioritize assigning the heaviest people first.
- Use a two-pointer approach to assign people to boats efficiently.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(1) since we only use a constant amount of space.