var N = Int(readLine()!)!
if let input = readLine() {
    let arr = input.split(separator: " ").compactMap { Int($0) }.sorted()
    
    var result = 0
    var pre = 0
    arr.forEach { time in
        pre += time
        result += pre
    }
    print(result)
}
