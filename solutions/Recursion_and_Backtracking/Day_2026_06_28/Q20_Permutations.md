# Permutations

## Problem Statement
Given a collection of distinct integers, return all possible permutations. The solution should be able to handle a large input size and provide all unique permutations. For example, given the input `[1, 2, 3]`, the output should be `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`. The input size will be between 1 and 10, and the integers will be between 1 and 100.

## Approach
The algorithm uses backtracking to generate all permutations. It iterates through each element in the input array, adds it to the current permutation, and recursively generates all permutations of the remaining elements. The base case is when the current permutation is the same size as the input array, at which point it is added to the result list. The algorithm ensures that all elements are used exactly once in each permutation.

## Complexity
- Time: O(N!), where N is the number of elements in the input array, since there are N! possible permutations.
- Space: O(N!), as in the worst case, the space required to store all permutations is proportional to the number of permutations.

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
                // Swap the current element with the start element
                swap(nums[start], nums[i]);
                // Recursively generate all permutations of the remaining elements
                backtrack(result, nums, start + 1);
                // Backtrack by swapping the elements back
                swap(nums[start], nums[i]);
            }
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result = solution.permute(nums);
    // Print the result
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
Input: [0, 1]
Output: [[0, 1], [1, 0]]
Input: [1]
Output: [[1]]
```

## Key Takeaways
- The algorithm uses backtracking to generate all permutations, ensuring that all elements are used exactly once in each permutation.
- The time complexity is O(N!), where N is the number of elements in the input array, as there are N! possible permutations.
- The space complexity is also O(N!), as in the worst case, the space required to store all permutations is proportional to the number of permutations.