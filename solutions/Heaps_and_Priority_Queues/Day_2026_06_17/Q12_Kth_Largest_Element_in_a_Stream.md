# Kth Largest Element in a Stream

## Problem Statement
Given an integer `k` and a stream of integers, design a class to find the `kth` largest element in the stream. The class should have a constructor that takes an integer `k` as input and a method `add` that takes an integer `num` as input and returns the `kth` largest element in the stream so far. If the stream has less than `k` elements, return the largest element in the stream. For example, if `k = 3` and the stream is `[4, 5, 8, 2]`, the output should be `4`.

## Approach
We can use a min-heap to store the `k` largest elements in the stream. When a new element is added, we check if the heap has less than `k` elements or if the new element is larger than the smallest element in the heap. If so, we add the new element to the heap and remove the smallest element if the heap has more than `k` elements.

## Complexity
- Time: O(log k) for the `add` method
- Space: O(k) for storing the min-heap

## C++ Solution
```cpp
#include <queue>
using namespace std;

class KthLargest {
private:
    int k;
    priority_queue<int, vector<int>, greater<int>> minHeap;

public:
    KthLargest(int k) : k(k) {}

    int add(int num) {
        if (minHeap.size() < k) {
            minHeap.push(num);
        } else if (num > minHeap.top()) {
            minHeap.pop();
            minHeap.push(num);
        }
        return minHeap.size() < k ? (minHeap.empty() ? -1 : minHeap.top()) : minHeap.top();
    }
};
```

## Test Cases
```
Input: k = 3, stream = [4, 5, 8, 2]
Output: [4, 4, 4, 4]
Input: k = 1, stream = [1, 2, 3]
Output: [1, 2, 3]
```

## Key Takeaways
- Use a min-heap to efficiently store and retrieve the `k` largest elements in the stream.
- The `add` method has a time complexity of O(log k) due to the heap operations.
- The space complexity is O(k) for storing the min-heap.