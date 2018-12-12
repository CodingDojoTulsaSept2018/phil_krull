import { Component, OnInit } from '@angular/core';
import { HttpService } from './../http.service';
import { Planet } from '../planet';

@Component({
  selector: 'app-planet-show',
  templateUrl: './planet-show.component.html',
  styleUrls: ['./planet-show.component.css']
})
export class PlanetShowComponent implements OnInit {
  allPlanets: Array<Planet>;
  planet: Planet;

  constructor(private _service: HttpService) { }

  ngOnInit():void {
    this._service.getPlanetsFromService().subscribe(response => {
        this._service.setPlanets(response['allPlanets']);
        console.log('get planets', this._service.getPlanets())
        this.allPlanets = this._service.getPlanets();
      });;
  }

  showOne(planet_id: String):void {
    // get one planet
    this._service.getOnePlanet(planet_id).subscribe(response =>{
      console.log(response);
      this.planet = response['onePlanet'];
    })
    // set the planet to the child component using Inputs
  }

}
