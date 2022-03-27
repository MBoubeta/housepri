<!-- PROJECT SHIELDS -->
<!--
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
![housesbanner](images/housesbanner.png)

<p align="center">
  <h3 align="center">house-prices</h3>

  <p align="center">
    Houses prices prediction
    <br />
    <a href="https://github.com/MBoubeta/housepri"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/MBoubeta/housepri">View Demo</a>
    ·
    <a href="https://github.com/MBoubeta/housepri">Report Bug</a>
    ·
    <a href="https://github.com/MBoubeta/housepri">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
       <ul>
        <li><a href="#project-structure">Project structure</a></li>
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
<!-- TABLE OF CONTENTS
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
-->
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

Ask a home buyer to describe their dream house, and they probably won't begin with the height of the basement ceiling or the proximity to an east-west railroad.
But this playground competition's dataset proves that much more influences price negotiations than the number of bedrooms or a white-picket fence.

With 79 explanatory variables describing (almost) every aspect of residential homes in Ames, Iowa, this competition challenges you to predict the final price of each home.

### Project structure

    ├── docs
    │
    ├── housepri
    │   │
    |   ├── config
    │   │   |
    │   |   ├── config.yml
    |   |   |
    │   |   └── set_config.py
    │   │
    │   ├── data
    │   │   │
    │   │   ├── test.csv
    │   │   |
    │   │   └── train.csv  
    │   │
    │   ├── models 
    │   │
    │   ├── pipeline
    │   │   |
    │   |   └── set_pipeline.py
    │   │
    │   ├── process
    │   │   |
    │   |   ├── data_manager.py
    │   │   |
    │   |   ├── features.py
    │   │   |
    │   |   └── validation.py
    │   │
    │   ├── predict.py
    │   │
    │   ├── train.py
    │   │
    │   └── VERSION
    │
    ├── requirements         
    │
    ├── tests
    │
    ├── README.md
    │
    └── setup.py


## Getting Started

Some instructions are given to configure and execute your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This section contains the prerequisites you need to use the software and how to install them.
* Download the Kaggle data.

    Logging to Kaggle and go [here](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data).

    Download the train.csv and test.csv and put them in the house_prices/data directory.
* Install tox package.
  ```sh
  pip install tox
  ```

### Installation

Clone the repo
   ```sh
   git clone https://github.com/MBoubeta/house-prices.git
   ```

   
<!-- USAGE EXAMPLES -->
## Usage

Run this tox command to create a virtual environment in Python, install the necessary packages (from the requirements file) and run the LASSO model training.
   ```sh
   tox -e train
   ```
   
<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/MBoubeta/housepri.svg?style=for-the-badge
[contributors-url]: https://github.com/MBoubeta/housepri/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/MBoubeta/housepri.svg?style=for-the-badge
[forks-url]: https://github.com/MBoubeta/housepri/network/members
[stars-shield]: https://img.shields.io/github/stars/MBoubeta/housepri.svg?style=for-the-badge
[stars-url]: https://github.com/MBoubeta/housepri/stargazers
[issues-shield]: https://img.shields.io/github/issues/MBoubeta/housepri.svg?style=for-the-badge
[issues-url]: https://github.com/MBoubeta/housepri/issues
[license-shield]: https://img.shields.io/github/license/MBoubeta/housepri.svg?style=for-the-badge
[license-url]: https://github.com/MBoubeta/housepri/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/miguel-boubeta-martinez/