# Random Password Generator

Made this quick script because I kept using the same passwords for everything (bad habit I know). Figured I should probably start using random ones but didn't want to pay for a password manager app.

## What it does

Generates a random password with whatever length you want. Mixes up lowercase letters, uppercase, numbers, and symbols all together. Super basic but gets the job done.

## Running it

Just Python needed, nothing else:
```bash
python password_generator.py
```

It'll ask you how long you want the password. Type a number and hit enter. That's literally it.

## Example

```
Enter the length of password: 12
K8#mP2@xL9vQ
```

Every time you run it you get something different obviously since it's random.

## How I wrote it

Pretty straightforward approach:
- Grab all the lowercase letters (a-z)
- Grab uppercase too (A-Z)
- Add in digits (0-9)
- Throw in punctuation symbols (!@#$%^&* etc)
- Combine everything into one big pool
- Use random.sample to pick characters without repeating
- Join them together into a string

The `random.sample` thing is nice because it doesn't pick the same character twice, so you get better variety.

## Things to note

- Minimum length is technically 1 but that'd be a terrible password lol
- Maximum is 94 characters since that's how many total characters are available (26 lowercase + 26 uppercase + 10 digits + 32 symbols)
- If you try to go over 94 it'll crash because sample() can't pick more items than exist
- No validation on the input so if you type letters or negative numbers it'll break

## Why it's useful

Good for:
- Generating throwaway passwords for random sites
- Creating strong passwords when you need them quick
- Learning how Python's random and string modules work

Not so good for:
- Passwords you need to remember (use a password manager for that)
- Situations where you need specific requirements like "must have 2 numbers" or whatever

## Possible improvements

If I wanted to make this fancier I could:
- Add error handling for bad inputs
- Let you specify how many of each character type (like exactly 2 symbols)
- Option to exclude confusing characters like 0/O or 1/l/I
- Save generated passwords to a file
- Copy to clipboard automatically
- Make it a GUI instead of command line

But honestly for my use case the simple version works fine. Sometimes simpler is better.

## Security stuff

The passwords are random but Python's `random` module isn't cryptographically secure. For most purposes it's totally fine, but if you're like a spy or something you might want to use `secrets` module instead of `random`.

Like you could change:
```python
temp = random.sample(gen,length)
```
to:
```python
import secrets
temp = [secrets.choice(gen) for _ in range(length)]
```

But again, for normal people uses the regular random is perfectly adequate.

## My take

This was one of those scripts I threw together in like 5 minutes because I needed it right then. Could it be better? Sure. Does it work? Yep. That's good enough for me.

Feel free to use it however you want. Modify it, improve it, whatever. No need to credit me or anything.
