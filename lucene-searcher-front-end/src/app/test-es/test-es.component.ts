import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { ElasticsearchService } from '../elasticsearch.service';
 
@Component({
  selector: 'app-test-es',
  templateUrl: './test-es.component.html',
  styleUrls: ['./test-es.component.css']
})
export class TestEsComponent {
  isConnected = false;
  status: string;
 
  constructor(private es: ElasticsearchService, private cd: ChangeDetectorRef) {
    this.isConnected = false;
  }
 
}