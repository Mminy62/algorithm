import Foundation

func solution(_ number:String, _ k:Int) -> String {
    var stack = [Character]()
    var k = k
    var answer = ""
    
    for num in Array(number){
        if !stack.isEmpty && stack.last! < num {
            // while stack 
            while !stack.isEmpty && stack.last! < num && k > 0 {
                stack.removeLast()
                k -= 1
            }
            stack.append(num)
        } else {
            stack.append(num)
        }
    }
    
    return String(stack.prefix(number.count - k))
}