func solution(_ arr:[Int]) -> [Int] {
    var min_value = arr.min()

    if arr.count > 1 {
        return arr.filter{$0 != min_value}
    }
    return [-1]
}