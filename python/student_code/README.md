# Instructions to students writing in Python

You will be constructing code that decides who to save in any scenario - the passengers in the car or the pedestrians in the crosswalk.

To see sample code in action, simply run `main.py`:
`python main.py`

Your task is to write a more sophisticated ethical engine.  To do so modify engine.py.  Each time you make a modification test your 
code by typing 'python main.py'

You can also run a primitive audit on your algorithm by running auditor.py
'python auditor.py'

After you have coded an algorithm that you are happy with, reflect on your experience.

    First, confer with a classmate (if you have been assigned one by the instructor) and compare your engines. Did you code your engines the same way or differently? What were your differences?

    Second, consider reading a little more about what philosophers and pundits have to say about designing ethics engines and the Trolley Problem exercise. Quite a few of them are listed on the trolley problem wikipedia page

    Third, write a two to three page paper where you reflect on your experiences. Tackle at least three of the following questions:

    "What principles of justice/fairness were you attempting to embody in your decision engine? How well did you succeed in embedding these principles into your engine? What (if any) compromises did you have to make? Compare your own engine to one of your classmates -- what were the merits and demerits of your engine compared to your classmates? What are some larger lessons about the relationship between justice/fairness and the development of algorithms that you learned from doing this assignment? What did you learn in the process of testing and fine-tuning your engine? What are the benefits and costs of attempting to express justice and fairness through this exercise? Is it possible to create algorithms that are neutral?"

VI. Turn In Your Work
Deliverables
Your decision algorithm: engine.js
Your two page reflection paper: reflection.doc or reflection.pdf


**List of files:**
- `scenario.py` contains code to randomly generate scenarios, including a `Scenario` and `Person` class. Students should not need to touch this.
- `main.py` contains code that repeatedly cycles through scenarios - printing them out for the user to see, and also making a decision based on the `decide` method constructed in `engine.py`.
- `engine.py` is where students will code the decision-making of their car. Currently, it is designed simply so it can be demoed - only save the passengers if there are more passengers than pedestrians.
- `auditor.py` the code that statistically samples the biases of an engine.py



