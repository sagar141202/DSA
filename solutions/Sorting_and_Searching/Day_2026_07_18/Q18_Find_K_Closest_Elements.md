# Find K Closest Elements

## Problem Statement
Given a sorted array `arr`, an integer `k`, and a target value `x`, find the `k` closest elements to `x` in the array. If there are multiple closest elements, return the first `k` closest elements. The array `arr` contains distinct integers and is sorted in ascending order. The integer `k` is a positive integer, and the target value `x` is an integer.

## Approach
The algorithm involves using a two-pointer technique to find the closest elements. We initialize two pointers, one at the start and one at the end of the array, and then move them based on the comparison of the elements with the target value. We use a priority queue or sorting to find the `k` closest elements.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> findKClosestElements(vector<int>& arr, int k, int x) {
    // Calculate the absolute difference between each element and the target value
    vector<pair<int, int>> diff;
    for (int i = 0; i < arr.size(); i++) {
        diff.push_back({abs(arr[i] - x), arr[i]});
    }
    
    // Sort the elements based on the absolute difference
    sort(diff.begin(), diff.end());
    
    // Get the k closest elements
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
    int k = 3;
    int x = 3;
    vector<int> result = findKClosestElements(arr, k, x);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: arr = [1, 2, 3, 4, 5], k = 3, x = 3
Output: [2, 3, 4]
Input: arr = [1, 5, 10, 15, 20], k = 2, x = 8
Output: [5, 10]
```

## Key Takeaways
- Use a two-pointer technique or sorting to find the closest elements.
- Calculate the absolute difference between each element and the target value.
- Use a priority queue or sorting to find the `k` closest elements.