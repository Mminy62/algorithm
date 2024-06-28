import Foundation

func solution(_ s:String) -> Int{
    var s = s
    
    while true {
        var stack = [Character]()
        for c in s {
             if let last = stack.last, last == c {
                stack.removeLast()
            } else {
                stack.append(c)
            }
        }
        
        if stack.isEmpty {
            return 1
        } else if s.count == stack.count {
            return 0
        } else {
            s = stack.map{String($0)}.joined(separator: "")
        }
        
    }
    
    return 0
}