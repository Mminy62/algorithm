import Foundation

func solution(_ s:String) -> Bool
{
    var stack = [Character]()
    
    for c in s {
        if c == "(" {
            stack.append("(")
        } else {
            guard stack.last == "(" else { return false }
            stack.popLast()
        }
    }
    
    return stack.isEmpty ? true : false
}