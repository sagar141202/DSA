# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. The goal is to determine the minimum number of boats required to save all people, with each boat able to hold a maximum weight equal to the given limit. The weights of people must be paired in such a way that the total weight of each pair does not exceed the limit of the boat. If a person cannot be paired, they will occupy a boat alone.

## Approach
The problem can be solved using a greedy approach by sorting the weights of people in descending order and then pairing the heaviest person with the lightest person who does not exceed the boat's limit. This approach ensures that the minimum number of boats are used.

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
        
        int left = 0, right = people.size() - 1;
        int boats = 0;
        
        // Pair the heaviest person with the lightest person
        while (left <= right) {
            if (people[left] + people[right] <= limit) {
                // If the pair's weight does not exceed the limit, move both pointers
                right--;
            }
            // Move the left pointer regardless of whether a pair is formed
            left++;
            // Increment the boat count
            boats++;
        }
        
        return boats;
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
- Sort the weights of people in descending order to prioritize pairing the heaviest person.
- Use two pointers, one starting from the heaviest person and one from the lightest person, to efficiently pair people.
- Increment the boat count for each iteration, regardless of whether a pair is formed or not.