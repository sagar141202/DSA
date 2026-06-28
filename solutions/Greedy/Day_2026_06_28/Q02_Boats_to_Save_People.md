# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. The goal is to determine the minimum number of boats required to save all people. Each boat can carry a maximum weight of limit. The problem can be solved by using a greedy approach where we try to fill each boat with the heaviest people first.

## Approach
The algorithm works by sorting the people in descending order of their weights and then trying to fill each boat with the heaviest people. We use two pointers, one at the start and one at the end of the array, to keep track of the people who can be put in the current boat.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int numRescueBoats(vector<int>& people, int limit) {
    // Sort the people in descending order of their weights
    sort(people.rbegin(), people.rend());
    
    int count = 0;
    int left = 0, right = people.size() - 1;
    
    // Try to fill each boat with the heaviest people
    while (left <= right) {
        // If the heaviest person can be put in the same boat as the lightest person, do so
        if (people[left] + people[right] <= limit) {
            left++;
            right--;
        } 
        // Otherwise, put the heaviest person in a separate boat
        else {
            left++;
        }
        count++;
    }
    
    return count;
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
```

## Key Takeaways
- The key to solving this problem is to sort the people in descending order of their weights.
- We use a two-pointer approach to keep track of the people who can be put in the current boat.
- By trying to fill each boat with the heaviest people first, we minimize the number of boats required to save all people.