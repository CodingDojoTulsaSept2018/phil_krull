import { Component, OnInit, Input } from '@angular/core';
import { Planet } from '../planet';

@Component({
  selector: 'app-planet-showone',
  templateUrl: './planet-showone.component.html',
  styleUrls: ['./planet-showone.component.css']
})
export class PlanetShowoneComponent implements OnInit {
  @Input() showOnePlanet: Planet;

  constructor() { }

  ngOnInit() {
    console.log('in showone component', this.showOnePlanet);
  }

}
