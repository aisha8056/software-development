//console.log("found");

persons = [
    {id: 12, name: 'Cathy Mill', role: 'manager', gender: 'female', age: 26},
    {id: 45, name: 'Mohamed Johnson', role: 'client', gender: 'male', age: 11},
    {id: 3, name: 'Rose Ogene', role: 'designer', gender: 'female', age: 21},
  ]
  
  
  
  function showPerson(person){
    //console.dir(person);
    let personWindow = document.getElementById("get-person");
  }
  
  getPersonButton = document.getElementById("get-person");
  
  function getPersonbuttonClicked(event){
    console.log("clicked");
    showPerson(persons[0]);
  }