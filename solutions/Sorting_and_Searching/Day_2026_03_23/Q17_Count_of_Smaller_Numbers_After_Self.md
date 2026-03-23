# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`. For each element in the array, count the number of smaller elements on its right side. Return an array where each element at index `i` represents the count of smaller numbers to the right of `nums[i]`. The length of the input array will be between 1 and 20000, and the elements will be between 0 and 10000.

## Approach
We can use a Binary Indexed Tree (BIT) to solve this problem efficiently. The idea is to iterate through the array from right to left, and for each element, use the BIT to count the number of smaller elements on its right side. We will also use a hash map to store the frequency of each number.

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

    BIT(int n) : n(n), tree(n + 1, 0) {}

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
    vector<int> res(nums.size());
    vector<int> sortedNums = nums;
    sort(sortedNums.begin(), sortedNums.end());
    map<int, int> ranks;
    for (int i = 0; i < sortedNums.size(); i++) {
        ranks[sortedNums[i]] = i + 1;
    }
    BIT bit(nums.size() + 1);
    for (int i = nums.size() - 1; i >= 0; i--) {
        res[i] = bit.query(ranks[nums[i]] - 1);
        bit.update(ranks[nums[i]], 1);
    }
    return res;
}

int main() {
    vector<int> nums = {5, 2, 6, 1};
    vector<int> res = countSmaller(nums);
    for (int i = 0; i < res.size(); i++) {
        cout << res[i] << " ";
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
- We use a Binary Indexed Tree to efficiently count the number of smaller elements on the right side of each element.
- We use a hash map to store the frequency of each number, which allows us to get the rank of each number in O(1) time.
- The time complexity of the solution is O(n log n) due to the sorting and BIT operations.