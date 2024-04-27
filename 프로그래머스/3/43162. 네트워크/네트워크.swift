import Foundation

func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    var answer = 0
    var graph = [[Int]]()
    // graph 초기화
    for i in 0..<n {
        graph.append([-1])
    }
    
    for i in 0...computers.count - 1 {
        for j in 0...computers[0].count - 1 {
            if i == j { continue }
            if computers[i][j] == 1 {
                if graph[i] == [-1] {
                    graph[i] = [j]
                } else { graph[i].append(j) }
            }
        }
    }

    var visited = [Bool](repeating: false, count: n)
    
    func bfs(_ start: Int) -> Bool {
        var queue = [Int]()
        queue.append(start)
        
        if visited[start] {
            return false
        }

        while !queue.isEmpty {
            var node = queue.removeFirst()
            if node == -1 {
                continue
            }

            if !visited[node] {
                visited[node] = true
                queue += graph[node]
            }
        }
        return true
    }
    
    for i in 0...n-1 {
        if bfs(i) {
            answer += 1
        }
    }
    
    return answer
}