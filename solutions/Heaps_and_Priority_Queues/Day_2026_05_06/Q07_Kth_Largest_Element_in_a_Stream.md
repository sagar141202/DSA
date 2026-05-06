# Kth Largest Element in a Stream

## Problem Statement
Given an integer `k` and a stream of integers, design a data structure to find the `k`th largest element in the stream at any given time. The stream can be thought of as a sequence of integers that are generated on the fly, and we need to find the `k`th largest element in the stream seen so far. The integers in the stream can be positive, negative, or zero, and `k` is a positive integer. For example, if the stream is `[4, 5, 8, 2]` and `k = 3`, the `k`th largest element is `4`.

## Approach
We can use a min-heap data structure to solve this problem efficiently. The min-heap will store the `k` largest elements seen so far in the stream. When a new element is added to the stream, we check if the min-heap has less than `k` elements. If it does, we add the new element to the min-heap. If the min-heap already has `k` elements, we compare the new element with the smallest element in the min-heap (the root of the min-heap). If the new element is larger, we remove the smallest element from the min-heap and add the new element.

## Complexity
- Time: O(log k) for adding an element to the min-heap and finding the kth largest element
- Space: O(k) for storing the k largest elements in the min-heap

## C++ Solution
```cpp
#include <queue>
using namespace std;

class KthLargest {
private:
    int k;
    priority_queue<int, vector<int>, greater<int>> minHeap;

public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (int num : nums) {
            add(num);
        }
    }

    int add(int val) {
        if (minHeap.size() < k) {
            minHeap.push(val);
        } else if (val > minHeap.top()) {
            minHeap.pop();
            minHeap.push(val);
        }
        return minHeap.top();
    }
};
```

## Test Cases
```
Input: k = 3, stream = [4, 5, 8, 2]
Output: 4
```

## Key Takeaways
- Use a min-heap to store the k largest elements seen so far in the stream
- When a new element is added to the stream, compare it with the smallest element in the min-heap and update the min-heap accordingly
- The time complexity of adding an element to the min-heap and finding the kth largest element is O(log k)