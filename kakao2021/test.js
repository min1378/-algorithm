// function solution(info, query) {
//   var answer = []
//   const infoMap = {}

//   for (const infomation of info) {
//     const check = infomation.split(" ")
//     let key = ""
//     if (check[0] === "cpp") key += "0"
//     else if (check[0] === "java") key += "1"
//     else if (check[0] === "python") key += "2"

//     check[1] === "backend" ? (key += "0") : (key += "1")
//     check[2] === "junior" ? (key += "0") : (key += "1")
//     check[3] === "chicken" ? (key += "0") : (key += "1")
//     if (infoMap[key]) infoMap[key].push(check[4])
//     else infoMap[key] = [check[4]]
//   }
//   console.log(infoMap)
//   for (const queryInfo of query) {
//     const checkList = queryInfo.split("and")
//     let queryList = []
//     for (const check of checkList) {
//       const newList = check.trim().split(" ")
//       queryList = queryList.concat(newList)
//     }
//     const score = queryList.pop()
//     console.log(queryList, score)
//     if (queryList[0] === '-')
//   }

//   return answer
// }

// solution(
//   [
//     "java backend junior pizza 150",
//     "python frontend senior chicken 210",
//     "python frontend senior chicken 150",
//     "cpp backend senior pizza 260",
//     "java backend junior chicken 80",
//     "python backend senior chicken 50",
//   ],
//   [
//     "java and backend and junior and pizza 100",
//     "python and frontend and senior and chicken 200",
//     "cpp and - and senior and pizza 250",
//     "- and backend and senior and - 150",
//     "- and - and - and chicken 100",
//     "- and - and - and - 150",
//   ]
// )

const list = [1, 2, 3]
const score = 0
console.log(list.map((el) => el > score).length)
