## General Information
**OpenClassrooms Project4**
Swiss chess tournament software that allows to manage offline tournaments and produce reports.

## Guide and standardization
* PEP8
* flake8 max-line-length = 119

## Features

* Records information about a tournament
* Register the players of a tournament
* Manage rounds and matches
* Gives the results
* Restart an interrupted tournament
* Produce reports

### Prerequisites

The program being written in Python, it is essential that it is installed on your machine. You can download Python :
* [Download Python](https://www.python.org/downloads/)  

## Technologies

* tinydb](https://tinydb.readthedocs.io/en/latest/getting-started.html)
* [tkinter - tk] (https://docs.python.org/fr/3/library/tk.html)
* [re] https://docs.python.org/fr/3/library/re.html


### Installation

In order not to conflict with other existing projects, it is best to run the program under a virtual environment.
Here are the main commands for :

1. Create a virtual environment 

windows/mac/linux : ``python3 -m venv env```

2. Activate the virtual environment

windows: ``env\Scripts\activate.bat``
mac/linux : ```source env/bin/activate```

For more details on setting up a virtual environment, see the Python documentation
* [Python documentation](https://docs.python.org/fr/3.6/tutorial/venv.html/)  

It is also necessary to install the libraries that are essential to the proper functioning of the program. These are listed in the document ``requirement.txt`` and their installation is done via the following command executed in the virtual environment you just created:

``pip install -r requirements.txt``

## Startup

Once the console has been placed in the program folder, simply run the following command in the virtual environment:

``python3 main.py```

A menu will open offering the different options of the application. 

## flake8

To regenerate a flake8 report, launch "flake8" at the root of the project.

## Made with
VisualStudioCode](https://code.visualstudio.com/) - Text editor

## Authors

* **Marine BAP** _alias_ [@MarineBdlt](https://github.com/outout14)


## Acknowledgements

Thanks to **Ranga Gonnage** for his teaching and support.

Translated with www.DeepL.com/Translator (free version)