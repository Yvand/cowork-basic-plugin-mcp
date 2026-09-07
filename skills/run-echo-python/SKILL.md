---
name: run-echo-python
description: Runs the bundled Python echo script with user-provided text. Use only when the user asks to run the local echo Python script.
license: MIT
metadata:
  author: Yvand
  version: "1.0"
---

# Run Echo Python

Run `scripts/echo.py` with a Python 3 interpreter, passing the user's text as the positional argument:

```sh
python scripts/echo.py "text to echo"
```

Return the script's output to the user.