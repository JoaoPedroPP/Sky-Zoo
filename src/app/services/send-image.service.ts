import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class SendImageService {

  private url:string = '';
  
  constructor(private http:HttpClient) {
    if (!environment.production) {
      this.url = 'http://localhost:8080';
    }
  }

  analyzeImge(file: File) {
    const headers = new HttpHeaders();
    headers.append('Content-Type', 'image/png')
    const body = new FormData()
    body.append('image', file)
    console.log(body)
    return this.http.post(this.url + '/predict', body, {headers: headers}).toPromise();
  }
}
