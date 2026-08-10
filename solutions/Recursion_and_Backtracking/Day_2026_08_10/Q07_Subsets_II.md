# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, and no duplicate subsets are allowed in the result, return all possible subsets of the given set of integers. The integers in the set may be duplicated, but the subsets in the result must be unique. For example, if the input is [1, 2, 2], the output should be [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]].

## Approach
The solution utilizes recursion and backtracking to generate all subsets. It sorts the input array to handle duplicates and skips the current iteration if the current element is the same as the previous one. This approach ensures that duplicate subsets are not included in the result.

## Complexity
- Time: O(2^n * n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        sort(nums.begin(), nums.end());
        backtrack(result, current, nums, 0);
        return result;
    }

    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& nums, int start) {
        result.push_back(current);
        for (int i = start; i < nums.size(); i++) {
            // Skip duplicates
            if (i > start && nums[i] == nums[i - 1]) {
                continue;
            }
            current.push_back(nums[i]);
            backtrack(result, current, nums, i + 1);
            current.pop_back();
        }
    }
};
```

## Test Cases
```
Input: [1, 2, 2]
Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
Input: [0]
Output: [[], [0]]
```

## Key Takeaways
- Recursion and backtracking can be used to solve subset-related problems efficiently.
- Sorting the input array helps handle duplicates by allowing us to skip identical elements during the backtracking process.
- Utilizing a helper function (backtrack) simplifies the code and improves readability.