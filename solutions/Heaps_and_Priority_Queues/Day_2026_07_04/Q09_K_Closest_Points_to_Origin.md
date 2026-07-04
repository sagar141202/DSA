# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2 - x1)^2 + (y2 - y1)^2). Return the k closest points. You may return the answer in any order. The answer is guaranteed to be unique (no two points have the same distance to the origin).

## Approach
We can use a priority queue to store the points along with their distances from the origin. The priority queue will automatically sort the points based on their distances. We can then pop the k closest points from the priority queue to get our answer. Alternatively, we can use the nth_element function from the algorithm library to find the kth smallest distance and then filter out the points with distances less than or equal to the kth smallest distance.

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

struct Comparator {
    bool operator()(const Point& p1, const Point& p2) {
        int dist1 = p1.x * p1.x + p1.y * p1.y;
        int dist2 = p2.x * p2.x + p2.y * p2.y;
        return dist1 > dist2;
    }
};

vector<Point> kClosest(vector<Point>& points, int k) {
    priority_queue<Point, vector<Point>, Comparator> pq;
    for (auto& point : points) {
        if (pq.size() < k) {
            pq.push(point);
        } else {
            int dist1 = pq.top().x * pq.top().x + pq.top().y * pq.top().y;
            int dist2 = point.x * point.x + point.y * point.y;
            if (dist2 < dist1) {
                pq.pop();
                pq.push(point);
            }
        }
    }
    vector<Point> result;
    while (!pq.empty()) {
        result.push_back(pq.top());
        pq.pop();
    }
    return result;
}

// Alternatively, using nth_element function
vector<Point> kClosestAlternative(vector<Point>& points, int k) {
    vector<int> distances;
    for (auto& point : points) {
        distances.push_back(point.x * point.x + point.y * point.y);
    }
    nth_element(distances.begin(), distances.begin() + k - 1, distances.end());
    vector<Point> result;
    for (auto& point : points) {
        int dist = point.x * point.x + point.y * point.y;
        if (dist <= distances[k - 1]) {
            result.push_back(point);
        }
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
- We can use a priority queue to efficiently find the k closest points to the origin.
- The time complexity of the solution using a priority queue is O(n log k), where n is the number of points.
- Alternatively, we can use the nth_element function to find the kth smallest distance and then filter out the points with distances less than or equal to the kth smallest distance.