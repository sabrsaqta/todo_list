import { Component } from '@angular/core';
import {FormsModule} from '@angular/forms';
import { HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [
    FormsModule
  ],
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})
export class RegisterComponent {
  username = '';
  email = '';
  password = '';

  constructor(private http: HttpClient) { }
  onSubmit(){
    const user = {
      username: this.username,
      email: this.email,
      password: this.password
    };

    this.http.post('http://localhost:8000/api/register', user).subscribe(
      {
        next: response => {
          console.log('User registered successfully', response);
        },
        error: error => {
          console.log('Register failed with error', error);
        }
      }
    );
  }

  // protected readonly onsubmit = onsubmit;
}
