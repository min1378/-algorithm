function solution(answers) {
    const first = [1, 2, 3, 4, 5]
    const second = [2, 1, 2, 3, 2, 4, 2, 5]
    const third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    const check = [0, 0, 0]
    for (const index in answers) {
        const ans = answers[index]
        if (first[index % 5] == ans) {
            check[0] += 1
        }
        if (second[index % 8] == ans) {
            check[1] += 1
        }
        if (third[index % 10] == ans) {
            check[2] += 1
        }

    }
    var answer = [];
    const maxCount = Math.max.apply(null, check)
    for (const index in check) {
        console.log(index, maxCount)
        if (check[index] == maxCount) {
            answer.push(Number(index) + 1)
        }
    }

    return answer;
}

console.log(solution([1, 2, 3, 4, 5]))