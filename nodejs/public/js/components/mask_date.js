export default class MaskDate {

    constructor() {

        this.input = document.getElementById('expiry');
        this.input.value = null;

        this.inputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Backspace'];
        this.mask = ['x', 'x', '/', 'x', 'x'];
        this.content = [];

        this.pressKey();
    }

    pressKey() {
        
        this.input.addEventListener("keydown", e => {

            e.preventDefault();

            const key = e.key;
            const length = this.input.value.length;
            const limit = this.mask.length;

            if ( this.inputs.includes(key) && key != 'Backspace' ) {

                if ( length < limit ) {

                    if ( this.mask[length] === '/' )
                        this.content.push('/');
                    
                    this.content.push(key);
                }
            }
            else
                this.content.pop();

            this.input.value = this.content.join('');
        });
    }
}