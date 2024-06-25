import Foundation

func solution(_ left:Int, _ right:Int) -> Int {
    var result = 0
    for num in left...right {
        var cnt = Set<Int>()
        // 숫자별로 약수 개수 파악
        for v in 1...Int(sqrt(Double(num))) {
            var tmp = 0
            if num % v == 0 {
                tmp = num / v // 2 7 4 4
                cnt.insert(v)
                cnt.insert(tmp)
            }
        }
        if cnt.count % 2 == 0 { 
            result += num
        } else {
            result -= num
        }

    }
    return result
}