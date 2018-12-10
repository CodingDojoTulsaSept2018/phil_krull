import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { HttpService } from './http.service';
import { PlanetShowComponent } from './planet-show/planet-show.component';
import { PlanetAddComponent } from './planet-add/planet-add.component';
import { PlanetShowoneComponent } from './planet-showone/planet-showone.component';

@NgModule({
  declarations: [
    AppComponent,
    PlanetShowComponent,
    PlanetAddComponent,
    PlanetShowoneComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [HttpService],
  bootstrap: [AppComponent]
})
export class AppModule { }
