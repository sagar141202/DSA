# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. For example, if the input is [1, 2, 3], the output will be [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]. The input array will have a length between 1 and 6, and it will contain distinct integers.

## Approach
The approach used here is recursion and backtracking, where we generate each permutation by fixing one number at a time and recursively generating the rest. The algorithm uses a helper function to swap numbers and backtrack when necessary. This process continues until all numbers have been fixed in each possible position.

## Complexity
- Time: O(N * N!)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        backtrack(result, nums, 0);
        return result;
    }

    void backtrack(vector<vector<int>>& result, vector<int>& nums, int start) {
        if (start == nums.size()) {
            result.push_back(nums);
        }
        for (int i = start; i < nums.size(); i++) {
            swap(nums[start], nums[i]);
            backtrack(result, nums, start + 1);
            swap(nums[start], nums[i]);
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result = solution.permute(nums);
    for (auto& permutation : result) {
        for (auto& num : permutation) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

## Key Takeaways
- Recursion and backtracking are useful for solving problems that involve exploring all possible configurations or arrangements.
- The key to backtracking is to make a choice, explore the consequences of that choice, and then undo the choice when it's no longer needed.
- The time complexity of this solution is O(N * N!) because there are N! permutations and it takes O(N) time to generate each permutation.