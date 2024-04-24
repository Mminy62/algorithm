func solution(_ n:Int64) -> Int64 {
    
    // 정수를 문자열로 변환하여 각 자릿수를 문자 배열로 만듭니다.
    let digits = String(n).compactMap { Int(String($0)) }
    
    // 자릿수를 내림차순으로 정렬합니다.
    let sortedDigits = digits.sorted(by: >)
    
    // 내림차순으로 정렬된 자릿수 배열을 다시 정수로 변환합니다.
    let sortedNumber = Int(sortedDigits.map { String($0) }.joined()) ?? 0
    
    return Int64(sortedNumber)
}