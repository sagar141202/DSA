# Count of Smaller Numbers After Self

## Problem Statement
Given an array of integers, return an array where each element at index `i` represents the number of smaller elements to the right of `i` in the original array. The input array will contain unique integers, and the length of the array will be between 1 and 10^5. For example, given the array `[5, 2, 6, 1]`, the output should be `[2, 1, 1, 0]`, because there are 2 elements smaller than 5 to its right (2 and 1), 1 element smaller than 2 to its right (1), 1 element smaller than 6 to its right (1), and 0 elements smaller than 1 to its right.

## Approach
We can solve this problem using a Binary Indexed Tree (BIT) and a modified merge sort algorithm. The merge sort will help us to count the smaller elements for each element, and the BIT will help us to update the count efficiently. We will iterate over the array from right to left and for each element, we will count the number of smaller elements to its right using the BIT.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class BIT {
public:
    vector<int> tree;
    int n;

    BIT(int n) {
        this->n = n;
        tree.resize(n + 1, 0);
    }

    void update(int i, int val) {
        while (i <= n) {
            tree[i] += val;
            i += i & -i;
        }
    }

    int query(int i) {
        int sum = 0;
        while (i > 0) {
            sum += tree[i];
            i -= i & -i;
        }
        return sum;
    }
};

vector<int> countSmaller(vector<int>& nums) {
    vector<int> rank(nums.begin(), nums.end());
    sort(rank.begin(), rank.end());
    for (int i = 0; i < nums.size(); i++) {
        nums[i] = lower_bound(rank.begin(), rank.end(), nums[i]) - rank.begin() + 1;
    }

    BIT bit(nums.size() + 1);
    vector<int> res(nums.size(), 0);
    for (int i = nums.size() - 1; i >= 0; i--) {
        res[i] = bit.query(nums[i] - 1);
        bit.update(nums[i], 1);
    }
    return res;
}

int main() {
    vector<int> nums = {5, 2, 6, 1};
    vector<int> res = countSmaller(nums);
    for (int num : res) {
        cout << num << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: [5, 2, 6, 1]
Output: [2, 1, 1, 0]
```

## Key Takeaways
- We can use a Binary Indexed Tree to efficiently update and query the count of smaller elements.
- We can use a modified merge sort algorithm to count the smaller elements for each element in the array.
- The time complexity of the solution is O(n log n) due to the use of the BIT and the modified merge sort algorithm.