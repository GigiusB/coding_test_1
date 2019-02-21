# Introduction

The following exercise has been completed without considering advanced Riak search techniques.

Possible improvements could be achieved by using the Apache SOLR - Riak integration.
More info is available at following links:
- https://docs.basho.com/riak/kv/2.0.8/developing/usage/search/
- http://basho.com/products/riak-kv/complex-query-support/

# Common query caching

The key for the cache entry will be generated using the same word extraction algorithm
in use for the search utility.
The resulting query words will be concatenated to the operator using ",".

For example a query using `Care Quality Commission` and `OR` will be resulting in the following
key:

```
OR,commission,quality,care
```


Here follow the *curl* examples to load the cache

```bash

curl -X POST \
  -H "Content-Type: text/plain"  \
  -d "0,1,2,3,4,5,6" \
   http://localhost:8098/buckets/hscicNewsCache/keys/OR,commission,quality,care

curl -X POST \
  -H "Content-Type: text/plain"  \
  -d "9" \
  http://localhost:8098/buckets/hscicNewsCache/keys/OR,2004,september

curl -X POST \
  -H "Content-Type: text/plain"  \
  -d "6,8" \
  http://localhost:8098/buckets/hscicNewsCache/keys/OR,population,generally,general

curl -X POST \
  -H "Content-Type: text/plain"  \
  -d "1" \
  http://localhost:8098/buckets/hscicNewsCache/keys/AND,commission,quality,admission,care

curl -X POST \
  -H "Content-Type: text/plain"  \
  -d "6" \
  http://localhost:8098/buckets/hscicNewsCache/keys/AND,population,alzheimer,general
```

The following is an example of hwo to retrieve the indexes:
```bash
curl http://localhost:8098/buckets/hscicNewsCache/keys/OR,population,generally,general
```
The result is a list of document keys separated by commas (eg. "*6,8*")

The content can then be retrieved using the key:
```bash
curl localhost:8098/buckets/hscicNews/keys/6
```


# Monthly indexes

In order to optimise document retrieval by year and eventually month we are using two secondary indexes:
- `year_month_bin` : for year and month in form YYYYMM
- `year_bin` : for year only in format YYYY

## Commands for loading the documents:
```bash
curl -X POST \
  -H 'x-riak-index-year_month_bin:201306' \
  -H 'x-riak-index-year_bin:2013' \
  -H "Content-Type: text/plain"  \
  -d "June 5 , 2013 : The majority of carers say they are extremely , ..." \
  http://localhost:8098/buckets/hscicNews/keys/0

curl -X POST \
  -H 'x-riak-index-year_month_bin:201307' \
  -H 'x-riak-index-year_bin:2013' \
  -H "Content-Type: text/plain"  \
  -d "July 9 , 2013 : The HSCIC has extended the consultation period on ..." \
  http://localhost:8098/buckets/hscicNews/keys/1

curl -X POST \
  -H 'x-riak-index-year_month_bin:201306' \
  -H 'x-riak-index-year_bin:2013' \
  -H "Content-Type: text/plain"  \
  -d "June 19 , 2013 : New figures from the Health and Social Care ..." \
  http://localhost:8098/buckets/hscicNews/keys/2

curl -X POST \
  -H 'x-riak-index-year_month_bin:201306' \
  -H 'x-riak-index-year_bin:2013' \
  -H "Content-Type: text/plain"  \
  -d "June 13 , 2013 : Almost one in five women who gave birth in the ... " \
  http://localhost:8098/buckets/hscicNews/keys/3

curl -X POST \
  -H 'x-riak-index-year_month_bin:201306' \
  -H 'x-riak-index-year_bin:2013' \
  -H "Content-Type: text/plain"  \
  -d "June 5 , 2013 : The majority of carers say they are extremely , very ..." \
  http://localhost:8098/buckets/hscicNews/keys/4

curl -X POST \
  -H 'x-riak-index-year_month_bin:201304' \
  -H 'x-riak-index-year_bin:2013' \
  -H "Content-Type: text/plain"  \
  -d "April 15 , 2013 Thousands of GP practices around the country that ..." \
  http://localhost:8098/buckets/hscicNews/keys/5

curl -X POST \
  -H 'x-riak-index-year_month_bin:201302' \
  -H 'x-riak-index-year_bin:2013' \
  -H "Content-Type: text/plain"  \
  -d "February 19 , 2013 : Mortality among mental health service users ... " \
  http://localhost:8098/buckets/hscicNews/keys/6

curl -X POST \
  -H 'x-riak-index-year_month_bin:201301' \
  -H 'x-riak-index-year_bin:2013' \
  -H "Content-Type: text/plain"  \
  -d "January 23 , 2013 : English A and E departments see the most ..." \
  http://localhost:8098/buckets/hscicNews/keys/7

curl -X POST \
  -H 'x-riak-index-year_month_bin:201212' \
  -H 'x-riak-index-year_bin:2012' \
  -H "Content-Type: text/plain"  \
  -d "December 12 , 2012 : The proportion of final year primary school ..." \
  http://localhost:8098/buckets/hscicNews/keys/8

curl -X POST \
  -H 'x-riak-index-year_month_bin:201209' \
  -H 'x-riak-index-year_bin:2012' \
  -H "Content-Type: text/plain"  \
  -d "September 26 , 2012 : Income before tax for UK contract holding GPs ..." \
  http://localhost:8098/buckets/hscicNews/keys/9
```

## Some example of data retrieval

Using a year and month index:

```bash
curl localhost:8098/buckets/hscicNews/index/year_month_bin/201306
```

Using a year only index:

```bash
curl localhost:8098/buckets/hscicNews/index/year_bin/2012
```

Retrieving the document using the key:

```bash
curl localhost:8098/buckets/hscicNews/keys/9
```

# Considerations

In order to test the deliverables a local instance of Riak has been set up using a
[docker image](https://hub.docker.com/r/lapax/riak) supporting LevelDB as backend
in order to use secondary indexes.


## Limitations of the solution
 
A suggested limit of 512 nodes in a ring exists for using the secondary indexes.
See [When Not to Use Secondary Indexes](http://docs.basho.com/riak/1.2.0/tutorials/querying/Secondary-Indexes/#When-Not-to-Use-Secondary-Indexes)

Search strategies links consulted for the exercise:
"[Comparing MapReduce, RiakSearch, and Secondary Indexes](http://docs.basho.com/riak/1.2.0/tutorials/querying/)"
and particularly
"[When to Use Search](http://docs.basho.com/riak/1.2.0/tutorials/querying/Riak-Search/#When-to-Use-Search)"

 