import { Component, inject, Input, Output, signal, Signal } from '@angular/core';
import { ProcessData } from '../../../../models/monitor.interface';
import { MonitorService } from '../../../../services/monitor';
import { EventEmitter } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-process-monitor',
  imports: [
    FormsModule,
  ],
  templateUrl: './process-monitor.html',
  styleUrl: './process-monitor.css',
})
export class ProcessMonitor {

  public monitorService = inject(MonitorService)
  searchQuery ='';

  @Input() data!:ProcessData[];
  @Output() killProcess = new EventEmitter<number>();
  @Output() search = new EventEmitter<string>();

  onSearch(){
    this.search.emit(this.searchQuery);
  }

  onKill(pid:number){
    this.killProcess.emit(pid);
  }



}
