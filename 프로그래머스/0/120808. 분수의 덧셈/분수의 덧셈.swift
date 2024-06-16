import Foundation

func gcd(_ a:Int, _ b:Int) -> Int {
    if b == 0 {
        return a
    }
    return gcd(b, Int(a % b))
}

func solution(_ numer1:Int, _ denom1:Int, _ numer2:Int, _ denom2:Int) -> [Int] {
    var denom = denom1 * denom2 
    var numer = numer1 * denom2 + numer2 * denom1 
    
    var dd = 0
    if denom > numer {
        dd = gcd(denom, numer)
    } else {
        dd = gcd(numer, denom)
    }

    denom = denom / dd
    numer = numer / dd
    
    return [numer, denom]
}