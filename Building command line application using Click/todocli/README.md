<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">tody</h3>
  <p align="center">
    A todo list cli application designed using Python, Click and Rich
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)
This project will help you create a to-do list in command-line using the following commands:
```bash
> tody show                           # list all todos
> todo add -t "To Do 01" -c "Study"   # Add a todo under category "Study"
```

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://nextjs.org/)
* [Click](https://pypi.org/project/click/)
* [Rich](https://vuejs.org/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
### Prerequisites

List things you need to use the software and how to install them.
```sh
pip3 install click
pip3 install rich
sudo apt-get install sqlite3
```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/jahidul-arafat/Top-Python-Modules-for-DevOps.git
   ```
2. Install the module
   ```sh
   cd Top-Python-Modules-for-DevOps$ cd Building\ command\ line\ application\ using\ Click/todocli/
   pip3 install --editable .
   pip3 show tody
   ```

<!-- USAGE EXAMPLES -->
## Usage
```shell
tody show               # list all todos in the database
tody --help             
tody add --help
tody delete --help
tody update --help
tody complete --help

# add a task under a category or without a category
tody add -t "ToDo1" -c "Study"
tody add -t "ToDo2" -c "Youtube"
tody add -t "ToDo3" 

# Update the Category of ToDo3
tody update -i 3 -c Sports

# Mark a todo complete
tody complete -i 3

# Delete a todo
tody delete -i 3
```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] A simple database in sqlite3 which will store all the DB operations of storing/fetching/updating
- [x] List all todos in your task list
- [x] Add a new task under a certain category
- [x] Update a todo 
- [x] Mark a task completed
- [x] Delete a todo


See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Jahidul Arafat - jahidapon@gmail.com

Project Link: [https://github.com/jahidul-arafat/Top-Python-Modules-for-DevOps](https://github.com/jahidul-arafat/Top-Python-Modules-for-DevOps)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/jahidul-arafat/Top-Python-Modules-for-DevOps
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/jahidul-arafat/Top-Python-Modules-for-DevOps
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/jahidul-arafat/Top-Python-Modules-for-DevOps
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/jahidul-arafat/Top-Python-Modules-for-DevOps
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/jahidul-arafat/Top-Python-Modules-for-DevOps
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/jahidul-arafat-791a7490/
[product-screenshot]: images/screenshot.png
