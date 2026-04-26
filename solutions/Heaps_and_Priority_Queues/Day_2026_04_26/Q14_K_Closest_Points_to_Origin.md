# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2 - x1)^2 + (y2 - y1)^2). If two points have the same distance from the origin, their order in the result does not matter. The constraints are 1 <= k <= points.length <= 10^4 and -10^4 <= xi, yi <= 10^4.

## Approach
The algorithm uses a priority queue to store points based on their distance from the origin. We iterate over all points, calculate their distance, and push them into the priority queue. The priority queue automatically orders points based on their distance. We then pop the k closest points from the queue.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Point {
    int x, y;
    Point(int x, int y) : x(x), y(y) {}
};

struct compare {
    bool operator()(const Point& a, const Point& b) {
        int distA = a.x * a.x + a.y * a.y;
        int distB = b.x * b.x + b.y * b.y;
        return distA > distB;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<Point, vector<Point>, compare> pq;
    for (auto& point : points) {
        pq.push(Point(point[0], point[1]));
        if (pq.size() > k) {
            pq.pop();
        }
    }
    
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
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
```

## Key Takeaways
- We use a min-heap (priority queue) to efficiently find the k closest points.
- The time complexity is O(n log k) because we are pushing and popping from the priority queue for each point.
- The space complexity is O(k) because in the worst case, the size of the priority queue will be k.