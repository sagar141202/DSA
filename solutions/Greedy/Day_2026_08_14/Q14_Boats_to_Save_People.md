# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. Each boat can only hold a limited number of people, and the weight of the people in the boat cannot exceed the limit. The goal is to determine the minimum number of boats required to save all people. The people can be divided into boats in any order, but each person can only be in one boat.

## Approach
The problem can be solved using a greedy approach by sorting the weights of people in descending order and then assigning them to boats. We use two pointers, one at the start and one at the end of the array, to assign the heaviest and lightest people to the same boat if possible.

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
        
        int count = 0;
        int left = 0, right = people.size() - 1;
        
        while (left <= right) {
            // If the heaviest and lightest people can be in the same boat
            if (people[left] + people[right] <= limit) {
                right--;
            }
            // Increment the boat count and move to the next heaviest person
            left++;
            count++;
        }
        
        return count;
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
- Sort the weights of people in descending order to prioritize the heaviest people.
- Use two pointers to assign the heaviest and lightest people to the same boat if possible.
- Increment the boat count for each boat, regardless of whether it contains one or two people.