function solution(priorities, location) {
    let count = 0
    while (true) {
        let max = 0
        if (priorities.length < 2) max = priorities[0]
        else max = priorities.reduce((a, b) => a > b ? a : b)
        let check = priorities.shift() // 앞에서빼는거
        console.log(check, priorities, location, max)
        // console.log(check, max, priorities)
        if (check < max) {
            priorities.push(check)
            if (location == 0) location = priorities.length - 1
            else location--
        } else {
            count++
            // console.log("hi", check, priorities)
            if (location == 0) return count
            else location--

        }
    }
}

console.log(solution([1, 2, 3], 0))