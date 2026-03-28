# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. For example, if the input is [1, 2, 3], the output should be [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]. The input array is non-empty and contains at most 9 numbers.

## Approach
The approach to solve this problem is to use recursion and backtracking. We start with an empty permutation and add numbers one by one, making sure that each number is used only once in each permutation. 
We use a helper function to generate all permutations.
The base case for recursion is when the permutation is complete.

## Complexity
- Time: O(N!)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        backtrack(result, current, nums);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& nums) {
        if (current.size() == nums.size()) {
            result.push_back(current);
            return;
        }
        
        for (int i = 0; i < nums.size(); i++) {
            if (find(current.begin(), current.end(), nums[i]) != current.end()) {
                continue;
            }
            current.push_back(nums[i]);
            backtrack(result, current, nums);
            current.pop_back();
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
- Use recursion and backtracking to generate all permutations of a given array.
- The time complexity is O(N!), where N is the number of elements in the array, because there are N! permutations.
- The space complexity is O(N), which is used to store the current permutation.