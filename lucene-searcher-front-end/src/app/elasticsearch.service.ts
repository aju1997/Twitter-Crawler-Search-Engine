import { Injectable } from '@angular/core';
import { Client } from 'elasticsearch-browser';
import * as elasticsearch from 'elasticsearch-browser';
 
@Injectable({
  providedIn: 'root'
})

export class ElasticsearchService {
 
  private client: Client;
 
  constructor() {
    if (!this.client) {
      this._connect();
    }
  }
 
  private connect() {
    this.client = new Client({
      host: 'http://localhost:9200',
      log: 'trace'
    });
  }
 
  private _connect() {
    this.client = new elasticsearch.Client({
      host: 'localhost:9200',
      log: 'trace'
    });
  }

  queryDocuments(_index, _type, _query): any {
    return this.client.search({
      index: _index,
      type: _type,
      size: 100,
      body: {
        "track_scores": true,
        "sort" : [
          {"_score" : { "order": "desc"}},
          { "timestamp_ms" : {"order" : "desc"}}
        ],
        "query": {
          "function_score": {
            "query": { "match_all": {} },
            "functions": [
                {
                    "filter": { "match": { "user.name": _query } },
                    "script_score" : {
                      "script" : "_score" 
                    },
                    "weight":2
                }, 
                {
                  "filter": { "match": { "entities.hashtags.text": _query } },
                  "script_score" : {
                    "script" : "_score"
                  },
                  "weight":3
                },
                {
                  "filter": { "match": { "url_title": _query } },
                  "script_score" : {
                    "script" : "_score"
                  },
                  "weight":3
                },
                {
                  "filter": { "match": { "text": _query } },
                  "script_score" : {
                    "script" : "_score"
                  },
                  "weight":2
                }
            ],
            "score_mode": "sum",
          }
      }
        
      }
    })
  }
}

