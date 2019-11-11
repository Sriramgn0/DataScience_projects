#!/bin/bash
# Ask the user for their name
echo Hello, who am I talking to?
read varname
echo It\'s nice to meet you $varname
#ask how they are
echo How are you feeling $varname
read varfeel
echo Well $varname i am glad you are feeling $varfeel
echo Here is a list of things to do $varname
PS3='Please enter your choice: '
options=("Tell a joke" "Show disk usage" "Show current dir" "exit")
select opt in "${options[@]}"
do
    case $opt in
        "Tell a joke")
            echo $varname, you are a joke! Stop wasting my time!
            ;;
        "Show disk usage")
            df
            ;;
        "Show current dir")
            pwd
            ;;
        "exit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
