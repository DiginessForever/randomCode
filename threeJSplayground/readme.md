Three.js personal notes:

Keyboard control:
-----------------------------
THREEx.KeyboardState.js usage:

var keyboard = new THREEx.KeyboardState();  //start listening to the keyboard

//Can also use "keyboard.pressed('shift+A')" in the if statement below for modifiers like shift, ctrl, alt, etc 
//see source of THREEx.KeyboardState.js for more info
if (keyboard.pressed('A')){  				
  //do something
}

//later, kill the keyboard listener:
keyboard.destroy()

---------------------------
