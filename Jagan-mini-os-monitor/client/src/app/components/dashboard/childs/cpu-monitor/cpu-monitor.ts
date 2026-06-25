import { Component, Input } from '@angular/core';
import { CpuData } from '../../../../models/monitor.interface';
@Component({
  selector: 'app-cpu-monitor',
  imports: [],
  templateUrl: './cpu-monitor.html',
  styleUrl: './cpu-monitor.css',
})
export class CpuMonitor {
  @Input() data!:CpuData;
}
