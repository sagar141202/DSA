# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, given the array [1, 2, 2], the function should return `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`. The integers in the array can be negative and can have a value of zero.

## Approach
The approach involves using recursion and backtracking to generate all subsets. We will sort the array first to handle duplicates, then use a helper function to recursively generate subsets. The base case for recursion is when the start index exceeds the array size.

## Complexity
- Time: O(2^n * n)
- Space: O(2^n * n)

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
            // skip duplicates
            if (i > start && nums[i] == nums[i - 1]) {
                continue;
            }
            current.push_back(nums[i]);
            backtrack(result, current, nums, i + 1);
            current.pop_back();
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 2};
    vector<vector<int>> result = solution.subsetsWithDup(nums);
    for (auto& subset : result) {
        for (auto& num : subset) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: [1, 2, 2]
Output: 
[ ]
[ 1 ]
[ 1 2 ]
[ 1 2 2 ]
[ 2 ]
[ 2 2 ]
```

## Key Takeaways
- Recursion and backtracking can be used to solve problems that involve generating all possible combinations.
- Sorting the input array can help handle duplicates.
- Using a helper function can simplify the code and improve readability.