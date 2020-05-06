function checkZero(array, n){
    if (array.length != n){
        var temp = "0".repeat(n - array.length)
        array = temp + array
        
    }
    return array
}

function solution(n, arr1, arr2) {
    var answer = [];
    for(var i= 0; i < n; i++){
        var first = arr1[i].toString(2)
        var second = arr2[i].toString(2)
        var newFirst = checkZero(first, n)
        var newSecond = checkZero(second, n)
        var result = ""
        for(var j = 0; j < n; j++){
            if(newFirst[j] | newSecond[j]){
                result += "#"
            }
            else{
                result += " "
            }
        }
        answer.push(result)
    }
    
    return answer;
}

console.log(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))