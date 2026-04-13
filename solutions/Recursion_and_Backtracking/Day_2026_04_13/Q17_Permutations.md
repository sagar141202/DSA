# Permutations

## Problem Statement
Given an array of distinct integers, generate all possible permutations of the array. The length of the array will be in the range [1, 10]. The array will contain distinct integers in the range [-10, 10]. For example, given the array [1, 2, 3], the output should be [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]].

## Approach
The problem can be solved using recursion and backtracking. The idea is to fix one element at a time and generate all permutations of the remaining elements. We will use a helper function to recursively generate the permutations.

## Complexity
- Time: O(n!)
- Space: O(n)

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
        } else {
            for (int i = start; i < nums.size(); i++) {
                // swap the current element with the start element
                swap(nums[start], nums[i]);
                // recursively generate permutations for the remaining elements
                backtrack(result, nums, start + 1);
                // backtrack by swapping the elements back
                swap(nums[start], nums[i]);
            }
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result = solution.permute(nums);
    for (auto& vec : result) {
        for (auto& num : vec) {
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
- Recursion and backtracking can be used to generate all permutations of an array.
- The time complexity is O(n!) because there are n! possible permutations.
- The space complexity is O(n) because we need to store the recursive call stack.