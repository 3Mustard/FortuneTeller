
//takes a HTTP URL as a parameter ex(http://127.0.0.1:5002/DrawThree)
//and displays one or more cards to the webpage
function displayJSON(url) {

    //object that makes the request is a default package in javascript
    var xmlhttp = new XMLHttpRequest();

    //make request
    xmlhttp.onreadystatechange = function () {
        //if there are no errors convert the JSON to an object
        if (this.readyState == 4 && this.status == 200) {
            //convert JSON to object named response
            var response = JSON.parse(this.responseText);
            //if the URL was a draw one call the displayCard() function
            //else if the URL was a draw three call the displayCards() function
            if(url.includes("DrawOne")){
                displayCard(response,false);
            }else if(url.includes("DrawThree")){
                displayCards(response);
            }
            console.log(response);
        }
    };
    //sends request
    xmlhttp.open("GET", url, true);
    xmlhttp.send();

}

//function that is linked to button on html page, sends in the HTTP url to the displayJSON() function
function drawOne(){
    displayJSON("http://127.0.0.1:5002/DrawOne");
}
//function that is linked to button on html page, sends in the HTTP url to the displayJSON() function
function drawThree(){
    displayJSON("http://127.0.0.1:5002/DrawThree");
}
//takes a JSON array of cards in as a parameter and calls the displayCard() function for each card in the array
//clear display before sending the cards to displayCard()
//ex(calling DrawThree)
function displayCards(cards){
    var displayDiv = document.getElementById("display");
    displayDiv.innerHTML = "";
    for(var i = 0; i < cards.length; i++){
        displayCard(cards[i],true);
    }
}
//takes a JSON object of a card and a boolean(t/f) indicating whether there are multiple cards incoming
//if there is only one it does clear the display else it does not clear display
function displayCard(card,multiple){

  var displayDiv = document.getElementById("display");

  if(multiple == false) {
      displayDiv.innerHTML = "";
  }
  var cardImage = document.createElement("IMG");
  cardImage.src = card.image;

  var description = document.createElement("p");
  var descriptionNode = document.createTextNode("Description: "+card.description);
  description.appendChild(descriptionNode);

  var cardName = document.createElement("p");
  var cardNameNode = document.createTextNode("Name: "+ card.name);
  cardName.appendChild(cardNameNode);


  var suit = document.createElement("p");
  var suitNode = document.createTextNode("Suit: "+ card.suit);
  suit.appendChild(suitNode);

  var element = document.createElement("p");
  var elementNode = document.createTextNode("Element: "+ card.element);
  element.appendChild(elementNode);

  var attributes = document.createElement("p");

   min = Math.ceil(2);
   max = Math.floor(1);
   var upOrDown = Math.round(Math.random() * (max - min) + min);

  if(upOrDown == 1){
      attributes.appendChild(document.createTextNode("Attributes: "))
    for(var i = 0; i < card.face_up.length; i++){
        var value = card.face_up[i];
        if(i != 0){
            attributes.appendChild(document.createTextNode("," + value));
        }else {
            attributes.appendChild(document.createTextNode(value));
        }
    }
  }else if(upOrDown == 2){
      attributes.appendChild(document.createTextNode("Attributes: "))
       for(var i = 0; i < card.face_down.length; i++){
        var value = card.face_down[i];
        if(i != 0){
            attributes.appendChild(document.createTextNode("," + value));
        }else {
            attributes.appendChild(document.createTextNode(value));
        }
    }
  }

  displayDiv.appendChild(element);
  displayDiv.appendChild(attributes);
  displayDiv.appendChild(description);
  displayDiv.appendChild(cardImage);
  displayDiv.appendChild(cardName);
  displayDiv.appendChild(suit);
}

