// import { Component } from '@angular/core';

// @Component({
//   selector: 'app-root',
//   templateUrl: './app.component.html',
//   styleUrls: ['./app.component.css']
// })
// export class AppComponent {
//   title = 'lucene-searcher-front-end';
// }

import { Component } from '@angular/core';
import { ElasticsearchService } from './elasticsearch.service';
 
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  queryData = [];
  constructor(private es: ElasticsearchService) {

  }

  search(value){
    // console.log(value)
    this.es.queryDocuments('tweets', 'tweets', value)
    .then(response => {
      if (response.hits != null) {
        this.queryData = response.hits.hits;
        console.log(this.queryData)
      }
    })

  }
}

