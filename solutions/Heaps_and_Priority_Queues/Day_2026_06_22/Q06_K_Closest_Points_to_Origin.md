# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2-x1)^2 + (y2-y1)^2). If two points have the same distance to the origin, their order does not matter. Return the k closest points.

## Approach
We can use a priority queue to store the points along with their distances from the origin. The priority queue will automatically order the points based on their distances. We can then pop the k closest points from the queue.

## Complexity
- Time: O(N log k)
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
        int distA = a.x * a.x + a.y * a.y;
        int distB = b.x * b.x + b.y * b.y;
        return distA > distB;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<Point, vector<Point>, Compare> pq;
    for (auto& point : points) {
        pq.push({point[0], point[1]});
        if (pq.size() > k) {
            pq.pop();
        }
    }

    vector<vector<int>> result;
    while (!pq.empty()) {
        auto point = pq.top();
        pq.pop();
        result.push_back({point.x, point.y});
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
- Use a priority queue to efficiently find the k closest points.
- Define a custom comparator to order points based on their distances from the origin.
- Use a struct to represent points and make the code more readable.