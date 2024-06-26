func solution(_ s:String) -> String {
    let arr = s.split(separator: " ").compactMap{ Int($0) }
    var result = ""
    result += String(arr.min()!)
    result += " "
    result += String(arr.max()!)
    return result
}