import { Routes } from '@angular/router';
import {TaskListComponent} from './pages/task-list/task-list.component';
import {RegisterComponent} from './pages/register/register.component';
import {LoginComponent} from './pages/login/login.component';

export const routes: Routes = [ //routes for other pages
  { path: '', component: TaskListComponent }, //main page
  { path: 'register', component: RegisterComponent },
  { path: 'login', component: LoginComponent },
];
