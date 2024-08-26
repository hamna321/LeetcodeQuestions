class Solution:
  def compress(self, chars: List[str]) -> int:
    ans = 0
    group_length = 0

    while group_length < len(chars):
      letter = chars[group_length]
      count = 0

      while group_length < len(chars) and chars[group_length] == letter:
        count += 1
        group_length += 1
      chars[ans] = letter
      ans += 1

      if count > 1:
        for c in str(count):
          chars[ans] = c
          ans += 1

    return ans