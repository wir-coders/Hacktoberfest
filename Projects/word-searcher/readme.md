# Cómo usar

To look for specific words in a given directory, program must be executed inside that directory.

For example, if you want to analyze the files inside a directory called `T02`, both files *keywords.json* and *alert.py* must be placed in that same directory.

To run the script, you must use the following command:

```
python alert.py directory_name
```

This will generate an output file called *_filenames.txt*, with the filenames where the script found the words.