## Prerequisites
- [x] Linux/MacOS 
- [x] Python 3.x 
- [x] Graphviz package 
- [x] Java (OpenJDK 10 or 11)
- [x] plantuml.jar


## My Environment Setup
```bash
> python --version                                    # Python 3.6.9
> sudo apt-get install graphviz pandoc
> git clone https://github.com/jahidul-arafat/pytm    # clone the pytm opensource repo
> cd pytm
> sudo pytho3 setup.py develop
> pip3 show pytm                                      # Show the pytm version

# Download the plantuml.jar file from here https://sourceforge.net/projects/plantuml/
> wget https://sourceforge.net/projects/plantuml/files/1.2022.1/plantuml.1.2022.1.jar
> mv plantuml.1.2022.1.jar plantuml.jar
> export PLANTUML_PATH = "~/Downloads/plantuml.jar"

> java --version                                # openjdk 11.0.13 2021-10-19
```

## Execute the below commands
```bash
> ./sample-tm.py --dfd | dot -Tpng -o outputs/dfd.png
> ./sample-tm.py --seq | java -Djava.awt.headless=true -jar ../resources/plantuml.jar -tpng -pipe > outputs/seq.png
> ./sample-tm.py --report ../resources/my_templates/basic_template.md | pandoc -f markdown -t html > outputs/report.html

# list all threats in the model # 103 threats
> ./simple-tm.py --list   
> ./simple-tm.py --list | wc -l 
```




