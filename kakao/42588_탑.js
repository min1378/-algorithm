function checkIndex(check, target) {
    for (let j = check.length - 1; j > -1; j--) {
        if (check[j] > target) return j + 1
    }
    return 0;
}

function solution(heights) {
    var answer = [];
    for (let i = 0; i < heights.length; i++) {
        let check = heights.slice(0, i)
        answer.push(checkIndex(check, heights[i]))
    }
    return answer;
}


console.log(solution([6, 9, 5, 7, 4]))