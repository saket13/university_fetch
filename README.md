# university_fetch(https://cryptic-lowlands-23524.herokuapp.com)

A Flask based web app to fetch the list of universities based on the given country name.


## API used 
http://universities.hipolabs.com/search?country= has been used for the same.


## Directory Structure
    
    university_fetch             
    .
    ├── Contains       
    |   ├── static               # Contain the static images, css, js
    │   ├── templates            # Templates include the html files of the Front end
    │   ├── fetch.py             # Main python file for the flask server
    |   ├── forms.py             # Forms for selecting country
    │   └── univ_list.py         # Python script for making request to the external API
    |   └── requirements.txt     # Requirements file
    |______________________   

## Instructions for Setup

Clone the repo and install Requirements :

```bash
git clone https://github.com/saket13/university_fetch
cd path_to_university_fetch
pip3 install -r requirements.txt (Install the requirements preferrably in Virtual environment)
```

## Settings
```python
After installing the requirements in the virtual environment, 
export FLASK_APP=fetch.py
```

## Usage

Run the server:

```python
flask run
```

To fetch the list of universities, select the country and the result will be shown:


## Live Hosting On heroku

https://cryptic-lowlands-23524.herokuapp.com

