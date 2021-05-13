# EmailMyIP
Script that emails your ip when it detects a change.  

To run simply:
1. Clone this repo
2. Create a folder inside called _personal_ and move _config.json_ inside. 
3. Edit _config.json_ with your data. Recommended gmail with [allow less secure apps](https://myaccount.google.com/lesssecureapps) ). 
4. run `sudo ./run.sh`

## Setup 
This tool uses the _request_ package (so install it with your favourite package manager).  
Also this creates a smtp server on your local machine every iteration, in the future we will create a daemon that handles this.

## TO DO
- [x] Add requirements.txt
- [ ] Add support for other auth methods.
