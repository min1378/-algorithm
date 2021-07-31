function solution(m, musicinfos) {
  let answer = null;
  for (const musicInfo of musicinfos) {
    const [startTime, endTime, name, melody] = musicInfo.split(",");
    const playedMin = playedTimeToMin(startTime, endTime);
    const convertedMelody = melodyConvert(melody);
    const playedMelody = findPlayedMelody(playedMin, convertedMelody);
    const result = compareMelody(melodyConvert(m), playedMelody);
    if (result) {
      answer = answer ? compareMusic(answer, { playedMin, name }) : { playedMin, name };
    }
  }
  if (!answer) return "(None)";
  return answer.name;
}

function playedTimeToMin(startTime, endTime) {
  const [startHour, startMin] = startTime.split(":");
  const [endHour, endMin] = endTime.split(":");
  return endHour * 60 + Number(endMin) - (startHour * 60 + Number(startMin));
}

function melodyConvert(melody) {
  let newMelody = melody;
  while (newMelody.indexOf("#") > -1) {
    const index = newMelody.indexOf("#");
    const changeChar = newMelody[index - 1];
    newMelody = newMelody.replace(changeChar + "#", changeChar.toLowerCase());
  }
  return newMelody;
}

function findPlayedMelody(min, melody) {
  if (min <= melody.length) {
    return melody.slice(0, min);
  } else {
    const repeatCount = parseInt(min / melody.length);
    const rest = min % melody.length;
    return melody.repeat(repeatCount) + melody.slice(0, rest);
  }
}
function compareMelody(melody, playedMelody) {
  if (playedMelody.indexOf(melody) > -1) {
    return true;
  } else return false;
}
function compareMusic(oldMusic, newMusic) {
  if (oldMusic.playedMin < newMusic.playedMin) {
    return newMusic;
  } else return oldMusic;
}
console.log(solution("CCB", ["12:00,12:14,HELLO,CCB#CCBCCB#", "13:00,13:14,WORLD,ABCDEF"]));
