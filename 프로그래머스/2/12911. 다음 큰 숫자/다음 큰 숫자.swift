import Foundation

func solution(_ n:Int) -> Int
{
    var answer:Int = 0
    var num = n
    var numBin = String(n, radix: 2).filter{ $0 == "1" }.count
    var tempBin = 0
    var temp = num
    
    while numBin != tempBin {
        temp += 1
        tempBin = String(temp, radix: 2).filter{ $0 == "1" }.count
    }
    
    
    return temp
}