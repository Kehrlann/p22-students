# p22-students

Python Students, with classes (ha-ha)


***NOTES IMPORTANTES :***  

* notez pour commencer que dans ce TP nous **utilisons les *type hints***, que nous avons rencontré brièvement au cours 3; c'est-à-dire qu'on a fréquemment indiqué le type des paramètres des méthodes, en écrivant par exemple  
`add_grade(topic: str, grade: float)` au lieu de simplement  
`add_grade(topic, grade)`
* dans ce TP nous allons nous définir deux classes `Student` et `Class`. Comme vous l'avez vu en cours une classe est définie (entre autres) par une série d'attributs et de méthodes. Il faut voir les méthodes comme des fonctions écrites spécialement pour s'appliquer à une instance de la classe. Les méthodes sont des fonctions qui, vous avez l'habitude de voir maintenant, ont généralement `self` comme premier argument; cela permet une utilisation `instance.methode(autre, arguments)`  
  
Ainsi, lorsqu'il vous est demandé d'implémenter la méthode `add_grade(topic: str, grade: float)` à la classe `Student`, n'oubliez pas que cela se traduit dans votre cellule par quelque chose comme : 

```python
class Student:
    ...
    
    def add_grade(self, topic: str, grade: float):
        # Votre code ici
        pass

    ...
```
  
  Notez l'apparition du `self` comme premier argument ! Bon courage ! ;)


## La classe `Student`

Nous allons commencer par créer une classe `Student` qui va nous permettre d'instancier des étudiants. Le noyau de la classe est le suivant :

```python
from collections import defaultdict

class Student:
    def __init__(self, first_name: str, last_name: str):
        pass
        
    def __repr__(self):
        pass
```

Dans la suite du TP, vous allez devoir ajouter des fonctionnalités à la classe `Student`. Pour ce faire, vous devez revenir à **chaque fois** à cette cellule, implémenter votre code et **ré-évaluer** la cellule pour que les changements soient pris en compte.


### Constructeur et `__repr__`

Surchargez les deux méthodes `__init__` et `__repr__` dans la cellule ci-dessus. (Et n'oubliez pas de la ré-évaluer!)

```python
try:
    student = Student("Achille", "Talon")
    if repr(student) != "Achille Talon":
        raise Exception("There is an issue in your __repr__ method.")
except Exception as e:
    print('[Student.__init__ and Student.__repr__] Does not work')
    print(f"Error message : {e}")
else:
    print('[Student.__init__ and Student.__repr__] OK')
```

### Gestion des notes

#### `add_grade`

Nous souhaitons maintenant ajouter des notes à cet élève. Implémentez la méthode `add_grade(topic: str; grade: float)` dans la classe `Student` pour que le code suivant s'exécute sans erreur :  

**Note :** Pour stocker les notes de l'élève vous allez devoir ajouter un attribut à la classe `Student`. Prenez le temps de réfléchir au conteneur le plus approprié.

```python
try:
    student = Student("Achille", "Talon")
    student.add_grade("History", 10.)
    student.add_grade("History", 12.)
except Exception as e:
    print('[Student.add_grade] Does not work')
    print(f"Error message : {e}")
else:
    print('[Student.add_grade] OK')
```

#### `followed_topics`

Maintenant, nous aimerions savoir quelles matières suit un élève *via* la méthode `followed_topics()` qui renvoyer un itérable.

```python
try:
    student = Student("Achille", "Talon")
    student.add_grade("History", 10.)
    topics = student.followed_topics()
    if len(topics) != 1 or "History" not in topics:
        raise Exception(f"Expecting ['History'] got {topics}")
except Exception as e:
    print('[Student.followed_topic] Does not work')
    print(f"Error message : {e}")   
else:
    print('[Student.followed_topic] OK')
```

#### `compute_average`

Nous voudrions calculer la moyenne de l'élève pour une matière donnée. Implémentez la méthode `compute_average(topic: str)`. Nous fixons comme convention que si l'élève n'a pas de note dans la matière demandée, la méthode renvoie -1 (*n'oubliez pas la méthode que vous venez de coder...*). Le code suivant doit s'exécuter sans erreur :

```python
try:
    student = Student("Achille", "Talon")
    student.add_grade("History", 10.)
    student.add_grade("History", 12.)
    if (student.compute_average("History") != 11.):
        raise Exception(f"Issue in your average calculation.")
    if (student.compute_average("French") != -1.):
        raise Exception("If topic is not followed return -1")
except Exception as e:
    print('[student.compute_average] Does not work')
    print(f"Error message : {e}")    
else:
    print('[student.compute_average] OK')
```

### `report`

Finalement, il ne manque plus qu'à afficher à l'écran le bulletin de l'élève en codant la fonction`report()` qui renvoie la chaine de caractères qui s'affiche comme suit :
```
Report for student Albert Einstein
+===============+===============+
|     Topic     |    Average    |
+===============+===============+
|   Chemistry   |     11.33     |
+---------------+---------------+
|    English    |     14.00     |
+---------------+---------------+
|    Physics    |     13.25     |
+---------------+---------------+
|    French     |     11.50     |
+---------------+---------------+
|  Mathematics  |     12.80     |
+---------------+---------------+
|  Scubadiving  |     12.50     |
+---------------+---------------+
```

```python
try:
    reference_lines = ['Report for student Albert Einstein', 
                       '+===============+===============+', 
                       '|     Topic     |    Average    |', 
                       '+===============+===============+', 
                       '|  Mathematics  |     12.80     |', 
                       '+---------------+---------------+', 
                       '|  Scubadiving  |     12.50     |', 
                       '+---------------+---------------+']
    
    student = Student("Albert", "Einstein")
    student.add_grade("Mathematics", 12.80)
    student.add_grade("Scubadiving", 12.50)
    report = student.report()
    report_lines = report.strip().split('\n')
    for i, (lineref, linestudent) in enumerate(zip(reference_lines, report_lines), start=1):
        assert lineref == linestudent, f"Ligne {i} : attendu = {lineref}// obtenu = {linestudent}"
except AssertionError as e:
    print('[student.report] Does not work')
    print("Les deux chaines sont différentes")
    print(e)
except Exception as e:
    print('[student.report] Does not work')
    print(f"Error message : {e}")
else:
    print('[student.report] OK')
```

## La classe `Class`

Nous allons maintenant gérer un ensemble d'élèves dans l'objet `Class`.

```python
class Class:
    def __init__(self, classname: str):
        pass
        
    def add_student(self, student: Student):
        pass

    def __len__(self):
        return 0

    def __repr__(self):
        return f""
```

### Premières méthodes

Implémentez les méthodes dont les prototypes sont données dans la cellule précédente. Le code suivant doit s'exécuter sans problèmes : 

**Note :** Nous aurons besoin par la suite de savoir rapidement si un élève est dans la classe et d'y accéder. Évitez donc de stocker les étudiants dans une simple liste.

```python
try:
    classe = Class("P20")
    student = Student("Matthieu", "Mazière")
    classe.add_student(student)
    if len(classe) != 1:
        raise Exception('OOPS - There is an issue in your __len__ method.')
    if repr(classe) != "Class P20 - 1 student(s)":
        raise Exception('OOPS - There is an issue in your __repr__ method.')
except Exception as e:
    print('[Class.__init__, Class.__len__, Class.__repr__] Does not work')
    print(f"Error message : {e}")
else:
    print('[Class.__init__, Class.__len__, Class.__repr__] OK')
```

### Accès à un élève 

Nous aimerions pouvoir accèder très facilement à un élève de la classe. Pour cela, codez la méthode `get_student(first_name: str, last_name:str)` qui permet au code suivant de s'exécuter sans erreur :

```python
try:
    classe = Class("P20")
    student = Student("Matthieu", "Mazière")
    classe.add_student(student)
    new_student = classe.get_student("Matthieu", "Mazière")
    assert student == new_student
    new_student = classe.get_student("Jérôme", "Adnot")
    assert new_student is None
except Exception as e:
    print('[Class.add_student, Class.get_student] Does not work')
    print(f"Error message : {e}")
else:
    print('[Class.add_student, Class.get_student] OK')
```

### Initialisons la classe à partir d'un fichier

Nous nous plaçons dans le cas où l'effectif d'une classe est définie dans le fichier `class.csv`. Chaque ligne de ce fichier contient le prénom et le nom d'un étudiant (vous en connaissez peut-être quelques-uns) :

```
Andre Marie,Ampere
Henri,Becquerel
Daniel,Bernoulli
Alfred,Binet
Niels,Bohr
Ludwig,Boltzmann
Max,Born
Carl,Bosch
Lawrence,Bragg
...
```

Implémentez la méthode `load_students_from_file(filename: str)` qui permet de remplir la classe. Le code suivant doit s'exécuter sans problèmes :

```python
try:
    classe = Class("P1920")
    classe.load_students_from_file('class.csv')
    if len(classe) != 89:
        raise Exception('OOPS - There is an issue in your load_from_file method')
except Exception as e:
    print('[Class.load_students_from_file] Does not work')
    print(f"Error message : {e}")
else:
    print('[Class.load_students_from_file] OK')
```

### Saisie de notes pour les élèves
Nous allons maintenant rentrer les notes des élèves pour les différentes matières. Cette saisie ce fait aussi *via* un fichier csv que vous allez devoir parser. Dans ce cas, chaque ligne du fichier est découpée comme suit : 

`Prénom, Nom, Matière, Note1, Note2, ..., NoteN`

```python
Francis,Galton,Physics,17.0,15.0,8.0,8.0
Enrico,Fermi,English,17.0,14.0
Heinrich,Hertz,Mathematics,17.0,12.0,13.0,11.0,18.0
Henri,Poincare,Mathematics,11.0,11.0,13.0,11.0,10.0
Claude,Levi-Strauss,Physics,15.0,12.0,14.0,12.0
...
```

Il est à noter d'une part que le nombre de notes dépend de la matière et d'autre part que tous les élèves ne suivent pas les mêmes cours. Implémentez la méthode `load_grades_from_file(filename: str)` qui permet d'affecter à chaque étudiant ses notes. 

**Note :** Dans le cas où l'on souhaiterait attribuer une note à un étudiant qui n'est pas dans la classe, il ne faut pas lever d'exception, mais seulement imprimer un message d'avertissement.

```python
try:
    classe = Class("P1920")
    classe.load_students_from_file('class.csv')
    classe.load_grades_from_file('grades.csv')
    assert classe.get_student("Albert", "Einstein").compute_average("Physics") == 13.25
    assert classe.get_student("Richard", "Feynman").compute_average("Physics") == 12.
    assert classe.get_student("Pierre", "Curie").compute_average("Scubadiving") == 9.5
except Exception as e:
    print('[Class.load_grades_from_file] Does not work')
    print(f"Error message : {e}")
else:
    print('[Class.load_grades_from_file] OK')
```

### Catalogue des matières suivies par les élèves de la classe
Implémentez la méthode `catalog()` qui renvoie un dictionnaire dont les clés sont les noms des matières et les valeurs sont le nombre d'étudiants suivant chaque cours. Le code suivant vous permet de valider votre implémentation :

```python
try:
    classe = Class("P1920")
    classe.load_students_from_file('class.csv')
    classe.load_grades_from_file('grades.csv')
    true_catalog = {'Physics': 89, 'Mathematics': 89, 'Chemistry': 89,
                    'English': 69, 'French': 30, 'Scubadiving': 10, 'Horse-riding': 15, 'Sailing': 3}
    assert classe.catalog() == true_catalog
except Exception as e:
    print('[Class.catalog] Does not work')
    print(f"Error message : {e}")
else:
    print('[Class.catalog] OK')
```

### Calcul des moyennes par matière
Nous allons maintenant nous intéresser à calculer des moyennes de la classe par matière. Codez la méthode `compute_averages()`. Cette dernière doit retourner un dictionnaire dont les clés sont des matières et les valeurs les moyennes de la classe.

```python
try:
    import math
    classe = Class("P1920")
    classe.load_students_from_file('class.csv')
    classe.load_grades_from_file('grades.csv')
    true_averages = {'Physics': 12.053370786516854,
                    'Mathematics': 12.071910112359552,
                    'Chemistry': 11.977528089887638,
                    'English': 12.369565217391305,
                    'French': 11.683333333333334,
                    'Scubadiving': 11.7,
                    'Horse-riding': 11.366666666666667,
                    'Sailing': 14.0}
    avgs = classe.compute_averages()
    assert all(math.isclose(avgs[top], true_averages[top]) for top in true_averages)
except Exception as e:
    print('[Class.compute_averages] Does not work')
    print(f"Error message : {e}")
else:
    print('[Class.compute_averages] OK')
```

### Pour les plus forts
Répercutez les infos sur la classe sur la méthode `report` de l'étudiant. Vous pouvez par exemple afficher la moyenne de l'étudiant mais aussi celle de la classe, le nombre d'élèves suivant le cours ou le rang de l'élève dans la classe.


## License

All exercises above are licensed _CC BY-NC-ND, Thierry Parmentelat_

- [Source](https://github.com/flotpython/exos/blob/main/python-tps/students-grades/README-students.md
