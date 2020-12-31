#!/usr/bin/env bash

# the submodules we're downloading are (names separated by a space):
submodulenames="dsge-fixvar-shock dsge-perturbation"

# STANDARD_SUBMODULE_DOWNLOAD_START:{{{

# script to delete any current submodules and replace them with latest version of submodules from https://github.com/c-d-cotton/

# get current directory
pwdoriginal="$(pwd)"

# cd to this script's directory
cd "$(dirname "$0")"

# delete old submodules folder if 
# run script as ./setup_submodules.sh --deletesubmodules if I want to delete the current submodules/f older
if [ "$1" == "--deletesubmodules" ] && [ -d submodules/ ]; then
    rm -rf submodules/
fi

# make new submodules directory
mkdir -p submodules/

# move to the submodules directory
cd submodules/

# for each of the following submodule names
for submodulename in $submodulenames; do
    # git clone the submodule to the submodules folder
    if [ -d "$submodulename" ]; then
        cd $submodulename
        git pull
        cd ..
    else
        git clone https://github.com/c-d-cotton/"$submodulename"/
    fi

    # run setup.sh file in the submodule if that file exists
    if [ -f "$submodulename"/setup_submodules.sh ]; then
        ./"$submodulename"/setup_submodules.sh
    fi
done

# cd back to original working directory
cd "$pwdoriginal"

# STANDARD_SUBMODULE_DOWNLOAD_END}}}

