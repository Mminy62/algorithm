var temp = readLine()!.split(separator: " ").map{ Int($0)! }
var N = temp[0]
var K = temp[1]

var items = [(Int, Int)]()
items.append((0, 0))
for _ in 1...N {
    let temp = readLine()!.split(separator: " ").map{ Int($0)! }
    items.append((temp[0], temp[1]))
}

// col - 무게, row - 물건별
var dp = Array(repeating: [Int](repeating: 0, count: K + 1), count: N + 1)

for i in 1...N {
    let (W, V) = items[i]
    for k in 1...K {
        if k - W >= 0 {
            dp[i][k] = max(dp[i - 1][k - W] + V, dp[i - 1][k])
        } else {
            dp[i][k] = max(dp[i][k - 1], dp[i - 1][k])
        }
       
    }
}

print(dp[N].last!)
