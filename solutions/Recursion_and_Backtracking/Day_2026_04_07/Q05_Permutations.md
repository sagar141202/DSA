# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. The solution should use recursion and backtracking to generate all permutations. For example, given the input [1, 2, 3], the output should be [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]. The input array will contain at most 6 elements.

## Approach
The approach involves using recursion to generate all permutations. We will start with an empty permutation and add elements from the input array one by one, backtracking when a permutation is complete. The key idea is to swap each element in the array with the current position and recurse.

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
Output: 
1 2 3 
1 3 2 
2 1 3 
2 3 1 
3 1 2 
3 2 1 
```

## Key Takeaways
- Recursion and backtracking can be used to generate all permutations of a given array.
- The time complexity of this approach is O(n!) because there are n! permutations of an array of size n.
- The space complexity is O(n) due to the recursive call stack.