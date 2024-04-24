func solution(_ n:Int64) -> [Int] {
    var temp = String(n)
    return temp.reversed().compactMap { Int(String($0)) }
}