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

* File layout
  * One file per exercise.
  * Filename should follow the pattern
    ```
    {page number}-description_of_exercise.tex`
    ```
  * The first line of each file should be
    ```
    \leveldown{Description of Exercise - pg. XX}`
    ```
* Start each sentence on a new line.
* Indent environments with two spaces, e.g.
    ```
    \begin{equation}
      f(x) = x^2 \, .
    \end{equation}
    ```
* If a sentence ends with an equation, put `\, .` at the end of that equation (see above).
* Prefer `\left(` and `\right)` over e.g. `\big )`.
* Prefer to use the repo's macros, e.g. `\avgang{content}` instead of inlining `\left \lange content \right \rangle`.

Not all existing exercises in the repo follow this style guide (issue #23 is about fixing that).
