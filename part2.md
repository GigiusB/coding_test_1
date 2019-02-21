Search strategies:

"[Comparing MapReduce, RiakSearch, and Secondary Indexes](http://docs.basho.com/riak/1.2.0/tutorials/querying/)"
and particularly
"[When to Use Search](http://docs.basho.com/riak/1.2.0/tutorials/querying/Riak-Search/#When-to-Use-Search)"


# Common query caching


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


## Limitations of the solution
 
A limit of 512 nodes in a ring exists for using the secondary indexes.
See [When Not to Use Secondary Indexes](http://docs.basho.com/riak/1.2.0/tutorials/querying/Secondary-Indexes/#When-Not-to-Use-Secondary-Indexes)
 