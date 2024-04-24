import Foundation

func solution(_ n:Int) -> Int
{
    var temp = String(n).compactMap { Int(String($0)) }

    return temp.reduce(0) {$0 + $1}
}