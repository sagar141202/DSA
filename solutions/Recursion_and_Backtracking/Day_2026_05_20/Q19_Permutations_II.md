# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input collection is not sorted, and the output should not contain duplicate permutations. For example, given the input [1, 1, 2], the output should be [[1, 1, 2], [1, 2, 1], [2, 1, 1]]. The input array will have a length between 1 and 9, and each element will be between 1 and 9.

## Approach
The solution uses recursion and backtracking to generate all permutations. It sorts the input array and skips duplicate elements to avoid duplicate permutations. The algorithm recursively generates all permutations by swapping each element with the remaining elements.

## Complexity
- Time: O(N! / (k1! * k2! * ... * kn!)) where N is the length of the input array, and k1, k2, ..., kn are the frequencies of each element.
- Space: O(N) for the recursion stack and the output array.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        vector<bool> visited(nums.size(), false);
        vector<int> current;
        
        backtrack(result, nums, current, visited);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& nums, vector<int>& current, vector<bool>& visited) {
        if (current.size() == nums.size()) {
            result.push_back(current);
            return;
        }
        
        for (int i = 0; i < nums.size(); i++) {
            if (visited[i] || (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1])) {
                continue;
            }
            visited[i] = true;
            current.push_back(nums[i]);
            backtrack(result, nums, current, visited);
            current.pop_back();
            visited[i] = false;
        }
    }
};

```

## Test Cases
```
Input: [1, 1, 2]
Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
Input: [2, 1, 1]
Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
```

## Key Takeaways
- Sort the input array to handle duplicate elements.
- Use a visited array to keep track of the elements that have been used in the current permutation.
- Use recursion and backtracking to generate all permutations.