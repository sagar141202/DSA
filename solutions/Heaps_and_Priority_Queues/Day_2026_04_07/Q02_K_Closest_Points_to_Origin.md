# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2-x1)^2 + (y2-y1)^2). If two points have the same distance to the origin, their order does not matter. Return the k closest points. You can return the answer in any order. The number of points, n, will be in the range [1, 10^4] and k will be in the range [1, n].

## Approach
We can use a priority queue to store points based on their distance from the origin. The priority queue will automatically sort points based on their distance. We then pop the k closest points from the queue.

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
        int distA = a.x * a.x + a.y * a.y;
        int distB = b.x * b.x + b.y * b.y;
        return distA > distB;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<Point, vector<Point>, Compare> pq;
    for (auto& point : points) {
        pq.push({point[0], point[1]});
    }
    vector<vector<int>> result;
    while (k-- > 0) {
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
- Use a priority queue to efficiently find the k closest points.
- Define a custom comparator to calculate the distance from the origin for each point.
- Use a struct to represent points for better readability.