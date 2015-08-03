# lcc-pdf-to-json

Converts the outlines of the Library of Congress Classification schedules from PDF into a JSON representation. 

The outlines found here: http://www.loc.gov/aba/publications/FreeLCC/freelcc.html

Each classmark has these properties:
```
    {
      "id": "ZA3201-3250",
      "parents": [
        "ZA3038-5190"
      ],
      "prefix": "ZA",
      "start": 3201.0,
      "stop": 3250.0,
      "subject": "Information superhighway"
    }
```
And are organized into objects based on prefix.

The goal of this dataset is to make it easy to place a LCC number into a coarse classfication catagory byeond what is available at http://id.loc.gov/authorities/classification.html

```
results.json         - The dataset
download_source.py   - Script to download the PDFs
extract_outlines.py  - Does the conversion, run with "python2.7 extract_outlines.py all"
problems.json        - Documents the dirty laundry, some classmarks needed to be changed to fit into this dataset's requirements or were excluded due to complexity
```
