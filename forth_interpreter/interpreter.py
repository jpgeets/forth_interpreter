class Interpreter:

    def  execute(self, code: str) -> list[int]:
        stack: list[int] = []
        for token in code.split():
            if token.isdigit():
                stack.append(token)
            elif token == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(a - b)
            else:
                raise ValueError(f"Unknown token: {token}")

        return stack
