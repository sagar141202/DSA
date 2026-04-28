# Sliding Window Median

## Problem Statement
The Sliding Window Median problem is a classic problem that involves finding the median of a given array within a sliding window of size k. The array is of size n, and we need to find the median for each window of size k. The constraints are 1 <= k <= n <= 10^5, and the array elements are integers in the range [-10^5, 10^5]. For example, given the array [1, 3, -1, -3, 5, 3, 6, 7] and k = 3, the medians for each window are [1, -1, -1, 3, 5, 6].

## Approach
We will use two heaps, a max heap to store the smaller half of the window and a min heap to store the larger half. The max heap will store the k/2 smaller elements, and the min heap will store the k/2 larger elements. We will maintain the balance between the two heaps to ensure the median can be calculated efficiently.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
public:
    priority_queue<int> maxHeap; // max heap to store smaller half
    priority_queue<int, vector<int>, greater<int>> minHeap; // min heap to store larger half

    void addNum(int num) {
        // add num to the correct heap
        if (maxHeap.empty() || num <= maxHeap.top()) {
            maxHeap.push(num);
        } else {
            minHeap.push(num);
        }

        // balance the heaps
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }

    double findMedian() {
        // calculate the median
        if (maxHeap.size() == minHeap.size()) {
            return (maxHeap.top() + minHeap.top()) / 2.0;
        } else {
            return (double)maxHeap.top();
        }
    }

    vector<double> getMedians(vector<int>& nums, int k) {
        vector<double> medians;
        for (int i = 0; i < nums.size(); i++) {
            addNum(nums[i]);
            if (i >= k) {
                // remove the oldest num from the heaps
                if (maxHeap.top() <= nums[i - k]) {
                    maxHeap.pop();
                } else {
                    minHeap.pop();
                }
            }
            if (i >= k - 1) {
                medians.push_back(findMedian());
            }
        }
        return medians;
    }
};

int main() {
    MedianFinder mf;
    vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    vector<double> medians = mf.getMedians(nums, k);
    for (double median : medians) {
        cout << median << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
```

## Key Takeaways
- We use two heaps to maintain the balance between the smaller and larger halves of the window.
- The max heap stores the k/2 smaller elements, and the min heap stores the k/2 larger elements.
- We add and remove elements from the heaps while maintaining the balance to ensure the median can be calculated efficiently.