const solution = (data, word) => {
  const idMap = {};
  for (const line of data) {
    const [id, name, parentId] = line.split(" ");
    idMap[id] = name;
  }
  console.log(idMap);
};
solution(["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"], "BROWN");
// ["CONY/DOLL/BROWN-CONY", "BROWN/DOLL/LARGE-BROWN", "BROWN/DOLL/SMALL-BROWN"]
solution(["1 ROOTA 0", "2 AA 1", "3 ZZZ 1", "4 AABAA 1", "5 AAAAA 1", "6 AAAA 1", "7 BAAAAAAA 1", "8 BBAA 1", "9 CAA 1", "10 ROOTB 0", "11 AA 10"], "AA");
// ["ROOTA/AA", "ROOTB/AA", "ROOTA/BAAAAAAA", "ROOTA/AAAAA", "ROOTA/AAAA", "ROOTA/AABAA", "ROOTA/CAA", "ROOTA/BBAA"]
