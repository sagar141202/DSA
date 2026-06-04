# Kth Largest Element in a Stream

## Problem Statement
Given an integer `k` and a stream of integers, design a data structure to find the `k`th largest element in the stream. The stream can contain duplicate integers and the integers can be positive or negative. The data structure should support the following operations: 
- `KthLargest(int k, int[] nums)`: Initializes the data structure with the integer `k` and the stream of integers `nums`.
- `add(int val)`: Adds the integer `val` to the stream and returns the `k`th largest element in the stream.
The constraints are: `1 <= k <= 10^4`, `1 <= nums.length <= 10^5`, `10^4 <= nums[i] <= 10^4`, and `10^4 <= val <= 10^4`.

## Approach
We will use a min-heap data structure to store the `k` largest elements in the stream. The heap will be initialized with the first `k` elements of the stream. Then, for each subsequent element in the stream, we will check if the heap size is less than `k` or if the new element is greater than the smallest element in the heap. If either condition is true, we will add the new element to the heap and remove the smallest element if the heap size exceeds `k`.

## Complexity
- Time: O(N log k) where N is the number of elements in the stream
- Space: O(k)

## C++ Solution
```cpp
#include <queue>
using namespace std;

class KthLargest {
private:
    int k;
    priority_queue<int, vector<int>, greater<int>> minHeap;

public:
    KthLargest(int k, vector<int>& nums) : k(k) {
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
Input: KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
Output: 
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);    // returns 8
```

## Key Takeaways
- Use a min-heap to store the `k` largest elements in the stream.
- Initialize the heap with the first `k` elements of the stream.
- For each subsequent element, add it to the heap if the heap size is less than `k` or if the new element is greater than the smallest element in the heap.