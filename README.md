# Scrape IQ


email_finder.py searches for email ids inside domain names, by guessing various formats.

Remember to check for:
1. First or last names with more than one word, or initial. Add them as separate rows
2. Remove INC, LLP, LLC, etc. from company names
3. Remove ", a part of <> group" from company names
4. Remove Google and LinkedIn URLs from domain names