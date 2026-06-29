```yaml
name: IPTV Checker

on:
schedule:
- cron: '0 0 * * *'
workflow_dispatch:

jobs:
build:
runs-on: ubuntu-latest
steps:
- name: Checkout code
uses: actions/checkout@v3

- name: Set up Python
uses: actions/setup-python@v4
with:
python-version: '3.9'

- name: Install dependencies
run: pip install requests

- name: Run script
run: python check_links.py

- name: Commit changes
run: |
git config --global user.name 'GitHub Action'
git config --global user.email 'action@github.com'
git add .
git commit -m "Update links" || echo "No changes to commit"
git push
```
