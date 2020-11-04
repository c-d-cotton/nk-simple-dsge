# Introduction
Studies the standard 3-equation simple New Keynesian model. Includes analysis of how this model is affected by a fixed interest rate.

# Installation
<!---INSTALLATION_STANDARD_START.-->
I found standard methods for managing submodules to be a little complicated so I use my own method for managing my submodules. I use the mysubmodules project to quickly install these. To install the project, it's therefore sensible to download the mysubmodules project and then use a script in the mysubmodules project to install the submodules for this project.

If you are in the directory where you wish to download nk-simple-dsge i.e. if you wish to install the project at /home/files/nk-simple-dsge/ and you are at /home/files/, and you have not already cloned the directory to /home/files/nk-simple-dsge/, you can run the following commands to download the directory:

```
git clone https://github.com/c-d-cotton/mysubmodules.git getmysubmodules
python3 getmysubmodules/singlegitmodule.py nk-simple-dsge --downloadmodule --deletegetsubmodules
```

The option --downloadmodule downloads the actual module before installing the submodules. The option --deletegetsubmodules deletes the getsubmodules project after the submodules are installed.

If you have already downloaded projectdir to the folder /home/files/nk-simple-dsge/, you can add the submodules by running the following commands from the directory /home/files/:
```
git clone https://github.com/c-d-cotton/mysubmodules.git getmysubmodules
python3 getmysubmodules/singlegitmodule.py nk-simple-dsge --deletegetsubmodules
```
<!---INSTALLATION_STANDARD_END.-->


