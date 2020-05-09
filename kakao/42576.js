// function solution(participant, completion) {
//     let completionMap = new Map()
//     for (const person of completion) {
//         const mapItem = completionMap.get(person)
//         completionMap.set(person, mapItem ? mapItem + 1 : 1)
//     }

//     for (const person of participant) {
//         const mapItem = completionMap.get(person)
//         if (!mapItem) {
//             return person
//         } else {
//             completionMap.set(person, mapItem - 1)
//         }
//     }
//     var answer = '';
//     return answer;
// }
var solution = (participant, completion) => participant.find(
    name => console.log("hi", name, completion[name], !completion[name]--),
    completion.map(name => completion[name] = (completion[name] | 0) + 1))

console.log(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))



var idReg = /[a-zA-z]/g;
console.log(idReg.test("LeesinHo"))
console.log(idReg.test("123"))