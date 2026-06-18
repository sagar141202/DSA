# Find K Closest Elements

## Problem Statement
Given a sorted array, find the K closest elements to a target value. The array is sorted in ascending order, and the target value can be any integer. The K closest elements are the K elements in the array that have the smallest absolute difference with the target value. If there are multiple elements with the same smallest absolute difference, the elements with the smaller value should be included first. For example, if the array is [1, 2, 3, 4, 5] and the target value is 3, the 3 closest elements are [2, 3, 4]. If the array is [1, 5, 10, 15, 20] and the target value is 8, the 3 closest elements are [5, 10, 15].

## Approach
The approach is to use a two-pointer technique to find the K closest elements. We first find the index of the closest element to the target value using a binary search. Then, we expand outwards from this index to find the K closest elements. We use a priority queue to keep track of the K closest elements.

## Complexity
- Time: O(N log N) for sorting, O(log N) for binary search, and O(K) for expanding outwards, where N is the number of elements in the array.
- Space: O(K) for storing the K closest elements.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> findKClosestElements(vector<int>& arr, int k, int x) {
    // Find the index of the closest element to the target value using binary search
    int left = 0, right = arr.size() - k;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (x - arr[mid] > arr[mid + k] - x) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    // Return the K closest elements
    return vector<int>(arr.begin() + left, arr.begin() + left + k);
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    int k = 3;
    int x = 3;
    vector<int> result = findKClosestElements(arr, k, x);
    for (int num : result) {
        cout << num << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: arr = [1, 2, 3, 4, 5], k = 3, x = 3
Output: [2, 3, 4]
Input: arr = [1, 5, 10, 15, 20], k = 3, x = 8
Output: [5, 10, 15]
```

## Key Takeaways
- Use binary search to find the index of the closest element to the target value.
- Expand outwards from the index to find the K closest elements.
- Use a two-pointer technique to efficiently find the K closest elements.