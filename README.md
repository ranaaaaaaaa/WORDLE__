# WORDLE__

## Code Logic

1. **Initialization**  
   - 4-word list: `["which", "their", "there", "about"]`  
   - Random selection: `random.choice(wordle_list)`

2. **Game Loop**  
   - 6 attempts max  
   - Input forced to lowercase  
   - Rejects non-5-letter guesses  

3. **Letter Checks**  
   ```python
   for i in range(len(attempt)):
       if attempt[i] == random_item[i]:  # GREEN
       elif attempt[i] in randomitem_list:  # ORANGE
       else:  # GRAY
