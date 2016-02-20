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

#### Commands

Count:
pseudophed@zeus:~$ curl wa-elastic01:9200/_cat/count/ads_new?v
epoch      timestamp count 
1455938798 22:26:38  3   

Health:
pseudophed@zeus:~$ curl 'wa-elastic01:9200/_cat/health?v'
epoch      timestamp cluster      status node.total node.data shards pri relo init unassign pending_tasks 
1455938971 22:29:31  weepy-search yellow          1         1     10  10    0    0       10             0 

Indexes:
pseudophed@zeus:~$ curl 'wa-elastic01:9200/_cat/indices?v'
health status index   pri rep docs.count docs.deleted store.size pri.store.size 
yellow open   fail      5   1          0            0       720b           720b 
yellow open   ads_new   5   1          3            1     17.5kb         17.5kb 

Master Info:
pseudophed@zeus:~$ curl 'wa-elastic01:9200/_cat/master?v'
id                     host         ip        node         
vUHeO0c9SeeUvuKPEU3zyQ wa-elastic01 127.0.1.1 wa-elastic01 

Nodes:
pseudophed@zeus:~$ curl 'wa-elastic01:9200/_cat/nodes?v'
host         ip        heap.percent ram.percent load node.role master name         
wa-elastic01 127.0.1.1            3           9 0.00 d         *      wa-elastic01

Plugins:
pseudophed@zeus:~$ curl 'wa-elastic01:9200/_cat/plugins?v'
name component version type url 


Repositories: **Elasticsearch 2.x
% curl 'localhost:9200/_cat/repositories?v'
id    type
repo1   fs
repo2   s3

