#elasticjack

## Features:

- Jack list of indexes available
- Enumerate document counts for each index
- Enumerate document count for specific index
- Jack *x* documents for specific index
- Jack **all** documents for specific index
- Jack **all** documents for **all** indexes

## What to Expect

ElasticSearch will give the output for operations in a JSON file. Python allows for nice manipulation of JSON, so certain info can be gleaned cleanly from documents. For example, if we want to grab the "date" field from a whack of documents, that can be easily accomplished by grabbing record['date'] in an iterative loop. For the big Jack commands (i.e. Jack all documents), the output will need to be pushed into a JSON file which can be manipulated further after the download has completed. This makes the process easier and cleaner than manipulating the data mid-stream. Further, it provides safety for the sanity of the document and means less rendundant dump calls to the Elasticsearch server in cases where you've supplied the wrong field to Jack. :)

