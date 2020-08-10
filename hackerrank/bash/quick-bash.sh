####################################################################
################## VARIABLES #####################################
#########################################################

# $ dereferences
# Variables in double quotes are interpreted, single quotes not
# Exported variables are passed to programs run within the shell
# Env shows exported variables, compgen -v shows all variables

MYNAME=Sushil
echo $MYNAME

MYSEN="A sentence"
echo $MYSEN

MYSEN1="A sentence with $MYSTRING in it"
echo $MYSEN1

echo $PPID   # Parent Process ID
echo $$      # Base Process ID

readonly READOONLYVAR=sushil  # can't change value

unset MYNAME  # to delete the variable

export MYSTRING=anotherstring  # available to all the bash (base, subshell)

env               # to see the list of all export variables
declare           # to see all list of variables
declare -f        # just function
delcare -F        # just function headers
declare -r        # just readonlys
declare -v
declare -a        # just array

echo $BASH_VERSINFO
echo ${BASH_VERSINFO[0]}
echo ${BASH_VERSINFO}_and_some_string
echo ${BASH_VERSINFO[1]}
echo ${BASH_VERSINFO[2]}
echo ${BASH_VERSINFO[3]}
echo ${BASH_VERSINFO[4]} 
echo ${BASH_VERSINFO[5]}
echo ${BASH_VERSINFO[6]}

A=1
echo $A             # 1
echo ${A[0]}        # 1, In bash everything is an array
echo ${A[1]}        # blank, since at position A[1] value is not provided

#############################################################################
####################### GLOBBING ###########################################
############################################################################

# File globbing is a feature provided by the UNIX/Linux shell to represent multiple filenames by using
# special characters called wildcard with a single file name.

# Wildcards: Special characters to help you rapidly specify group of filenames.
# Using wildcards allow you to select filenames based on patterns of characters

#  |----------------------------|------------------------------------------------------------------|
#  |      Wildcard              |                 Matches                                          |
#  |----------------------------|------------------------------------------------------------------|
#  |         *                  |             Any characters                                       |
#  |         ?                  |             Any single characters                                |
#  |      [characters]          |             Any char i.e., member of the set char                |
#  |      [!characters]         |             Any char i.e., not a member of the set char          |
#  |      [[:class:]]           |             Any char i.e., member of the specified class         |
#  |----------------------------|------------------------------------------------------------------|

# ** Wildcards can be used with any command that accepts filename as arguments.

# Commonly used characters classes
#            [:alnum:]        ---->        Any alphanumeric char
#            [:alpha:]        ---->        Any alphabetic char
#            [:digit:]        ---->        Any numeral
#            [:lower:]        ---->        Any lowercase letter
#            [:upper:]        ---->        Any uppercase letter

#  |------------------------------------------------------------------------------------------------------------------------|
#  |                                   WILDCARD EXAMPLES                                                                    |
#  |------------------------------------------------------------------------------------------------------------------------|
#  |           Pattern                     |                                      Matches                                   |
#  |---------------------------------------|--------------------------------------------------------------------------------|
#  |           *                           |  All Files                                                                     |
#  |           g*                          |  Any file beginning with g                                                     |
#  |           b*.txt                      |  Any file beginning with b followed by any characters & ending with .txt       |
#  |           Data???                     |  Any file beginning with Data followed by exactly three characters             |
#  |           [abc]*                      |  Any file beginning with either a. b, or c                                     |
#  |           [[:upper:]]*                |  Any file beginning with an uppercase letter                                   |
#  |           [![:digit:]]*               |  Any file not beginning with a numeral                                         |
#  |           *[[:lower:]123]             |  Any file ending with a lowercase letter or the numerals 1,2,0r 3              |
#  |           BACKUP.[0-9][0-9][0-9]      |  Any file beginning with BACKUP, followed by exactly three numerals.           |
#  |---------------------------------------|--------------------------------------------------------------------------------|

# REDIRECTION
#  I/O redirection allows us to redefine where standard output goes.
#  To redirect standard output(stdout) to another file instead of the screen, 
#  we use the > redirection operator followed by the name of the file.

# We could tell the shell to send the output of the ls command to the file ls-output.txt instead of the screen
ls -l /usr/bin > ls-output.txt

# grep -- Print Lines Matching a Pattern
# grep is a powerful program used to find text patterns within files, like this:
#                       grep pattern [file....]
# when grep encounters a "pattern" in the file, it prints out the lines containing it

# COMMANDS

mkdir itb_globe                            # make directory named itb_globe
cd itb_globe                               # move to itb_globe directory
touch file1 file2 file3                    # make three empty files
ls *                                       # list all files
echo *                                     # shows all files
echo ls *                                  # shows ls and all files
echo ls '*'                                # shows ls and * (single quote)
echo '$HOME'                               # shows $HOME
echo "$HOME"                               # shows your home directory path
ls "*"
ls *1                                      # list all files that ends with 1
ls file[12]                                # list all files that ends with 1, 2
ls file[a-z]                               # list all files that neds with a-z
ls file[a-z][0-9]                          # list all files that ends with [a-z][0-9]
echo file?                                 # shows all files that ends with any single characters
touch .adotfile
mkdir .adotfolder
touch .adotfolder/file1 .adotfolder/.adotfile
ls
ls *
echo .*                                    # shows all dot files
cd .                                       # remain in the same directory
echo text > afile                          # redirect text to afile
grep text afile                            # matching a pattern text in file afile and prints tot he console
grep '*' afile
grep '.*' afile


######################################################################################################
############################# PIPES & REDIRECTS ######################################################
######################################################################################################

# PIPELINES:
#   The ability of command to read data from standard input and send to standard output is utilized by a shell feature called pipelines.
#   Using the pipeline operator | (vertical bar), the stdout of one command can be piped into stdinput of another.
#                  command1 | command2

# Pipe is used to combine two or more command and in this the output of one command act as input to another command 
# and this command ouput may act as a input to next command as so on.

#                                                    |--------------   ls -l > temp
#   ls -l | less       can also be written as :  ----|
#                                                    |--------------   less < temp

# FILTERS
#  Pipelines are often used to perform complex operations on data.
#  It is possible to put several commands together into a pipeline.
#  Frequently, the command used this way are referred to as filters.
#    ls /bin /bin/usr | sort | less

# COMMANDS

mkdir itb_pipes_redirects
cd itb_pipes_redirects
echo "contents of file1" > file1
cat file1
cat file1 | grep -c file                          # print a count of matching lines for input files
cat file1 | grep 'contents of file1'
cat file1 | grep 'not in file'
cat file2
cat file2 | grep -c file
echo asd > /dev/stdout
ls -l /dev/stdout
cat file2 | grep -c file
command_does_not_exist
command_does_not_exist 2> /dev/null
grep -c file < file1                              # Using < redirection operator, we change the source of std input from the keyboard to the file1
echo line1 > file3
echo line2 > file3
echo line3 >> file3                               # >> used to append redirected output to a file instead of overwriting the file from the beginning
cat file3

#########################################################################################################
######################### COMMAND SUBSTITUTION ########################################################3
########################################################################################################

# Command Substitution:
#    It allows us to use the ouput of a command as an expansion

echo $(ls)
ls -l $(which cp)


# Quoting
#    Learn how we can control the shell expansion

echo this is a         test
echo The total is $100.0

# The shell provides a mechanism called quoting to selectively supress unwanted expansions.


## Double Quotes
#     If you place text inside double quotes all the special characters used by the shell lose their special meaning and are treated as ordinary characters.
#     The exceptions are $(dollar sign), \(backslash), and `(back tick).
#     This means that word splitting, pathname expansion, tilde expansion and brace expansion are supressed,
#     but parameter expansion, arithmetic expansion are still carried out.

echo this is a       test
echo $(cal)
echo "$(cal)"
echo "$(USER) $((2+2)) $(cal)"


## Single Quotes
#      If we need to supress all expansions, we use single quotes

echo text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER
echo "text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER"
echo 'text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER'


## Escaping Characters
#        Sometimes we want to quote only a single character. To do this, we can precede a character with a backslash,
#        which in this context is called escape character.

USER=sushil
echo "The balance for user $USER is: \$5.00"


# COMMAND

hostname                                    # show or set the system hostname
echo "My hostname is: $(hostname)"          # not supress $()
echo 'My hostname is: $(hostname)'          # supress $()
echo "My hostname is: `hostname`"           # not supress ``
echo 'My hostname is: `hostname`'           # supress ''
mkdir itb_cmdsub
cd itb_cmdsub
ls $(echo a $(echo b))
cd ..
ls `echo a `echo b``
ls `echo a \`echo b\``
echo `echo \` \\\`echo inside\\\`\``
echo $(echo $(echo $(echo inside)))




