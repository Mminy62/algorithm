var n = Int(readLine()!)!
var result = -Int.max
if let input = readLine() {
    let arr = input.split(separator: " ").compactMap { Int($0) }.sorted()
    var cnt = 0
    let end = n % 2 == 1 ? n - 2 : n - 1

    for i in 0..<(n / 2) {
        let temp = arr[i] + arr[end - i]
        result = max(temp, result)
    }
    
}
print(result)