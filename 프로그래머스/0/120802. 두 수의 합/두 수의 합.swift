import Foundation

func solution(_ num1:Int, _ num2:Int) -> Int {
    return [num1, num2].reduce(0) {$0 + $1}
    // return num1 + num2
}