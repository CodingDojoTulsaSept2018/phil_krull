import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PlanetShowoneComponent } from './planet-showone.component';

describe('PlanetShowoneComponent', () => {
  let component: PlanetShowoneComponent;
  let fixture: ComponentFixture<PlanetShowoneComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PlanetShowoneComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PlanetShowoneComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
