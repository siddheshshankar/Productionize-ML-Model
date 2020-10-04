## Decision Tree Classifier

### <u>Titanic Dataset</u>
| Variable  | Definition  | Key |
|---|---|---|
|  Survival | Survival  |  0=No<br>1=Yes |
| Pclass  |  Ticket class | 1=1st<br>2=2nd<br>3=3rd  |
|  Sex |  Sex | 1=Male<br>0=Female  |
| Age  |  Age in years |   |
|  Sibsp | Number of siblings/spouses aboard the Titanic  |   |
|  Parch |  Number of parents/children aboard the Titanic |   |
|  Ticket |  Ticket number |   |
| Fare | Passenger fare  |   |
| Cabin  | Cabin number  |   |
|  Enbarked | Port of Embarkation  | C=Cherbourg<br>Q=Queenstown<br>S=Southampton |

### <u>Variable Notes</u>
pclass: A proxy for socio-economic status (SES)<br>
&nbsp;&nbsp;&nbsp; 1st is Upper class<br>
&nbsp;&nbsp;&nbsp; 2nd is Middle class<br>
&nbsp;&nbsp;&nbsp; 3rd is Lower class

Age: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5

sibsp: The dataset defines family relations in this way:<br>
&nbsp;&nbsp;&nbsp;Sibling = brother, sister, stepbrother, stepsister<br>
&nbsp;&nbsp;&nbsp;Spouse = husband, wife (mistresses and fiancés were ignored)

parch: The dataset defines family relations in this way:<br>
&nbsp;&nbsp;&nbsp; Parent = mother, father<br>
&nbsp;&nbsp;&nbsp; Child = daughter, son, stepdaughter, stepson<br>
&nbsp;&nbsp;&nbsp; Some children travelled only with a nanny, parch=0 for them.
