let inputCount = readLine()!.split(separator: " ").map { Int($0)! }
var N = inputCount[0]
var M = inputCount[1]

struct Graph {
    var adjList: [[Int]]
    var visited: [Bool]
    
    init(capacity: Int) {
        self.adjList = Array(repeating: [], count: capacity + 1)
        self.visited = [Bool](repeating: false, count: capacity + 1)
    }
    
    mutating func addEdge(_ u: Int, _ v:Int) {
        adjList[u].append(v)
        adjList[v].append(u)
    }
    
    mutating func dfs(start: Int) {
        visited[start] = true
        
        for node in adjList[start] {
            if !visited[node] {
                dfs(start: node)
            }
        }
    }
    
    mutating func countComponents() -> Int {
        var count = 0
        for i in 1...(visited.count - 1) {
            if !visited[i] {
                dfs(start: i)
                count += 1
            }
        }
        return count
    }
}

var graph = Graph(capacity: N)
var result = 0

if M != 0 {
    for _ in 1...M {
        let input = readLine()!.split(separator: " ").map { Int($0)! }
        let a = input[0]
        let b = input[1]
        graph.addEdge(a, b)
    }
  result = graph.countComponents()
} else {
    result = N
}
print(result)