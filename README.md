# Predicting Grades

[![Build Status](https://travis-ci.org/TreeveWhite/Predicting-Grades.svg?branch=master)](https://travis-ci.org/TreeveWhite/Predicting-Grades)
![APM](https://img.shields.io/apm/l/vim-mode.svg)

This is a project which uses Sklearn libraries to predict final A-level grades from your mock grades and attendence percentage. The project was created as a way to learn about the bascis of machine learning in python without a depth look at the complexities of the libraries and methods.
## Getting Started

### Prerequsits

The program is written in the Python 3 programming language.  You will need a working version of the python interpreter which is available at https://www.python.org/downloads/. In particular your python version must include the pip module which will be used to download the other necessary requirement (more information on this bellow).

The program relies upon the machine learning model KNeighborsClassifier, more infomation on this type of machine learning model can be found both online and at the sklearn website where the library is from.
### Set Up

To access the program you can either download it from Github (given you have access) or download it as a zip file from the eBart system. Both options are outlined bellow.

1) Download the repository from Github using:

```bash
$ git clone https://github.com/TreeveWhite/PREDICTING-GRADES
```

2) Download the zip file and then extract all the files to your local computer in a folder called PREDICTING-GRADES.

Once you have a copy of the package on your local computer, install the requirements:

```bash
$ cd PREDICTING-GRADES
$ py -m pip install -r reqirements.txt
```
## Running the Program

Ensure you have installed all the requirements discussed above before running the app using:

```bash
$ cd PREDICTING-GRADES
$ cd predicting-grades-pkg
$ py -m PredictGrades
```

## Testing
Program uses continus integration Testing through travis-ci.com yet can run the tests individually through files with "test_". These tests can all be run manually from within the tests folder.

## Description

### License
This project uses the MIT license, see the license file for furthr details.
