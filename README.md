# Make outbank csv export to JSON _(german only  by now)_
 
 The [Outbank App][1] is a popular multi banking app which can collect all account movements over a 
 long period (even for my cash movements).
 
 All entry's are categorized using a static 2 layer category/subcategory method and 
 every entry can be tagged with unlimited free chosen text-tags.
 
 ## Usage
 ```Bash
 chmod +x outbank2json.py 
 ./outbank2json.py ~/Desktop/Outbank_Export_20190729.csv
 ls ~/Desktop
 # Outbank_Export_20190729.csv Outbank_Export_20190729.csv.json
 ```
 You can pass as **second argument the destination filename** for the json.
 
 Only python3 standard library are used. Nothing to install beside python3.
 
 # Motivation
 ## csv export - hard to analyse
 ![](images/CsvFromApp.gif)
 
 When exporting entry's using the csv export function, **tags are space separated combined in one column**.  
 For better analysis of your financial data, it's helpful to access every tag as a separate object.
 
 ## The resulting JSON
````JSON
{
    "Datum": "2019-07-29T00:00:00",
    "Betrag": -420.0,
    "... Other missing keys": "",
    "Kategorie": "Finanzen",
    "Unterkategorie": "Umbuchung",
    "Tags": [
      "#amazon_aws",
      "#IAAS"
    ],
    "Notiz": ""
  }
```` 
This example shows one outbank entry as json _(not every key is listed here)_. 

[1]: https://outbankapp.com
