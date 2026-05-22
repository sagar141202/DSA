# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. If there are multiple closest elements, return the ones with the smallest values. For example, given `arr = [1, 2, 3, 4, 5]`, `k = 4`, and `x = 3`, the output should be `[1, 2, 3, 4]`. The array `arr` has a length of `n`, where `1 <= n <= 10^4`, `1 <= k <= n`, and `x` is an integer.

## Approach
The algorithm uses a two-pointer technique to find the closest elements. It calculates the absolute difference between each element and the target value `x`, then uses this difference to determine the closest elements. The solution involves sorting the array based on the difference and the value itself, then selecting the `k` closest elements.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> findKClosestElements(vector<int>& arr, int k, int x) {
    // Calculate the absolute difference between each element and the target value x
    vector<pair<int, int>> diff;
    for (int num : arr) {
        diff.push_back({abs(num - x), num});
    }
    
    // Sort the array based on the difference and the value itself
    sort(diff.begin(), diff.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        if (a.first == b.first) {
            return a.second < b.second;
        }
        return a.first < b.first;
    });
    
    // Select the k closest elements
    vector<int> result;
    for (int i = 0; i < k; i++) {
        result.push_back(diff[i].second);
    }
    
    // Sort the result array in ascending order
    sort(result.begin(), result.end());
    
    return result;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    int k = 4;
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
Input: arr = [1, 2, 3, 4, 5], k = 4, x = 3
Output: [1, 2, 3, 4]
Input: arr = [1, 5, 10, 15, 20], k = 3, x = 8
Output: [1, 5, 10]
```

## Key Takeaways
- The two-pointer technique can be used to find the closest elements in a sorted array.
- Sorting the array based on the difference and the value itself ensures that the closest elements are selected.
- The solution has a time complexity of O(n log n) due to the sorting operation.