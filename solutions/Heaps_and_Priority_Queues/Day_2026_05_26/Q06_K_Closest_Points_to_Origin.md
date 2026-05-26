# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2 - x1)^2 + (y2 - y1)^2). Return the k closest points. You may return the answer in any order. The answer is guaranteed to be unique (no two different points are the same distance away from the origin).

## Approach
We will use a priority queue to store the points along with their distances from the origin. The priority queue will be ordered based on the distance, so the point with the smallest distance will always be at the top. We will then pop the top k points from the priority queue to get the k closest points.

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

struct Compare {
    bool operator()(const Point& a, const Point& b) {
        // Calculate the squared distance from the origin for each point
        int distA = a.x * a.x + a.y * a.y;
        int distB = b.x * b.x + b.y * b.y;
        
        // If the distances are different, return true if distA is greater than distB
        if (distA != distB) {
            return distA > distB;
        }
        
        // If the distances are the same, return true if the x-coordinates are different
        if (a.x != b.x) {
            return a.x > b.x;
        }
        
        // If the x-coordinates are the same, return true if the y-coordinates are different
        return a.y > b.y;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<Point, vector<Point>, Compare> pq;
    
    // Push all points into the priority queue
    for (const auto& point : points) {
        Point p = {point[0], point[1]};
        pq.push(p);
        
        // If the size of the priority queue exceeds k, pop the top element
        if (pq.size() > k) {
            pq.pop();
        }
    }
    
    // Create the result vector
    vector<vector<int>> result;
    while (!pq.empty()) {
        Point p = pq.top();
        pq.pop();
        result.push_back({p.x, p.y});
    }
    
    return result;
}
```

## Test Cases
```
Input: points = [[1, 3], [-2, 2]], k = 1
Output: [[-2, 2]]
Input: points = [[3, 3], [5, -1], [-2, 4]], k = 2
Output: [[3, 3], [-2, 4]]
```

## Key Takeaways
- We use a priority queue to efficiently find the k closest points to the origin.
- The priority queue is ordered based on the squared distance from the origin to avoid calculating the square root.
- We only store the top k points in the priority queue to reduce memory usage.