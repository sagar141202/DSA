# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. The problem statement requires generating all possible arrangements of the input numbers. For example, given the input [1, 2, 3], the output should be [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]. The input will contain distinct integers, and the output should be a list of lists, where each sublist is a permutation of the input.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will start with an empty permutation and add numbers one by one, making sure to explore all possible branches. The recursion will help us to generate all permutations by swapping each number with the remaining numbers.

## Complexity
- Time: O(n!)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, int start, vector<vector<int>>& result) {
    if (start == nums.size()) {
        result.push_back(nums);
    }
    for (int i = start; i < nums.size(); i++) {
        swap(nums[start], nums[i]);
        backtrack(nums, start + 1, result);
        swap(nums[start], nums[i]);
    }
}

vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int>> result;
    backtrack(nums, 0, result);
    return result;
}

int main() {
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result = permute(nums);
    for (auto& perm : result) {
        for (auto& num : perm) {
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
Output: 
1 2 3 
1 3 2 
2 1 3 
2 3 1 
3 1 2 
3 2 1 
```

## Key Takeaways
- Use recursion and backtracking to generate all permutations of a given input.
- Swap each number with the remaining numbers to explore all possible branches.
- Use a base case to stop the recursion when the permutation is complete.