function solution(skill, skill_trees) {
  const skillMap = {}
  const skillList = skill.split("")
  let skillIndex = 1
  for(const skill of skillList){
    skillMap[skill] = skillIndex
    skillIndex += 1 
  }
  let answer = 0
  for (const skillTree of skill_trees){
    let skillLevel = 1
    const skillTreeList = skillTree.split("")
    let flag = true
    for(const skill of skillTreeList){
      if(!skillMap[skill]) continue
      if(skillMap[skill] > skillLevel) {
        flag = false
        break
      }
      skillLevel += 1
    }
    if(flag) answer += 1
  }
  return answer;
}