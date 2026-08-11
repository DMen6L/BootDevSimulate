# Basic shell commands

## Introduction to shell

- `expr` is a simple command evaluating small expressions.
- `whoami` basic command letting user know as who they logged in as.
- `name="Name"` assigning variable name a value of "Name" and is called using `$name`.
- `history` provides a list of latest called commands in the CLI.

```bash
# examples of calling/using the commands mentioned

expr 123456 + 7890

whoami

name="Name"
echo $name

history
```

## Filesystem navigation commands

- `pwd` shows current path to the directory user is at.
- `ls` listing of files and directories in the current directory.
- `cd` changing directory.
- `cat` reading contents of a file.
- `head` print first lines of a file.
- `tail` print last lines of a file.
- `less/more` interactive pagers allowing reading files by line or page.
- `touch` update timestamps of a file or create new empty files.
- `mkdir` create directory.
- `mv` rename/move a file.
- `rm` remove file or directory.
- `cp` copy files or directories.
- `grep` searching for patterns, within files or e.t.c.
- `find` searching by file name.
- `which` location of an installed command.

```bash
# examples of calling mentioned commands

pwd

ls
ls <dir> # lists files in the provided directory

cd <dir> # moves to the mentioned directory
cd .. # moves to the parent directory

cat <file> # read contents of the file
cat <file1> <file2> # concatenate the contents of both files and print them out

head -n 10 <file> # print first 10 lines of a file
tail -n 10 <file> # print last 10 lines of a file

# [enter] to read by line, b to go back a page, q to quit, /pattern to search by words
less <file>
more <file>

touch <file> # update/create a file
touch <file1> <file2> #update/create multiple files

mkdir <dir> # create a directory

mv <filename1> <filename2> # rename the file
mv <file> <new_path> # move the file to the new directory

rm <file> # remove file
rm -r <dir> # remove directory

cp <source_file> <destination_dir> # copy file into destination
cp -R <copy_dir> <new_dir> # copy all of contents of directory into new directory

grep "hello" <file> # searching for string hello in the file
grep "hello" <file1> <file2> # searching for string hello in multiple files
grep "hello" -r . # searching recursively in current directory and all subdirectories

find <dir> -name <file> # searching file by name in directory
find <dir> -name "*.txt" # find all txt files in directory
find <dir> -name "*chad*" # find all files with chad in their name

which <command> # location of the command executable
```
