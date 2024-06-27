func solution(_ s:String) -> String {
    // 문자인 경우, 
    // 앞에 빈칸인 경우만 대문자로 바꿔주고, 
    // 나머지는 전부 소문자로 바꾼다. 
    
    var sentence = " " + s
    var result = ""
    let startIndex = sentence.index(sentence.startIndex, offsetBy: 1)
    var preC = sentence.first
    
    for c in sentence[startIndex..<sentence.endIndex] {
        if c.isLetter {
            if preC == " " {
                result += c.uppercased() 
            }
            else {
                result += c.lowercased()
            }
        } else {
            result += String(c)
        }
        
        preC = c
    }
    
    
    return result
}