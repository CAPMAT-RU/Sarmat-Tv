name: IPTV Checker

on:
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:

permissions:
  contents: write

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

      - name: Commit and push changes if any
        run: |
          git config --global user.name 'github-actions[bot]'
          git config --global user.email 'github-actions[bot]@users.noreply.github.com'
          git add .
          if [ -n "$(git status --porcelain)" ]; then
            git commit -m "Update links"
            git push
          else
            echo "No changes to commit"
          fi
