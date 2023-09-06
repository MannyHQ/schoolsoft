export default class MaskMatricula {

    constructor () {

        this.inputs = '0123456789';
        this.content = [];
        this.limit = 9;

        this.element = document.getElementById('idStudent');

        this.element.onkeydown = (e) => this.pressKey(e);
    }

    pressKey(e) {
        e.preventDefault();

        const key = e.key;

        if ( key === 'Backspace')
            this.content.pop();
        else if ( this.inputs.includes(key) && this.content.length < this.limit )
            this.content.push(key);

        this.element.value = this.content.join('');
    }
}