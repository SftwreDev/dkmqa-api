# DKMetrics Back-end API
Back-end API using Python, Django and Django Rest Framework

## Requirements
Make sure you have the latest version of [Python](https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe)

After you install Python in your machine , clone this repository
```bash
git clone https://github.com/Data-Kaizen-Metrics/dkmqa_api.git
```

To create a virtual environment, open your terminal and run 
Install Virtualenv
```python
pip install virtualenv
```
then run the virtualenv
```python 
virtualenv venv
```

To activate the virtual environment, run (for Windows)
```bash
.\venv\Scripts\activate
```

Install the required dependencies by running 
```python
pip install -r requirements.txt
```
After the installation , run 

```python
python manage.py migrate
```

To run the web app
```python
python manage.py runserver
 ```
 
 # URLS 
 
 http://127.0.0.1:8000/api/login/  = (For Login)
 
 http://127.0.0.1:8000/api/register/   =  (For Registration)
 
 http://127.0.0.1:8000/api/logout/   = (For Logging out)
 
 # Format for testing the Login 

```json
{
"username" : "<your-username" ,
"password" : "<your-password>"
}
```

# For testing the API method POST, Put for Category
```json
{
"label" : "<your-category>"
}
```
