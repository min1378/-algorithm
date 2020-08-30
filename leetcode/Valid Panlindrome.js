/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    s = s.toLowerCase().replace(/[\W_]/g, "")
    // 정규표현식에서  
    // \W => 단어가 아닌문자
    // [\W_] => 단어가 아닌 문자 or _ 밑줄
    // /[\W_]/g => 단어가 아닌 문자 or 밑줄을 전역에서 찾는다. 
    let left = 0
    let right = s.length - 1
    while(left < right){
      if (s[left] !== s[right]) return false
      else left++; right--;
    }
    return true
};
// 시간복잡도 (N)
// 공간복잡도 (1) left와 right를 사용해 있는 공간에서 움직였기 때문.
isPalindrome("A man, a plan, a canal: Panama")