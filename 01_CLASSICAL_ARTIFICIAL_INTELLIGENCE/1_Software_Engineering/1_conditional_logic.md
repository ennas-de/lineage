## The Conditional's Logic

- In Software Engineering construct, a conditional statement is a fundamental building block that allows a program to make decisions based on certain conditions. It enables the program to execute different code paths depending on whether a specified condition evaluates to true or false.

- This means that if as a software engineer, I want to create a system that behaves differently based on certain inputs or conditions (or states), I can use conditional statements to define these behaviors.

- A program that is designed to respond differently based on varying inputs can be seen as exhibiting a form of intelligence, as it can adapt its behavior according to the situation at hand.

- This is one of the basic principles and logic of software engineering.

- Depending on the programming language being used, conditional statements can take various forms, such as "if-else" statements, "switch" statements, or ternary operators.

- The core language or keywords used to implement conditional statements may vary, but the underlying concept remains consistent across different programming languages.

- For example, in Python, a simple conditional statement can be written as follows:

```python
if condition:
    # Code to execute if the condition is true
else:
    # Code to execute if the condition is false
```

- In this example, if the "condition" evaluates to true, the code block under the "if" statement will be executed; otherwise, the code block under the "else" statement will run.

- What this means in essense is that conditional statements are a way for software to perform different actions or tasks based on specific criteria or inputs, allowing for dynamic and adaptable behavior in software applications.

- Say, I want my program to tell me if we are in the daytime or nighttime based on the hour of the day. I can use a conditional statement to achieve this:

```python
hour = 14  # Example hour in 24-hour format

if hour < 12:
    print("It's daytime.")
else:
    print("It's nighttime.")
```

- The operator (<, >, ==, etc.) are used in the conditional statements to evaluate the state of the input (in this case, the hour of the day) to determine which code block to execute.

# Problems with Conditionals

- As you might have already noticed, excessive use of conditional statements can lead to complex and hard-to-maintain code, often referred to as "spaghetti code." This occurs when there are too many nested conditionals or when the logic becomes convoluted.

- Conditional staments, as powerful as they are, do not scale in production or real-world applications. If as new conditions arise, the code needs to be modified to accommodate those new conditions, which can lead to bugs and errors.

- We needed to find a way to mitigate this, or we needed to find a better way to represent intelligence in software engineering.

# Alternatives to Conditionals

- To address the limitations of conditional statements, software engineers often turn to alternative design patterns and techniques that promote cleaner and more maintainable code. Some of these alternatives include:

1. **Polymorphism**: In object-oriented programming, polymorphism allows objects of different classes to be treated as objects of a common superclass (i.e., they are created or they belong to a 'higher' entity). This enables the use of method overriding (or 'replacement of a parent function') to define different behaviors for different object (child) types without using conditionals.
2. **Strategy Pattern**: This design pattern involves defining a family of algorithms, encapsulating each one, and making them interchangeable. This allows the selection of an algorithm at runtime without using conditional statements.
3. **State Pattern**: This pattern allows an object to change its behavior when its internal state changes. It encapsulates state-specific behavior in separate classes, eliminating the need for conditionals to determine the current state.
4. **Lookup Tables**: Instead of using conditionals to determine actions based on input, a lookup table can map inputs to corresponding actions or values, allowing for direct access without conditional checks.
5. **Functional Programming Techniques**: Using higher-order functions, mapping, and filtering can help avoid conditionals by applying functions to data collections in a more declarative manner.

- By employing these alternatives, software engineers can create more modular, flexible, and maintainable code that better represents intelligence in software systems without relying heavily on conditional statements.

- But, these alternatives come with their own trade-offs and complexities. One of which is the fundamental issue of 'scaling'. That is, if we need to add new behaviors or states, we might need to create new classes or functions, which can lead to an increase in the number of components in the system.

- Also, in production systems (in the wild), we don't always know the exact data or states that the system will encounter. This uncertainty can make it challenging to design systems that can handle all possible scenarios without relying on conditionals.

## Quick Note

- Conditionals do not create intelligence; instead they encode decision rules that simulate intelligent behavior within narrow, predefined spaces.

- Also, conditionals fail not only because of code complexity, but because they require the designer to enumerate the state space in advance.

- Hence, we need something 'better', something more "ROBUST", something that can learn and adapt on its own without explicit programming for every possible condition. Or at least, that can handle more states of 'unkowns' than what we can explicitly program for.

# Feed Forward

This limitation of hand-coded conditionals is precisely what Artificial Intelligence (AI) set out to solve, and will lead us to the next part of this Section - 1.2 Genesis of AI.
