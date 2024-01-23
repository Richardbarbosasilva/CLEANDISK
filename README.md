# CLEANDISK

Automation of the cleandisk utility with python, powershell and batch

While it is not possible to run cleanmgr.exe via CLI properly, i have created this automation that makes the mouse do it alone, while blocking it for the user while the script is being executed, so the user cannot mess up 
with the automation. With the batch script, i made it to be executed by the GPO on every PC startup, so it find and executes powershell script, that searchs for python interpreter
and finally find and run the .py script, in this sequence.

It can be used as a Group policy to make all PCs inside a domain be constantly cleaned.
