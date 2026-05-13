# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. The input is a list of integers, and the output should be a list of lists, where each sublist is a permutation of the input list. For example, if the input is [1, 2, 3], the output should be [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]. The length of the input list will not exceed 10, and the elements will be between 1 and 10.

## Approach
The approach to solve this problem is to use recursion and backtracking. We start with an empty list and add each number from the input list to the current permutation, then recursively generate all permutations of the remaining numbers. After exploring all permutations with the current number, we backtrack and try the next number.

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
                swap(nums[start], nums[i]);
                backtrack(result, nums, start + 1);
                swap(nums[start], nums[i]);
            }
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
- The recursion and backtracking approach allows us to efficiently generate all permutations of the input list.
- The time complexity of O(n!) is due to the fact that there are n! possible permutations of a list of length n.
- The space complexity of O(n) is due to the recursive call stack, which can go up to a depth of n in the worst case.