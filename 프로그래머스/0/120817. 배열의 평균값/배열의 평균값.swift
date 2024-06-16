import Foundation

func solution(_ numbers:[Int]) -> Double {
    var tmp = numbers.reduce(0, +)
    return Double(tmp) / Double(numbers.count)
}