### Basic Instruction 
#### Creation of SSH keys 
```
ssh-keygen -t ed25519 -C "your_email@example.com" 
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```
#### Adding SSH key to GitHub 
1. Settings 
2. SSH and GPG keys 
3. New SSH key 
4. `cat ~/.ssh/id_ed25519.pub` &rarr Key
5. Add SSH key
#### Cloning repo under SSH
1. 
  1. Clone  
  1. SSH 
1. ^C link 
1. `git clone "your_link"` 
