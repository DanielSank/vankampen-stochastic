### Goal

Do all the problems in N.G. Van Kampen's stochastic processes book (or at least the interesting ones).

### Contributing

To contribute, solve a problem from the book and file a pull request against this repo.
See existing problems and solutions for expected format (we use Tex).
To easily find outstanding problems, search the issues for the "open problem" tag.
Open problem issues contain a link to a stub giving the complete problem.
See [issue 1](https://github.com/DanielSank/vankampen-stochastic/issues/1) as an example.

### View the work

To view the work, run LaTeX on main.tex.

### Issue labels

* **bug:** An existing problem or solution contains an error.
* **help wanted:** You're working on a problem and you'd like to find someone else to work with you. It's best to provide a link to your branch with work on this problem.
* **new solution (use for pull requests):** You've solved and written up a problem and want to get it merged in.
* **open problem:** Points to an as-yet unsolved problem.
* **question:** You have a question about stochastic processes (e.g. a math or physics question), or how this repo works.

### Style guide

1. File layout
    1. One file per exercise.
    1. Filename should follow the pattern
        ```
        {page number}-description_of_exercise.tex
        ```
    1. The first line of each file should be
        ```
        \leveldown{Description of Exercise - pg. XX}
        ```

1. Start each sentence on a new line.

1. Indent environments with two spaces, e.g.
    ```
    \begin{equation}
      f(x) = x^2 \, .
    \end{equation}
    ```

1. If a sentence ends with an equation, put `\, .` at the end of that equation (see above). For multiline blocks of math, put the `\, .` on its own line:
    ```
    \begin{align*}
      f(x)
      &= \int_1^\infty \frac{1}{x^2} \, dx \\
      &= - \frac{1}{x} \bigg \lvert^{\infty}_1 \\
      &= 1
      \, .
    \end{align*}
    ```

1. Prefer `\left(` and `\right)` over e.g. `\big )`.

1. Use the `align` environment for multiline math.

1. Write inline fractions like this: `1/2`.

1. Do not use `\frac` inside a superscript. If you have a lot going on inside e.g. an exponential, use
    ```
    \exp \left( stuff \right)
    ```

1. Prefer to use the repo's macros, e.g. `\avgang{content}` instead of inlining `\left \lange content \right \rangle`.
