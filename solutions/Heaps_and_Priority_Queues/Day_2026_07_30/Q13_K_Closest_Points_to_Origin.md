# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2-x1)^2 + (y2-y1)^2). If two points have the same distance to the origin, their order does not matter. Return the k closest points. You may return the answer in any order. The number of points, n, will be in the range [1, 10^4], and 1 <= k <= n.

## Approach
We use a max heap to store points based on their distance to the origin. The heap will keep track of the k closest points seen so far. We iterate through each point, calculate its distance, and push it into the heap if it's not full or if the point is closer than the farthest point in the heap.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Point {
    int x, y;
};

struct compare {
    bool operator()(const Point& a, const Point& b) {
        return (a.x * a.x + a.y * a.y) > (b.x * b.x + b.y * b.y);
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    // Create a max heap to store points
    priority_queue<Point, vector<Point>, compare> maxHeap;
    
    // Iterate through each point
    for (auto& point : points) {
        Point p = {point[0], point[1]};
        
        // If heap is not full, push the point into the heap
        if (maxHeap.size() < k) {
            maxHeap.push(p);
        }
        // If the point is closer than the farthest point in the heap
        else if ((p.x * p.x + p.y * p.y) < (maxHeap.top().x * maxHeap.top().x + maxHeap.top().y * maxHeap.top().y)) {
            maxHeap.pop();
            maxHeap.push(p);
        }
    }
    
    // Convert the heap to a vector and return
    vector<vector<int>> result;
    while (!maxHeap.empty()) {
        Point p = maxHeap.top();
        maxHeap.pop();
        result.push_back({p.x, p.y});
    }
    return result;
}
```

## Test Cases
```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
```

## Key Takeaways
- We use a max heap to efficiently keep track of the k closest points.
- The distance of a point to the origin is calculated as sqrt(x^2 + y^2), but we can compare distances without taking the square root.
- The time complexity is O(n log k) because we perform a heap operation for each point, and each heap operation takes O(log k) time.