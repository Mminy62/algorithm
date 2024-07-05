import Foundation

let tc = Int(readLine()!)
for _ in 1...tc! {
    let n = Int(readLine()!)!
    var clothes = [String:Int]()
    var ans = 1
    for _ in 0..<n {
        let input = readLine()!.components(separatedBy: " ")
        let k = input[1]
        clothes[k, default: 1] += 1
    }
    
    // 종류의 count 길이만큼, 종류 combi를 만들어서 곱한다.
    let types = clothes.keys
    for type in types {
        ans *= clothes[type]!
    }

    
    print(ans - 1)
}
