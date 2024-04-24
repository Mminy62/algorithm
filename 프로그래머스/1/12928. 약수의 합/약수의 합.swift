func solution(_ n:Int) -> Int {
    var ans: Int = 0
    if n > 0 {
        for i in 1...n {
            if n % i == 0 {
                ans += i
            }
        }
    }
    return ans
}