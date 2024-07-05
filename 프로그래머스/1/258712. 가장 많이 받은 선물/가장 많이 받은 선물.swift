import Foundation
/*
가장 많은 선물을 받는 친구가 받을 선물 수
친구: 선물 수
// 다 다음달에 받는 것
- 선물 주고 받은 기록 O
    - A > B, A가 B에게 선물을 하나 받는다.
    - A == B, 선물 지수가 큰 사람이 작은 사람한테 1개 받는다.

- 기록 X 
    - 선물지수 


*선물지수: 이번 달까지 준 것 - 받은 것 => 즉, 준게 더 많은 사람이 1개 더 받는다.
만약 선물 지수도 같다면, 선물 주고받지 X
*/
func solution(_ friends:[String], _ gifts:[String]) -> Int {
    
    // gifts를 기반으로 dict를 완성 시킨후,
    
    // record 초기화
    var record = [String: [String:Int]]()
    for key in friends {
        record[key] = [String: Int]()
        
        for friend in friends {
            if key != friend {
                record[key]![friend] = 0
            }
        }
    }

    for gift in gifts {
        let input = gift.components(separatedBy: " ")
        let (A, B) = (input[0], input[1])
        record[B]![A]! += 1
    }
    
    
    // 선물지수 미리 구해놓기
    var giftAmount = [String: Int]()
    for A in friends {
        let minus = record[A]!.values.reduce(0, +)
        var receive = 0
        for B in friends {
            if A == B { continue }
            record[B]!.forEach { (key, value) in
                if key == A {
                    receive += record[B]![key]!
                }
            }
        }
        
        giftAmount[A, default: 0] = receive - minus
    }
    
    
    // 각 키별로 주고받은 기록 남김
    var result = [String: Int]()
    for friend in friends {
        result[friend] = 0
    }
    
    for i in 0..<friends.count {
        for j in (i + 1)..<friends.count {
            let A = friends[i]
            let B = friends[j]
            
            let AtoB = record[B]![A]!
            let BtoA = record[A]![B]!
            // 선물 주고 받은 기록 O
            if AtoB > 0 || BtoA > 0 {
                if AtoB > BtoA {
                    result[A]! += 1
                } else if BtoA > AtoB {
                    result[B]! += 1
                } else {
                    // 선물지수 비교
                    if giftAmount[A] == giftAmount[B] { continue }
                    if  giftAmount[A]! > giftAmount[B]! {
                        result[A]! += 1
                    } else {
                        result[B]! += 1
                    }
                    
                }
            }
            else { //기록 X
                // 선물지수 비교
                // 선물지수 비교
                if giftAmount[A] == giftAmount[B] { continue }
                if  giftAmount[A]! > giftAmount[B]! {
                    result[A]! += 1
                } else {
                    result[B]! += 1
                }
            }
        }
    }
    
    return result.values.map{Int($0)}.max()!

}
