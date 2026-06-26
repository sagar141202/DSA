# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2 - x1)^2 + (y2 - y1)^2). If there are multiple points with the same distance to the origin, the points with smaller x-coordinates have higher priority, and if the x-coordinates are also the same, the points with smaller y-coordinates have higher priority. Return the k closest points to the origin.

## Approach
We can use a max heap to store the k closest points. The max heap will be ordered by the distance from the origin and then by the x and y coordinates. We iterate over all points, and for each point, we calculate its distance from the origin and push it into the heap if the heap has less than k points. If the heap has k points and the current point is closer to the origin than the point at the top of the heap, we remove the point at the top of the heap and push the current point into the heap.

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
        if (distA != distB) return distA > distB;
        if (a.x != b.x) return a.x > b.x;
        return a.y > b.y;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<Point, vector<Point>, Compare> maxHeap;
    for (auto& point : points) {
        Point p = {point[0], point[1]};
        if (maxHeap.size() < k) {
            maxHeap.push(p);
        } else if (Compare()(p, maxHeap.top())) {
            maxHeap.pop();
            maxHeap.push(p);
        }
    }
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
Input: points = [[1, 3], [-2, 2]], k = 1
Output: [[-2, 2]]
Input: points = [[3, 3], [5, -1], [-2, 4]], k = 2
Output: [[3, 3], [-2, 4]]
```

## Key Takeaways
- We use a max heap to efficiently find the k closest points to the origin.
- The custom comparator function is used to order the points in the heap based on their distance from the origin and their coordinates.
- The time complexity of the solution is O(n log k) due to the use of the heap.