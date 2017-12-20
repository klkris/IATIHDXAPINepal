# IATIHDXAPINepal
## Introduction

Exploratory project to find ways how IATI and HDX data can support humanitarian workers in their decision making during disaster response.

### Prerequisites
Tested on:
* Ubuntu Server 16.04
* Python 3.6 and pip
* Postgres 9.5
* Virtualenv 15

### Installing
Clone this repository
```
git clone https://github.com/d-paulus/IATIHDXAPINepal.git
```

Create a virtual environment within the project directory
```
cd IATIHDXAPINepal/ && virtualenv -p python3.6 venv
```

Activate the virtual environment 
```
source venv/bin/activate
```

Install the python requirements 
```
venv/bin/pip3 install -r requirements.txt
```

Create a Postgres user (use 'iatihdxapi' as password)
```
sudo -u postgres createuser -P -d iatihdxapi
```

Create a Postgres database
```
sudo -u postgres createdb -O iatihdxapi iatihdxapi
```

Migrate the database
```
venv/bin/python3 manage.py migrate
```

Run the project
```
venv/bin/python3 manage.py runserver
```

To populate the database with example data, make rest calls to
```
localhost:8000/updateiati
localhost:8000/updatehxl
localhost:8000/updateshelter
```

## Example REST calls
### IATI
Get all IATI data
```
localhost:8000/iati
```

Search in IATI data 
```
localhost:8000/iati/?search=food
```

Get IATI data from specific reporting organization 
```
localhost:8000/iati/?reporting-org=Sweden
```

Get IATI data by title 
```
localhost:8000/iati/?title=UNCERF Multi-year Commitment
```

### HXL
Get all HXL data
```
localhost:8000/hxl
```

Get HXL data by district
```
localhost:8000/hxl/?district=Kathmandu
```

### Shelter data
Get all shelter data
```
localhost:8000/shelter
```

Get HXL data by district
```
localhost:8000/shelter/?district=Kathmandu
```

### Combined HXL and shelter data
Get shelter data and HXL data merged by district
```
localhost:8000/multitest
```

### Ordering
HXL and shelter data views can be ordered via ```?ordering```
#### Example 
Districts ordered by female fatalities
```
localhost:8000/hxl/?ordering=-femalesDead
```
