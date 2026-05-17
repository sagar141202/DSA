# Kth Largest Element in a Stream

## Problem Statement
Given an integer `k` and a stream of integers, design an algorithm to find the `k`th largest element in the stream. The stream can be represented as an array of integers, and the `k`th largest element is the `k`th largest number in the sorted array. For example, if the stream is `[4, 5, 8, 2]` and `k` is `3`, the `k`th largest element is `4`. The solution should be efficient and scalable for large streams.

## Approach
We can use a min-heap to store the `k` largest elements seen so far. The min-heap will automatically maintain the smallest element at the top, which will be the `k`th largest element when the heap size is `k`. We iterate through the stream, pushing each element into the heap and popping the smallest element when the heap size exceeds `k`.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <queue>
#include <vector>
using namespace std;

class KthLargest {
public:
    priority_queue<int, vector<int>, greater<int>> min_heap;
    int k;

    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (int num : nums) {
            add(num);
        }
    }

    int add(int val) {
        if (min_heap.size() < k) {
            min_heap.push(val);
        } else if (val > min_heap.top()) {
            min_heap.pop();
            min_heap.push(val);
        }
        return min_heap.top();
    }
};
```

## Test Cases
```
Input: k = 3, stream = [4, 5, 8, 2]
Output: 4
Input: k = 1, stream = [1, 2, 3]
Output: 3
```

## Key Takeaways
- Use a min-heap to store the `k` largest elements seen so far.
- The min-heap automatically maintains the smallest element at the top, which will be the `k`th largest element when the heap size is `k`.
- The time complexity is O(n log k) due to the heap operations, where `n` is the size of the stream.