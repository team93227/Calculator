from os import system
digits, operator_info, unary_funcs = list(map(lambda num: str(num), range(10))), {"+": [lambda a, b: a + b, 0], "-": [lambda a, b: a - b, 0], "*": [lambda a, b: a * b, 1], "/": [lambda a, b: a / b, 1], "%": [lambda a, b: a % b, 1], "_": [lambda a, b: a // b, 1], "^": [lambda a, b: a ** b, 2]}, {"!": lambda num: 1 if num == 0 else num * unary_funcs["!"](num - 1), "|": lambda str: abs(float(str)), "n": lambda str: float(str) * -1}
while True:
  def evaluate(expression):
    in_brackets, numbers, operators = False, [""], []
    for char in expression:
      if in_brackets:
        if char == "(": bracket_level, sub_expression = bracket_level + 1, sub_expression + "("
        elif char == ")":
          if bracket_level == 0: in_brackets, numbers[-1] = False, evaluate(sub_expression)
          else: bracket_level, sub_expression = bracket_level - 1, sub_expression + ")"
        else: sub_expression += char
      else:
        if (char in digits) or (char == "." and numbers[-1] != "" and "." not in numbers[-1]): numbers[-1] += char
        elif char == "(": bracket_level, in_brackets, sub_expression = 0, True, ""
        elif char in operator_info and numbers[-1] != "": numbers.append(""), operators.append(operator_info[char])
        elif char in unary_funcs and numbers[-1] != "":
          if char == "!": numbers[-1] = abs(int(float(numbers[-1])))
          numbers[-1] = str(unary_funcs[char](numbers[-1]))
    if in_brackets: numbers[-1] = evaluate(sub_expression)
    if numbers[-1] == "": numbers.pop()
    while len(numbers) > 1:
      prev_prec = -1
      for i in range(len(operators)):
        if i < len(operators) and operators[i][1] > prev_prec and operators[i][1] >= (0 if i == len(operators) - 1 else operators[i + 1][1]):
          numbers[i] = str(operators[i][0](float(numbers[i]), float(numbers[i + 1])))
          numbers.pop(i + 1), operators.pop(i)
    return numbers[0]
  print("\nThe answer is", evaluate(input("Enter your expression:\n")) or "[invalid input]")
  if input("\nDo you want to use the calculator again?\n").lower() in ["n", "no"]: break
  system("clear")