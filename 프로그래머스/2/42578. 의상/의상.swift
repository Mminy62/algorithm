func solution(_ clothes: [[String]]) -> Int {
    var answer = 0
    var obj = [String: [String]]()

    for i in clothes {
        let key = i[1]

        if obj[key] == nil {
            obj[key] = [i[0]]
        } else {
            obj[key]?.append(i[0])
        }
    }

    answer = 1

    for (_, value) in obj {
        answer *= (value.count + 1)
    }

    answer -= 1

    return answer
}