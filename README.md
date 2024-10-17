# Computational Recruiting - HTB challenge

This Python script reads candidate data from a text file, calculates skill scores based on weighted attributes, and sends the top 14 candidates' results to a specified server.

## Features
- Reads candidate data from `data.txt`.
- Calculates skill scores using weighted attributes: Health, Agility, Charisma, Knowledge, Energy, and Resourcefulness.
- Sorts candidates by their overall value scores.
- Sends the top 14 candidates' names and scores to a server using a socket connection.

## Usage
1. Update the `ip` and `port` values with the target server's IP and port.
2. Ensure `data.txt` is in the same directory as the script, with each line containing candidate details.
3. Run the script:
   ```bash
   python script_name.py

## Requirements
1. `pandas`
2. `socks`

To Install all requirements
```bash
pip install -r requirements