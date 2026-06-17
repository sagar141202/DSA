# Boats to Save People

## Problem Statement
You are given an array of integers representing the weights of people and an integer representing the limit of each boat. The task is to determine the minimum number of boats required to save all people, where each boat can carry a maximum weight equal to the limit. The people can be assigned to the boats in any order, but each person can only be in one boat.

## Approach
The approach is to use a greedy algorithm, sorting the people by weight in descending order and then assigning them to the boats. We use two pointers, one at the start and one at the end of the array, to assign the heaviest and lightest people to the same boat if possible.

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
        // Sort the people by weight in descending order
        sort(people.rbegin(), people.rend());
        
        int count = 0;
        int left = 0, right = people.size() - 1;
        
        // Assign the heaviest and lightest people to the same boat if possible
        while (left <= right) {
            if (people[left] + people[right] <= limit) {
                right--;
            }
            count++;
            left++;
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
- Sorting the people by weight in descending order allows us to assign the heaviest and lightest people to the same boat if possible, minimizing the number of boats required.
- Using two pointers, one at the start and one at the end of the array, allows us to efficiently assign people to boats.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(n) for the input array.