const solution = (table, languages, preference) => {
  const jobs = [];
  const scores = [];
  for (const line of table) {
    const [job, ...rest] = line.split(" ");
    jobs.push(job);
    scores.push([...rest].reverse());
  }
  const result = [];
  for (const score of scores) {
    let sum = 0;
    for (let i = 0; i < languages.length; i++) {
      if (score.indexOf(languages[i]) > -1) {
        sum += (score.indexOf(languages[i]) + 1) * preference[i];
      }
    }
    result.push(sum);
  }
  const maxValue = Math.max.apply(null, result);
  const answer = [];
  for (let i = 0; i < result.length; i++) {
    if (result[i] === maxValue) {
      answer.push(jobs[i]);
    }
  }
  return answer.sort()[0];
};
solution(
  ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
  ["PYTHON", "C++", "SQL"],
  [7, 5, 5]
);
