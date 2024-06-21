# Hello, welcome to Web Homework 2

### The application uses *poetry* as package manager.

## Instruction to pull from DockerHub
1. In your terminal run `docker run -v ./<storage_folder>:/app/storage -it oleksyii/goit-web-hw2`
2. You should see the container pulled and executed
3. Enjoy!

## Instructions for local build:

1. Clone the repo by using `git clone`, or any other way, then doing `cd goit-web-01`
2. Create a docker image by running `docker build -t <your_tag_here> .`
3. Run the image by executing `docker run -v ./<storage_folder>:/app/storage -it <your_tag_here>`(on windows you have to specify the **ABSOLUTE** path to the storage folder on your host)
4. Enjoy the helper

> For example, the path on ***windows*** for me looks like: `C:\Users\Alex\Desktop\stuff\PythonStudy\web-01\storage`
> 
> The path on ***linux*** should be something like: `./storage`  




That's it. If you have any questions, feel free to reach out to me on [Slack](https://python24softw-r7k7319.slack.com/team/U077C5WB611)!