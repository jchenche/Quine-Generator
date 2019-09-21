# Quine-Generator

Quines (self-replicating programs) have the source code encoded as part of the source code, so it doesn't need to read any file to get the source code. The latter is impossible if the quine is compiled and the source code file is deleted.

After being fed to `quine_generator.py`, the target program becomes a quine. Now every time you run it, it does whatever it used to do, then prints itself.

If fed to `quine_generator2.py`, instead of printing, the target program will create a new file identical to itself. The maximum number of copies is 11, but this limitation could be removed.
