import Foundation

func solution(_ n:Int64) -> Int64 {
    var ans: Int64 = -1
    var i = Int(sqrt(Double(n)))
    if i * i == n {
        ans = Int64((i + 1) * (i + 1))
    }
    
    return ans
}