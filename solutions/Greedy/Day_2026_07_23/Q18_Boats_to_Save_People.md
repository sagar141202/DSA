# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. The goal is to determine the minimum number of boats required to save all people. Each boat can carry a maximum weight of limit. The people can be assigned to the boats in any order.

## Approach
The algorithm sorts the people by weight in descending order and then assigns them to the boats using a two-pointer technique. It tries to assign the heaviest person with the lightest person to minimize the number of boats.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        // Sort people by weight in descending order
        sort(people.rbegin(), people.rend());
        
        int light = 0, heavy = people.size() - 1;
        int boats = 0;
        
        // Assign people to boats
        while (light <= heavy) {
            // If the heaviest person can be assigned with the lightest person
            if (people[light] + people[heavy] <= limit) {
                light++;
            }
            // Move to the next heaviest person
            heavy--;
            boats++;
        }
        
        return boats;
    }
};

int main() {
    Solution solution;
    vector<int> people = {1, 2, 2, 3};
    int limit = 3;
    cout << solution.numRescueBoats(people, limit) << endl;
    return 0;
}
```

## Test Cases
```
Input: people = [1, 2, 2, 3], limit = 3
Output: 3
Input: people = [3, 2, 2, 1], limit = 3
Output: 3
```

## Key Takeaways
- Sort the people by weight to assign the heaviest person with the lightest person.
- Use a two-pointer technique to assign people to the boats.
- The time complexity is O(n log n) due to the sorting step.