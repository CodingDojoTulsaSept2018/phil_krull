import { Component, OnInit } from '@angular/core';
import { Planet } from '../planet';
import { HttpService } from '../http.service';

@Component({
  selector: 'app-planet-add',
  templateUrl: './planet-add.component.html',
  styleUrls: ['./planet-add.component.css']
})
export class PlanetAddComponent implements OnInit {
  planet: Planet = new Planet();

  constructor(private _service: HttpService) { }

  ngOnInit() {
  }

  addPlanet() {
    console.log(this.planet);
    this._service.addPlanet(this.planet).subscribe(response => {
      console.log(response);
      this._service.addPlanetToService(response.addedPlanet);
      this.planet = new Planet();
    });
  }

}
