import { Component, Input } from '@angular/core';
import { MemoryData } from '../../../../models/monitor.interface';
@Component({
  selector: 'app-memory-monitor',
  imports: [],
  templateUrl: './memory-monitor.html',
  styleUrl: './memory-monitor.css',
})
export class MemoryMonitor {
@Input() data!:MemoryData;

}
