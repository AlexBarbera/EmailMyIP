# EmailMyIP
Script that emails your ip when it detects a change.  
To run simply run `sudo ./run.sh`

## Setup
Change the _config.json_ file to your send from and to address (recommended gmail with [allow less secure apps](https://myaccount.google.com/lesssecureapps) ).  
This tool uses the _request_ package (so install it with your favourite package manager).  
Also this creates a smtp server on your local machine every iteration, in the future we will create a daemon that handles this.

## TO DO
- [x] Add requirements.txt
- [ ] Add support for other auth methods.
