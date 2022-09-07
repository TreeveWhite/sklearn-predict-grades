# Predicting Grades

[![Build Status](https://travis-ci.org/TreeveWhite/Predicting-Grades.svg?branch=master)](https://travis-ci.org/TreeveWhite/Predicting-Grades)
![APM](https://img.shields.io/apm/l/vim-mode.svg)

This is a project which uses sklearn libraries to predict final A-level grades from your mock grades and attendance percentage. The project was created as a way to learn about the basics of machine learning in python without a depth look at the complexities of the libraries and methods.
## Getting Started

### Prerequisite

The program is written in the Python 3 programming language.  You will need a working version of the python interpreter which is available at https://www.python.org/downloads/. In particular your python version must include the pip module which will be used to download the other necessary requirement (more information on this bellow).

The program relies upon the machine learning model KNeighborsClassifier, more information on this type of machine learning model can be found both online and at the sklearn website where the library is from.
### Set Up

To access the program you can either download it from Github (given you have access) using Git commands or download it as a zip file from the eBart system. Both options are outlined bellow.

1) Download the repository from GitHub using:

```bash
$ git clone https://github.com/TreeveWhite/sklearn-predict-grades
```

2) Download the zip file and then extract all the files to your local computer in a folder called sklearn-predict-grades.

Once you have a copy of the package on your local computer, install the requirements:

```bash
$ cd sklearn-predict-grades
$ py -m pip install -r requirements.txt
```

Run the test test-requirements using the following command to ensure that the correct modules have all been downloaded and are accessible under your current build environment.

```bash
$ cd sklearn-predict-grades
$ cd test
$ py test_requirements
```

## Running the Program

Ensure you have installed all the requirements discussed above before running the app using:

```bash
$ cd sklearn-predict-grades
$ cd predicting-grades-pkg
$ py -m PredictGrades
```

## Testing
Program uses continuous integration testing through travis-ci.com, yet can run the tests individually through files with "test_". These tests can all be run manually from within the tests folder.

## Description

This project was my first investigation into how AI is created using Python and the logic surrounding how the sklearn package operates. The project uses the sklearn module and more specifically the KNeighborsClassifier method of the module. This algorithm  works by finding the nearest neighbours to the data which is given and then classifying based on these neighbours. More details about this can be found in the sklearn documentation available on their website.

### License
This project uses the MIT license, see the license file for further details.
