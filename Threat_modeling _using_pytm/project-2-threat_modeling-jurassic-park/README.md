```bash
./main.py --dfd | dot -Tpng -o outputs/dfd.png
./main.py --seq | java -Djava.awt.headless=true -jar ../resources/plantuml.jar -tpng -pipe > outputs/seq.png
./main.py --report ../resources/my_templates/basic_template.md | pandoc -f markdown -t html > outputs/report.html
```
