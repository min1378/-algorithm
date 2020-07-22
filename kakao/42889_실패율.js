function solution(N, stages) {
    var answer = [];
    for(let stageNumber=1; stageNumber < N+1; stageNumber++){
        answer.push({'stage': stageNumber, 'failrate': stages.filter(element => element === i).length / stages.filter(element => element >= i).length})
    }
    
    return answer.sort((first, second) => {
        if(first.failrate > second.failrate) return -1
        if(first.failrate < second.failrate) return 1
        return first.stage - second.stage
    }).map(element => element.stage)
}