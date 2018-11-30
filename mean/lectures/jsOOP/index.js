
function Foo() {
    const privateMethod = function() {
          console.log('line regular function', this);
    }

    const privateMethodII = ()=>{
        console.log('line 7 arrow function', this);
    }
    // class 
    this.greet = function() {
            console.log('Hello!');
            privateMethod();
    }

    this.greetII = ()=> {
        console.log('HelloII!');
        privateMethodII();
    }

}
const joe = new Foo();
joe.greet();
joe.greetII();

