import Foundation

func solution(_ s:String) -> Bool
{
    var ans:Bool = false
 
    var temp = s.lowercased()
    ans = (temp.filter{ $0 == "p"}).count  == (temp.filter{ $0 == "y"}).count
    return ans
}