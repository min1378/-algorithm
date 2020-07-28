function solution(heights) {
    return heights.map((v, i) => {
        console.log(v, i)
        while (i) {
            i--;
            if (heights[i] > v) {
                return i + 1;
            }
        }
        return 0;
    });
}

solution([6, 9, 5, 7, 4])