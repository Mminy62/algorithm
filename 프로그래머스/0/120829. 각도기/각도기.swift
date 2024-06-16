import Foundation

func solution(_ angle:Int) -> Int {
    var ans = 0
    if angle < 90 {
        ans = 1
    } else if angle == 90 {
        ans = 2
    } else if angle == 180{
        ans = 4
    } else {
        ans = 3
    }
    return ans
}