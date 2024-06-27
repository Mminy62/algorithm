import Foundation

func solution(_ s:String) -> [Int] {
    var cur = s
    var pre = s
    var zeroCnt = 0
    var turn = 0
    
    while cur != "1" {
        cur = cur.replacingOccurrences(of: "0", with: "")
        zeroCnt += pre.count - cur.count
        
        // 이진법으로 변환
        cur = String(cur.count, radix: 2)
        turn += 1
        pre = cur
    }
    
    
    return [turn, zeroCnt]
}