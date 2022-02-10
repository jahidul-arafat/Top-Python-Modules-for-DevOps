## Directory Cleaner Command Line Application
by Jahidul Arafat

### Installation Guide
```bash
> git clone git@github.com:jahidul-arafat/Bot-Creation-and-WorkflowAutomation-using-Python-and-Node.js.git
> cd Bot-Creation-and-WorkflowAutomation-using-Python-and-Node.js/Project_1_Directory_Cleanup_Script
> pip3 install --editable .
```

### Setting the Dummy test directory
This will set a dummy directory with txt, jpg, png, pdf and hidden files for our simulation purposes
```bash
> cd Bot-Creation-and-WorkflowAutomation-using-Python-and-Node.js/Project_1_Directory_Cleanup_Script
> chmod +x test_directory_script.sh
> ./test_directory_script.sh
```


### Use cases for `clean` operation
```bash
> dirclearner
> dirclearner --help
> dirclearner clean --help
> dirclearner clean
> dirclearner clean --path ./test_directory
> dirclearner clean --path ~/Downloads
> dirclearner clean --path /Choose/Any/Path/You/Want/to/Clean
```

### Use cases for `rename` operation
```bash
> dircleaner rename --search file --replace rfile --filetype .txt --path ./test_directory
> dircleaner rename --search file --replace rfile --path ./test_directory
```

### Simulation
[![Watch the video](https://img.youtube.com/vi/T-D1KVIuvjA/maxresdefault.jpg)](https://youtu.be/NtPLmoohA70)

