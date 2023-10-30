import { Router } from '@angular/router';
import { AccountService } from './../shared/account.service';
import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  login = {
    email: '',
    password: '',
  };

  modal = false;

  constructor(
    private accountService: AccountService,
    private router: Router
  ) { }

  ngOnInit() {
  }

  async onSubmit() {
      try {
        const result = await this.accountService.login(this.login);
        console.log(`Login efetuado: ${result}`);
        console.log(result);
        this.router.navigate(['/logado']);
      } catch (error:any) {
        const tipoError = await error.error;
        alert(tipoError);
      }
  }
}
