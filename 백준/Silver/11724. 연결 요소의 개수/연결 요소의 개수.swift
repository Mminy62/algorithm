import Foundation

let inputCount = readLine()!.components(separatedBy: " ").map { Int($0)! }
var N = inputCount[0]
var M = inputCount[1]

var visited = [Bool](repeating: false, count: N + 1)
var edges = [(Int, Int)]()
var nodes = Array(repeating: [Int](), count: N + 1)
var result = 0

if M == 0 {
    result = N
}
else {
    for _ in 1...M {
        let input = readLine()!.components(separatedBy: " ").map { Int($0)! }
        let a = input[0]
        let b = input[1]
        edges.append((a, b))
        nodes[a].append(b)
        nodes[b].append(a)
    }
    
    for i in 1...N {
        var queue = [Int]()
        if !visited[i] {
            queue.append(i)
            visited[i] = true
            
            while !queue.isEmpty {
                let num = queue.removeFirst()
                for node in nodes[num] {
                    if !visited[node] {
                        queue.append(node)
                        visited[node] = true
                    }
                }
            }
            result += 1
        }
    }
}
print(result)
