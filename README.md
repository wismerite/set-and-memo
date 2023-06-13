# Set vs Memo

Small package to try out different solutions for a specific prompt.

## The Prompt

We need to parse a text file, containing one word per line, and return the longest word in the file that contains no repeated characters (“dog” would qualify, but “rabbit” wouldn’t).  The evaluation should be case insensitive.

## Usage

### Compare methods
Simplest is to run timing_script.py from the root dir:

```
python src/timing_script.py
```

To change the "memo" method and try out differen things, you can edit `_has_repeating_characters()` in `lib/find_longest_word.py`.

### Test module
Just run tox, after installing it:

```
tox
```
