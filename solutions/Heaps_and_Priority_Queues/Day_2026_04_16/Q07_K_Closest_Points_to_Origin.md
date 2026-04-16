# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2-x1)^2 + (y2-y1)^2). If two points have the same distance to the origin, their order in the result does not matter. The constraints are 1 <= k <= points.length <= 10^4 and -10^4 <= xi, yi <= 10^4.

## Approach
We can use a priority queue to store the points based on their distance from the origin. The priority queue will automatically keep track of the k closest points. We can also use the sort function with a custom comparator to sort the points based on their distance from the origin.

## Complexity
- Time: O(n log k)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Point {
    int x, y;
};

struct Comparator {
    bool operator()(const Point& a, const Point& b) {
        int distA = a.x * a.x + a.y * a.y;
        int distB = b.x * b.x + b.y * b.y;
        return distA > distB;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<Point, vector<Point>, Comparator> pq;
    for (auto& point : points) {
        Point p;
        p.x = point[0];
        p.y = point[1];
        pq.push(p);
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

// Alternatively, we can use sort function
vector<vector<int>> kClosestSort(vector<vector<int>>& points, int k) {
    sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
        int distA = a[0] * a[0] + a[1] * a[1];
        int distB = b[0] * b[0] + b[1] * b[1];
        return distA < distB;
    });
    return vector<vector<int>>(points.begin(), points.begin() + k);
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
- We can use a priority queue to efficiently find the k closest points to the origin.
- The time complexity is O(n log k) where n is the number of points, because we are pushing and popping elements from the priority queue.
- The space complexity is O(n) because we are storing all points in the priority queue.