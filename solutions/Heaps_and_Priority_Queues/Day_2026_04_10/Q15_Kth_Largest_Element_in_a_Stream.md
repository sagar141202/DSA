# Kth Largest Element in a Stream

## Problem Statement
Given an integer `k` and a stream of integers, design an algorithm to find the `k`th largest element in the stream. The stream is an unbounded sequence of integers that are generated on the fly, and you cannot store the entire stream in memory. The algorithm should return the `k`th largest element seen so far after each new integer is added to the stream. For example, if `k = 3` and the stream is `[4, 5, 8, 2]`, the algorithm should return `4` after the first integer, `5` after the second integer, and `5` after the third integer. If `k` is larger than the number of elements seen so far, the algorithm should return `-1`.

## Approach
We can use a min-heap to store the `k` largest elements seen so far. When a new integer is added to the stream, we check if the heap has less than `k` elements or if the new integer is larger than the smallest element in the heap. If so, we add the new integer to the heap and remove the smallest element if the heap has more than `k` elements.

## Complexity
- Time: O(log k) for each insertion
- Space: O(k) for storing the min-heap

## C++ Solution
```cpp
#include <queue>
using namespace std;

class KthLargest {
public:
    priority_queue<int, vector<int>, greater<int>> minHeap;
    int k;

    KthLargest(int k) : k(k) {}

    int add(int val) {
        // If the heap has less than k elements, add the new integer
        if (minHeap.size() < k) {
            minHeap.push(val);
        }
        // If the new integer is larger than the smallest element in the heap, add it and remove the smallest element
        else if (val > minHeap.top()) {
            minHeap.pop();
            minHeap.push(val);
        }
        // Return the kth largest element (the smallest element in the heap)
        return minHeap.size() < k ? -1 : minHeap.top();
    }
};
```

## Test Cases
```
Input: k = 3, stream = [4, 5, 8, 2]
Output: [4, 5, 5, 5]
Input: k = 1, stream = [1, 2, 3]
Output: [1, 2, 3]
```

## Key Takeaways
- Use a min-heap to efficiently store and retrieve the kth largest element
- The time complexity is O(log k) for each insertion, making it suitable for large streams
- The space complexity is O(k), which is reasonable for most use cases