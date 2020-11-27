var messages = [], //array that hold the record of each string in chat
  lastUserMessage = "", //keeps track of the most recent input string from the user
  botMessage = "", //var keeps track of what the chatbot is going to say
  botName = 'Chatbot' //name of the chatbot

//edit this function to change what the chatbot says
function chatbotResponse() {
  botMessage = "I'm confused..."; //the default message

  if (lastUserMessage === 'hi') {
    botMessage = 'Howdy!';
  }

  if (lastUserMessage === 'name') {
    botMessage = 'My name is ' + botName;
  }
}

//
//this runs each time enter is pressed.
//It controls the overall input and output
function newEntry() {
  //if the message from the user isn't empty then run 
  if (document.getElementById("chatbox").value != "") {
    //pulls the value from the chatbox ands sets it to lastUserMessage
    lastUserMessage = document.getElementById("chatbox").value;
    //sets the chat box to be clear
    document.getElementById("chatbox").value = "";
    //adds the value of the chatbox to the message array
    messages.push(lastUserMessage);
    //takes the return value from chatbotResponse() and outputs it
    chatbotResponse()
      //add the chatbot's name and message to the array messages
    messages.push("<b>" + botName + ":</b> " + botMessage)
      // says the message using the text to speech function written below
    Speech(botMessage);
    //outputs the last few messages to html
    for (var i = 1; i < 8; i++) {
      if (messages[messages.length - i])
        document.getElementById("chatlog" + i).innerHTML = messages[messages.length - i];
    }
  }
}

//text to Speech
//https://developers.google.com/web/updates/2014/01/Web-apps-that-talk-Introduction-to-the-Speech-Synthesis-API
function Speech(say) {
  if ('speechSynthesis' in window) {
    var utterance = new SpeechSynthesisUtterance(say);
    //utterance.volume = 1; // 0 to 1
    //utterance.rate = 1; // 0.1 to 10
    //utterance.pitch = 1; //0 to 2
    //utterance.text = 'Hello World';
    //utterance.lang = 'en-US';
    speechSynthesis.speak(utterance);
  }
}

//runs the keypress() function when a key is pressed
document.onkeypress = keyPress;
//if the key pressed is 'enter' runs the function newEntry()
function keyPress(e) {
  var x = e || window.event;
  var key = (x.keyCode || x.which);
  if (key == 13 || key == 3) {
    //runs this function when enter is pressed
    newEntry();
  }
}