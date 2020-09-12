function solution(info, query) {
  const answer = []
  const infoMap = {
    java: {
      backend: {
        junior: {
          pizza: [],
          chicken: [],
        },
        senior: {
          pizza: [],
          chicken: [],
        },
      },
      frontend: {
        junior: {
          pizza: [],
          chicken: [],
        },
        senior: {
          pizza: [],
          chicken: [],
        },
      },
    },
    cpp: {
      backend: {
        junior: {
          pizza: [],
          chicken: [],
        },
        senior: {
          pizza: [],
          chicken: [],
        },
      },
      frontend: {
        junior: {
          pizza: [],
          chicken: [],
        },
        senior: {
          pizza: [],
          chicken: [],
        },
      },
    },
    python: {
      backend: {
        junior: {
          pizza: [],
          chicken: [],
        },
        senior: {
          pizza: [],
          chicken: [],
        },
      },
      frontend: {
        junior: {
          pizza: [],
          chicken: [],
        },
        senior: {
          pizza: [],
          chicken: [],
        },
      },
    },
  }
  for (const infomation of info) {
    const check = infomation.split(" ")
    infoMap[check[0]][check[1]][check[2]][check[3]].push(check[4])
  }
  const allList = [
    ["java", "cpp", "python"],
    ["backend", "frontend"],
    ["junior", "senior"],
    ["pizza", "chicken"],
  ]
  for (const queryInfo of query) {
    const checkList = queryInfo.split("and")
    let queryList = []
    for (const check of checkList) {
      const newList = check.trim().split(" ")
      queryList = queryList.concat(newList)
    }
    const score = queryList.pop()
    let result = 0
    const check = (newQueryList) => {
      if (newQueryList.indexOf("-") === -1) {
        const filter = infoMap[newQueryList[0]][newQueryList[1]][newQueryList[2]][newQueryList[3]].filter((el) => Number(el) >= score)
        result += filter.length
        return
      }
      if (newQueryList.indexOf("-") === 0) {
        const string = ["java", "cpp", "python"]
        for (let i = 0; i < 3; i++) {
          newQueryList[0] = string[i]
          check(newQueryList)
          newQueryList[0] = "-"
        }
      }
      if (newQueryList.indexOf("-") === 1) {
        const string = ["backend", "frontend"]
        for (let i = 0; i < 2; i++) {
          newQueryList[1] = string[i]
          check(newQueryList)
          newQueryList[1] = "-"
        }
      }
      if (newQueryList.indexOf("-") === 2) {
        const string = ["junior", "senior"]
        for (let i = 0; i < 2; i++) {
          newQueryList[2] = string[i]
          check(newQueryList)
          newQueryList[2] = "-"
        }
      }
      if (newQueryList.indexOf("-") === 3) {
        const string = ["chicken", "pizza"]
        for (let i = 0; i < 2; i++) {
          newQueryList[3] = string[i]
          check(newQueryList)
          newQueryList[3] = "-"
        }
      }
    }
    check(queryList)
    answer.push(result)
  }
  return answer
}

solution(
  [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50",
  ],
  ["- and - and - and - 150"]
)
