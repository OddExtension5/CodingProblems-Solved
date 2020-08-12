### 1. When should you not use a list comprehension?
#### Answer:
Two common cases where you shouldn't use a list comprehension are:
+ You don't actually want a list
+ The logic is too long

**Case 1**:

List comprehension build lists, but that's not the only reason we use for loops.

```python
[team.set_location(HOME) for team in league_teams if team in home_teams_today]
  
# for loop, it doesn't waste space creating a list that it just ignores
for team in league_teams:
    if team in home_teams_today:
        team.set_location(HOME)
```

**Case 2**:

```python

active_player_accounts = [player.get_account() for team in league_teams
    if len(team.roster) > 1 for player in team.get_players()
    if not player.is_injured()]
    
# without list comprehension
active_player_accounts = []

for team in league_teams:

    # teams need to have at least 2 players before they're considered "active"
    if len(team.roster) <= 1:
        continue

    for player in team.get_players():

        # only want active players
        if player.is_injured():
            continue

        account = player.get_account()
        active_player_accounts.append(account)
```
    

### 2. Slicing lists from the end
#### Answer:

```python
def show_balances(daily_balances):
    num_balances = len(daily_balances)

    # still avoid slice that just has yesterday
    for day in range(num_balances - 3, num_balances - 1):
        balance_slice = daily_balances[day : day + 2]

        # need to calculate how many days ago
        days_ago = num_balances - day
        print("slice starting %d days ago: %s" % (abs(days_ago), balance_slice))
```
Other solution

```python
def show_balances(daily_balances):
    for day in range(-3, len(daily_balances)):
        balance_slice = daily_balances[day : len(daily_balances)]
        
        if day == -1:
            break

        # use positive number for printing
        print("slice starting %d days ago: %s" % (abs(day), balance_slice))
```

### 3. Count Capital Letters
Write a one-liner that will count the number of capital letters in a file. Your code should work even if the file is too big to fit in memory.

```python
count = sum(character.isupper() for line in fh for character in line)
```

