import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PlanetShowComponent } from './planet-show.component';

describe('PlanetShowComponent', () => {
  let component: PlanetShowComponent;
  let fixture: ComponentFixture<PlanetShowComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PlanetShowComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PlanetShowComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
