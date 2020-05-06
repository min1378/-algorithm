function solution(n, t, m, p) {
    var answer = '';
    const end = m * t
    let check = 0
    for (var i = 0; i < end; i ++){
        const number = i.toString(n)
        console.log(number.length)
    }
    return answer;
}


console.log(solution(2, 4, 2, 1)) // "0111"