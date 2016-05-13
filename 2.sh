curl -XPUT "http://localhost:9200/movies1/movie/_mapping" -d'
 {
    "movie": {
       "properties": {
          "director": {
             "type": "multi_field",
             "fields": {
                 "director": {"type": "string"},
                 "original": {"type" : "string", "index" : "not_analyzed"}
             }
          }
       }
    }
 }'

