import Foundation

func solution(_ n:Int) -> Int
{
    var temp = n + 1
    
    while n.nonzeroBitCount != temp.nonzeroBitCount {
        temp += 1
    }
    
    return temp
}