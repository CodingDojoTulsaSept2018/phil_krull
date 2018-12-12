import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Planet } from './planet';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HttpService {
  allPlanets: Planet[];

  constructor(private _http: HttpClient) { }

  getPlanetsFromService() {
    return this._http.get('/planets');
  }
  addPlanet(planet: Planet) {
    return this._http.post('/planets', planet);
  }

  addPlanetToService(planet: Planet):void {
    this.allPlanets.push(planet);
  }

  setPlanets(allPlanets: Planet[]):void {
    this.allPlanets = allPlanets;
  }

  getPlanets():Array<Planet> {
    return this.allPlanets;
  }

  getOnePlanet(planet_id: String) {
    return this._http.get(`/planets/${planet_id}`);
  }
}
