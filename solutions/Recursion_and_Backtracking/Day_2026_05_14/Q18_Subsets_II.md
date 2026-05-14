# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, and return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, if the input is `[1, 2, 2]`, the output should be `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`. The input array is not null, and the elements in the array are between 0 and 100. The size of the array is not more than 10.

## Approach
The solution involves using recursion and backtracking to generate all possible subsets. We will use a helper function to recursively build the subsets and avoid duplicates by skipping the same elements.

## Complexity
- Time: O(2^n) where n is the number of elements in the input array
- Space: O(2^n) for storing the result and O(n) for the recursion stack

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
    
    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& nums, int index) {
        result.push_back(current);
        for (int i = index; i < nums.size(); i++) {
            if (i > index && nums[i] == nums[i - 1]) {
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
    for (auto subset : result) {
        for (auto num : subset) {
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
[] 
[1] 
[1, 2] 
[1, 2, 2] 
[2] 
[2, 2]
```

## Key Takeaways
- The key to solving this problem is to use recursion and backtracking to generate all possible subsets.
- To avoid duplicates, we sort the input array and skip the same elements in the recursive function.
- The time complexity is O(2^n) because we generate all possible subsets, and the space complexity is O(2^n) for storing the result and O(n) for the recursion stack.