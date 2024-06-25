import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {
    var result = 0
    for item in Array(zip(a, b)) {
        result += item.0 * item.1
    }
    return result
}