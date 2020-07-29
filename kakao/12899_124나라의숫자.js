function solution(n) {
    let answer = '';
    let numbers = ["4", "1", "2"] // 나머지가 0 1 2 에 해당하는 숫자들
    while (n > 0) {
        let reminder = n % 3;
        n = parseInt(n / 3)
        if (reminder == 0) n-- // 나머지가 0일때 1빼줌. 
        answer = numbers[reminder] + answer
    }
    return answer;
}