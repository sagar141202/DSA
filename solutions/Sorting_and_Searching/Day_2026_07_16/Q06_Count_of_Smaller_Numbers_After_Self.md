# Count of Smaller Numbers After Self

## Problem Statement
Given an array of integers, find the count of smaller numbers after self for each element in the array. The count of smaller numbers after self for an element at index `i` is the number of elements in the array with indices greater than `i` that have values less than the value at index `i`. The function should return an array of these counts. For example, given the array `[5, 2, 6, 1]`, the output should be `[2, 1, 1, 0]`. The constraints are that the input array will have a length between 1 and 10^5, and the values in the array will be between 0 and 10^4.

## Approach
The approach is to use a Binary Indexed Tree (BIT) to keep track of the count of smaller numbers. We iterate over the array from right to left, and for each element, we use the BIT to find the count of smaller numbers to its right. We then update the BIT to include the current element.

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
    int size;

    BIT(int n) {
        size = n;
        tree.resize(n + 1, 0);
    }

    void update(int i, int val) {
        while (i <= size) {
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
    vector<int> ranks;
    for (int num : nums) {
        ranks.push_back(num);
    }
    sort(ranks.begin(), ranks.end());
    map<int, int> rankMap;
    for (int i = 0; i < ranks.size(); i++) {
        rankMap[ranks[i]] = i + 1;
    }

    BIT bit(ranks.size() + 1);
    vector<int> result(nums.size());
    for (int i = nums.size() - 1; i >= 0; i--) {
        result[i] = bit.query(rankMap[nums[i]] - 1);
        bit.update(rankMap[nums[i]], 1);
    }
    return result;
}

int main() {
    vector<int> nums = {5, 2, 6, 1};
    vector<int> result = countSmaller(nums);
    for (int num : result) {
        cout << num << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: [5, 2, 6, 1]
Output: [2, 1, 1, 0]
Input: [1, 2, 3, 4]
Output: [0, 0, 0, 0]
```

## Key Takeaways
- The Binary Indexed Tree (BIT) is a data structure that allows for efficient range sum queries and updates.
- The BIT is particularly useful for solving problems that involve counting or summing elements in a range.
- The time complexity of the solution is O(n log n) due to the use of the BIT and the sorting of the input array.