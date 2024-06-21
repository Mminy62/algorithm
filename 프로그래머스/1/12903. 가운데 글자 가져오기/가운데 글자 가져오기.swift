func solution(_ s:String) -> String {
    let length = s.count
    let idx = s.index(s.startIndex, offsetBy: length / 2)
    
    if length % 2 == 1 {
        return String(s[idx])
    } else {
        let beforeIdx = s.index(before: idx)
        return String(s[beforeIdx...idx])
    }
    return ""
    
}