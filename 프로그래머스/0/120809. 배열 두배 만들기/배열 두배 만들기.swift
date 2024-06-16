import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    var arr = [Int]()
    for i in (0..<numbers.count) {
        arr.append(numbers[i] * 2)
    }
    return arr
}