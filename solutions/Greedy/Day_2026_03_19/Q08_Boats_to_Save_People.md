# Boats to Save People

## Problem Statement
Given an array of integers representing the weights of people and an integer representing the limit of each boat, determine the minimum number of boats required to save all people. Each boat can hold at most two people, and the sum of their weights cannot exceed the limit of the boat. The weights of the people are non-negative integers, and there are no empty boats.

## Approach
The greedy approach is to sort the weights of people in descending order and then try to pair the heaviest person with the lightest person who does not exceed the limit of the boat. If no such person is found, the heaviest person will be placed in a separate boat.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int numRescueBoats(vector<int>& people, int limit) {
    sort(people.rbegin(), people.rend());
    int left = 0, right = people.size() - 1;
    int boats = 0;
    while (left <= right) {
        if (people[left] + people[right] <= limit) {
            left++;
            right--;
        } else {
            left++;
        }
        boats++;
    }
    return boats;
}

int main() {
    vector<int> people = {1, 2, 3, 4, 5};
    int limit = 6;
    cout << numRescueBoats(people, limit) << endl;
    return 0;
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
- Sort the weights of people in descending order to prioritize the heaviest people.
- Try to pair the heaviest person with the lightest person who does not exceed the limit of the boat.
- If no such person is found, the heaviest person will be placed in a separate boat.