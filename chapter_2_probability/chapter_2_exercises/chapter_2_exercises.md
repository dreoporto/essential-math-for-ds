# Chapter 2 Exercises

1. There is a 30% chance of rain today, and a 40% chance your umbrella order will arrive on time. You are eager to walk in the rain today and cannot do so without either!
What is the probability it will rain AND your umbrella will arrive?
    - *Joint probability*
    - `P(A AND B) = P(A) * P(B)`
    - `0.30 * 0.40 = 0.12`

2. There is a 30% chance of rain today, and a 40% chance your umbrella order will arrive on time.
You will be able to run errands only if it does not rain or your umbrella arrives.
What is the probability it will **not** rain OR your umbrella arrives?
    - *Union probability - Nonmutually Exclusive*
    - `P(A OR B) = P(A) + P(B) - P(A) * P(B)`
    - `0.70 + 0.40 - 0.70 * 0.40 = 1.10 - 0.28 = 0.82`

3. There is a 30% chance of rain today, and a 40% chance your umbrella order will arrive on time.
However, you found out if it rains there is only a 20% chance your umbrella will arrive on time.
What is the probability it will rain AND your umbrella will arrive on time?
    - *Joint and Conditional Probability*
    - `P(umbrella, A) = 0.40`
    - `P(rain, B) = 0.30`
    - `P(A|B) = P(umbrella|rain) = 0.20`
    - `P(A AND B) = P(A|B) * P(B) = 0.20 * 0.30 = 0.06` 

4. You have 137 passengers booked on a flight from Las Vegas to Dallas. However, it is Las Vegas on a Sunday morning and you estimate each passenger is 40% likely to not show up.
You are trying to figure out how many seats to overbook so the plane does not fly empty.
How likely is it at least 50 passengers will not show up?
    - Binomial distribution
    - P(A) = P(no-show) = 0.4; 137 attempts
    - Calc using Probability Mass Function, with 0.6 YES-SHOW for 
    - 87 or LESS yes-show = 0.8221
5. You flipped a coin 10 times and got heads 8 times and tails 2 times.
Do you think this coin has any good probability of being fair? Why or why not?
    - NO: there is a only a 4% chance of getting 8
    - **aoporto**: this test is only run once; try running 10 separate tests of 10 tosses and then see the result