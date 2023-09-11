"""You work on a payroll program.
Given a list of salaries,
you need to take the bonus everybody is getting as input and
increase all the salaries by that amount.
Output the resulting list."""

salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input())
bonu_salaries = list(map(lambda x : x+bonus,salaries))
print(bonu_salaries)

smaller_than_3500 = list(filter(lambda x : x<3500,salaries))
print(smaller_than_3500)