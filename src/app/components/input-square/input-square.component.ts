import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { SendImageService } from 'src/app/services/send-image.service';

@Component({
  selector: 'app-input-square',
  templateUrl: './input-square.component.html',
  styleUrls: ['./input-square.component.scss']
})
export class InputSquareComponent implements OnInit {

  sky: FormGroup;
  @Output('resp') result:EventEmitter<Object> = new EventEmitter();

  constructor(private fb: FormBuilder, private sendImg: SendImageService) {
    this.sky = this.fb.group({
      f: ['']
    })
  }

  ngOnInit() {
  }

  ResetForm() {
    this.result.emit({classe:{data: ''}});
    this.sky.reset()
  }

  loadFile(event) {
    if (event.target.files && event.target.files[0]) {
      const reader = new FileReader();
      reader.onload = () => {
        this.sky.get('f').setValue(event.target.files[0]);
      }
      reader.readAsDataURL(event.target.files[0]);
    }
  }

  onSubmit(event) {
    this.result.emit({classe:{data: ''}});
    this.sendImg.analyzeImge(this.sky.get('f').value)
      .then((data:any) => {
        console.log(data);
        this.result.emit({
          classe: data.class
        })
      })
      .catch((err) => {
        this.result.emit({
          classe: 'erro'
        })
      })
      .finally(() => this.sky.reset());
  }

}
