export default class MaskCVV {

    constructor() {

        this.inputs = `0123456789`;
        this.content = [];
        this.limit = 3;

        this.element = document.getElementById('cvv');

        this.element.onkeydown = (e) => this.pressKey(e);
    }

    pressKey(e){
        e.preventDefault();

        const key = e.key;

        if ( this.inputs.includes(key) ){

            if (this.content.length < this.limit )
                this.content.push(key);
        }
        else if ( key === 'Backspace' ){
            this.content.pop();
        }

        this.element.value = this.content.join('');
    }
}