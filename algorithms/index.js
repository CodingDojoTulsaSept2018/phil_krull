function Slnode(val) {
    if(!(this instanceof Slnode)){
      return new Slnode(val);
    }
    this.value = val;
    this.next = null;
}
function Slist() {
    if(!(this instanceof Slist)) {
      return new Slist();
    }
    this.head = null;
}

Slist.prototype.add = function(val) {
    var newNode = Slnode(val);
    if (!this.head) {
        this.head = newNode;
    } else {
        var current = this.head;
        while(current.next) {
            current = current.next;
        }
        current.next = newNode;
    }
}

function breakLoopII(list) {
    if(!list instanceof Slist || !list.head) return list;
    let runner = list.head;
    let isLoop = false;
    // check if list is 1 node long or if list is 1 node long and is a loop
    // fix loop and return
    if(runner.next == runner || runner.next == null) {
      runner.next = null;
      return true;
    }
    let runner2 = runner.next.next;
    // get runner and runner2 in loop
    while(runner2 && runner2.next && isLoop == false) {
      if(runner == runner2) {
        isLoop = true;
      } else {
        runner = runner.next;
        runner2 = runner2.next.next
      }
    }
    let runner3 = list.head;
    console.log(`isLoop is: ${isLoop}`);
    while(isLoop) {
      // print statement shows iterations to 
      console.log(`runner value is: ${runner.value} and runner2 value is: ${runner2.value}`);
      runner2 = runner.next;
      // set runner3 to head and move to 1 before runner
      while(runner3.next != runner && isLoop) {
        if(runner3.next == runner2) {
          runner.next = null;
          isLoop = false;
        }
        runner3 = runner3.next;
      }
      console.log(`runner3 value: ${runner3.value}`);
      while(runner2.next != runner && isLoop) {
        runner2 = runner2.next;
        if(runner2.next == runner) {
          // reset runner2 to be 1 ahead of runner, move runner back 1 closer to head, and reset runner3 to head
          runner = runner2;
          runner2 = runner2.next;
          runner3 = list.head;
          break;
        }
      }
    }
    return isLoop;
}

function hasLoop(list) {
    if(!list.head) return list;
    var runner = list.head.next;
    var walker = list.head;
    while(runner && runner.next){
      if(runner === walker) {
        return true;
      }
      runner = runner.next.next;
      walker = walker.next;
    }
    return false;
}

function setupLoop(list, nodeposition) {
    // creates loop to the nodeposition or the head if list < nodeposition
    if(!list.head) return list;
    var runner = list.head;
    var startLoop = list.head;
    while(runner.next){
      nodeposition--;
      if(nodeposition===0){
        console.log(`The start of the loops value will be ${runner.value}`);
        startLoop = runner;
      }
      runner = runner.next;
    }
    console.log(`The end node.next is ${runner.next}`);
    if(nodeposition === 1) {
        runner.next = runner;
    } else {
      runner.next = startLoop;
    }
    console.log(`After creating the loop, the end node.next.value is ${runner.next.value}`);
}

Slist.prototype.printArr = function() {
    if(!this.length()){return false;}
    var listArray = [];
    var runner = this.head;
    while(runner) {
      listArray.push(runner.value);
      runner = runner.next;
    }
    return listArray;
}

Slist.prototype.length = function() {
    var length = 0;
    var current = this.head;
    while(current) {
      length++;
      current = current.next;
    }
    return length;
}

var myList = Slist();
console.log('+'.repeat(100));
for(var idx = 0; idx < 90; idx++){
    var val = Math.floor(Math.random()*(100 - 1 + 1)) + 1;
    myList.add(val);
}

console.log(`myList before loop is: ${myList.printArr()}`);
// check the length both before and after the list has a loop and is fixed to make sure no nodes where lost
console.log(`length of list before breakLoop: ${myList.length()}`);
console.log(`Does the list hava a loop before Breakloop?: ${ breakLoopII(myList) }`);
// create loop at a random position in the list
setupLoop(myList, Math.floor(Math.random()*90) + 1);
// console.log(`Does the list have a loop before breakLoop?: ${hasLoop(myList)}`);
console.log('+'.repeat(25) + ' start of break loop ' + '+'.repeat(25));
console.log(`Does the list have a loop after breakLoop?: ${ breakLoopII(myList) }`);
console.log('+'.repeat(25) + ' end of break loop ' + '+'.repeat(25));
// console.log(`Does the list have a loop after breakLoop?: ${hasLoop(myList)}`);
// check the length both before and after the list has a loop and is fixed to make sure no nodes where lost
console.log(`length of list after breakLoop: ${myList.length()}`);