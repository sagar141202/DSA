# Subsets

## Problem Statement
Given a set of distinct integers, return all possible subsets. The solution should be in lexicographic order, and the input array may contain duplicate elements. The constraints are: 1 <= nums.length <= 10, and -10 <= nums[i] <= 10. For example, if the input is [1, 2, 3], the output should be [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]].

## Approach
The approach to solve this problem is to use recursion and backtracking. We will start with an empty subset and then add each element to the subset, exploring all possible combinations. The key is to avoid duplicates in the subsets.

## Complexity
- Time: O(2^n)
- Space: O(2^n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        backtrack(result, current, nums, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& nums, int start) {
        result.push_back(current);
        for (int i = start; i < nums.size(); i++) {
            current.push_back(nums[i]);
            backtrack(result, current, nums, i + 1);
            current.pop_back();
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result = solution.subsets(nums);
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
Input: [1, 2, 3]
Output: 
[] 
[1] 
[1, 2] 
[1, 2, 3] 
[1, 3] 
[2] 
[2, 3] 
[3]
```

## Key Takeaways
- Use recursion and backtracking to explore all possible subsets of a given set.
- Avoid duplicates in the subsets by using a start index to track the current position in the input array.
- The time complexity is O(2^n) because there are 2^n possible subsets of a set with n elements.