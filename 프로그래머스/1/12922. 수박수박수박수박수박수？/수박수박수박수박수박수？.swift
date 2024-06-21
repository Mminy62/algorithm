func solution(_ n:Int) -> String {
    var result = ""
    let word = "수박"
    
    result = String(repeating: word, count: n / 2)
    
    if n % 2 == 1 {
        result += "수"
    }
    return result
}