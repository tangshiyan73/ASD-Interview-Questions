// Problem 9: Directed graph path existence + shortest path (BFS).
// BFS explores nodes in increasing distance order, so the first time it
// reaches `end` is guaranteed to be via a shortest path (equal edge weights).

#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

struct PathResult {
    bool exists;
    std::vector<std::string> path;
};

class Graph {
public:
    void addEdge(const std::string& from, const std::string& to) {
        adjacency[from].push_back(to);
        adjacency[to]; // ensure `to` is registered even with no outgoing edges
    }

    // registers a node with no edges (e.g. isolated nodes)
    void addNode(const std::string& label) {
        adjacency[label];
    }

    PathResult findPath(const std::string& start, const std::string& end) {
        if (adjacency.find(start) == adjacency.end()) {
            return { false, {} };
        }
        if (start == end) {
            return { true, { start } };
        }

        std::queue<std::string> queue;
        std::unordered_map<std::string, std::string> cameFrom;
        std::unordered_set<std::string> visited;

        queue.push(start);
        visited.insert(start);

        while (!queue.empty()) {
            std::string current = queue.front();
            queue.pop();

            for (const auto& neighbor : adjacency[current]) {
                if (visited.find(neighbor) == visited.end()) {
                    visited.insert(neighbor); // mark visited on discovery, not on dequeue,
                                               // to avoid queuing the same node twice
                    cameFrom[neighbor] = current;
                    if (neighbor == end) {
                        return { true, reconstructPath(cameFrom, start, end) };
                    }
                    queue.push(neighbor);
                }
            }
        }
        return { false, {} }; // queue exhausted, end was never reached
    }

private:
    std::unordered_map<std::string, std::vector<std::string>> adjacency;

    std::vector<std::string> reconstructPath(
        std::unordered_map<std::string, std::string>& cameFrom,
        const std::string& start,
        const std::string& end) {
        std::vector<std::string> path;
        std::string node = end;
        // walk backward from end to start using the cameFrom trail
        while (node != start) {
            path.push_back(node);
            node = cameFrom[node];
        }
        path.push_back(start);
        // built in reverse (end -> start), so flip it
        std::reverse(path.begin(), path.end());
        return path;
    }
};
