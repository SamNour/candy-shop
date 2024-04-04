<img src="https://github.com/SamNour/candy-shop/assets/96638051/8696071b-e671-45f5-b26d-b2c24c137692" alt="image" style="width:100%;">

## About
The candy store Inspired by the OWASP Juice store is arguably one of the most advanced insecure platforms available! It serves as an invaluable resource for security training training Capture The Flag (CTF) events, and as a testing ground for various security tools! 

## LFS
There is no need to setup the Backend/Frontend (the below steps), all the dependencies and the required files are LFSed. 
Do follow the below steps only if error occurs in the initial run.


## Setting up the Backend:

```bash
# Navigate to the backend directory
$ cd ./backend

# Activate the virtual environment
$ pipenv shell

# Install dependencies from requirements.txt
$ pipenv install -r requirements.txt
```

## Setting up the Frontend:

```bash
# Make sure Node.js is installed

# Navigate to the frontend directory
$ cd ./frontend/

# Install project dependencies
$ npm install

# Install linter to avoid Vue-related issues
$ npm install --save-dev eslint eslint-plugin-vue
# For cool visuals on login pages
$ npm install --save particles-bg-vue
# To validate input form
$ npm install vuelidate --save
# Change to the frontend directory
$ cd frontend

# Start the development server
$ npm run serve
```

# Install Bootstrap version 4.6.0

```bash
$ npm install bootstrap bootstrap-vue --save
$ npm i bootstrap-icons
```
