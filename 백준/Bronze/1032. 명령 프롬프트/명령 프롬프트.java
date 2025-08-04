import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
          Scanner scanner = new Scanner(System.in);

        int n = Integer.parseInt(scanner.nextLine()); // 입력 문자열 개수
        String[] inputs = new String[n];

        for (int i = 0; i < n; i++) {
            inputs[i] = scanner.nextLine();
        }

        int length = inputs[0].length();

        // 길이만큼 Set 배열 생성
        Set<Character>[] charSets = new HashSet[length];
        for (int i = 0; i < length; i++) {
            charSets[i] = new HashSet<>();
        }

        // 각 문자열의 각 자리 문자들을 해당 위치 Set에 추가
        for (String s : inputs) {
            for (int i = 0; i < length; i++) {
                charSets[i].add(s.charAt(i));
            }
        }

        // 결과 문자열 만들기
        StringBuilder result = new StringBuilder();
        for (Set<Character> set : charSets) {
            if (set.size() >= 2) {
                result.append('?');
            } else {
                // set에 하나만 있는 문자 가져오기
                result.append(set.iterator().next());
            }
        }

        System.out.println(result.toString());

        scanner.close();
    }
}