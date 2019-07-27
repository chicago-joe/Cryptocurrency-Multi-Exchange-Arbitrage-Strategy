First, you need to install the CCXT library in Python using:
  python -m pip install --upgrade ccxt

Then, you need to edit the API_keys file with your public and secret API keys that are given to you by each exchange.
IMPORTANT: NEVER GIVE OUT YOUR API KEYS TO ANYONE!!! 

Anyone with access to your API_keys can place orders, withdraw funds, etc.
It is EXTREMELY important that only YOU have access to them! 

Finally, the strategy can be run entirely from the main.py file, like so: 
  python main.py
