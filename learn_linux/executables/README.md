# Executables

## Introduction to executables and work with them

Linux executables are saved as `executable_file.sh`, and are executed as:

```bash
./executable_file.sh
```

### Shebang

"shebang" - special line on top of executable file telling what to use to execute the file.

Format of shebang:

```bash
#! interpreter [optional-arg]

# shebang for python
#!/usr/bin/python3
```

### Bourne Shell

- `sh`: The Bourne Shell, original UNIX one, not so many comfortable daily tools.
- `bash`: The Bourne Again Shell, most used among Linux users builds on `sh` and has more tools.
- `zsh`: The Z Shell, shell on MacOS, like `bash`.

### Export

Saving local variables for current shell session.

```bash
export NAME="name"

echo $NAME # shows name
```

These variables also can be used by the shell scripts.

```bash
#!/bin/sh
echo "Hi I'm $NAME"

# some_script.sh
```

Later call will be like so:

```bash
./some_script.sh
# Hi I'm name
```

Also those variables can be set for one command:

```bash
MESSAGE="this works!" bash some_script.sh
```

### Unset

removes an environment variable:

```bash
unset NAME
```

## PATH

`PATH` holds all of the executable run commands for comfort.

```bash
# show all PATH variables
echo $PATH

# add new path to existing PATH
export PATH="$PATH:/some/new/directory"
```
