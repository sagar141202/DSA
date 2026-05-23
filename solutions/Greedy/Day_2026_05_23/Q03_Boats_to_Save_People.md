# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. The goal is to determine the minimum number of boats required to save all people, given that each boat can hold at most two people and the total weight of the two people cannot exceed the limit of the boat. The weights of the people are non-negative integers, and the limit of the boat is a positive integer.

## Approach
The approach to solve this problem is to use a greedy algorithm, sorting the weights of the people in descending order and then iterating through the sorted array to assign people to boats. We will try to assign the heaviest person to a boat with the lightest person that does not exceed the limit.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int numRescueBoats(vector<int>& people, int limit) {
    // Sort the weights of the people in descending order
    sort(people.rbegin(), people.rend());
    
    int left = 0, right = people.size() - 1;
    int boats = 0;
    
    // Iterate through the sorted array to assign people to boats
    while (left <= right) {
        // If the heaviest person can be assigned to a boat with the lightest person, increment both pointers
        if (people[left] + people[right] <= limit) {
            left++;
            right--;
        } 
        // Otherwise, increment only the left pointer (heaviest person)
        else {
            left++;
        }
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
- Sort the weights of the people in descending order to prioritize assigning the heaviest people to boats first.
- Use two pointers, one at the beginning and one at the end of the sorted array, to assign people to boats efficiently.
- The greedy approach ensures that the minimum number of boats is used to save all people.