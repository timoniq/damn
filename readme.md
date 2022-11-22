# damn

**damn** (desperately agonizing math noobs) is a language to help you write knowledge assessment test generators.

Language will help you in variables constraints declaration and generate unique pairs of data. Then, the generated pair of variables can be evaluated with the formula (via wolframalpha integration).

Syntax:

```damn
1 > x > 10
y in [1, 2, 3]
(a, b) in [(4, 5), (1, 10)]
```

## Example

Constraints:

```damn
10 > a > 20
(v1, v2) in [(1, 2), (4, 8)]
```

Formula:

```damn
a = (v2 - v1)/t
```

Making a test:

```python
from damn import DefinitionSet, Calculator
import asyncio

calculator = Calculator(["DEMO"])

async def main():
    def_set = DefinitionSet.from_expressions([
        "10 > a > 20", 
        "(v1, v2) in [(1, 2), (4, 8)]"
    ])
    data = def_set.get_data()
    print(
        "What is delta t if " + 
        ", ".join(
            (f"{k} = {v.get_common_representation()}" for k, v in data.items())
        )
    )
    result = await calculator.calculate(data, "a = (v2 - v1)/t")
    answer = float(input("your answer > "))
    if answer == result.v:
        print("great!!")
        return
    print(f"BAD student. the right answer is {result.v}")

asyncio.run(main())
```