namespace HumanOOP
{
    // 1.) Create a Human class with five fields: name, strength, intelligence, dexterity, and health
    class Human
    {
        // this is where the class members and methods go
        // define both with an access modifier ie(public, private, protected, internal or protected internal)
        // defind the members
        // (access modifer) (type) (name) initialize(optional)
        // 2.) Give a default value of 3 for strength, intelligence, and dexterity. Health should have a default of 100.
        public string Name;
        public int Health;
        public int Intelligence = 3;
        public int Dexterity = 3;
        public int Strength = 3;

        // contructor, which is the same name as the class, no return type
        // define the types of the arguements, passed into the methods
        // the constructor is invoke only when the class is instantiated
        // 3.) When an object is constructed from this class it should have the ability to pass a name
        public Human(string _name)
        {
            Name = _name;
            Health = 100;
        }
        public Human(int _strength)
        {
            Strength = _strength;
        }
        // 4.) Let's create an additional constructor that accepts 5 parameters, so we can set custom values for every field.
        // an example of method overloading
        public Human(string _name, int _health, int _intelligence, int _dexterity, int _strength)
        {
            Name = _name;
            Health = _health;
            Intelligence = _intelligence;
            Dexterity = _dexterity;
            Strength = _strength;
        }
        // 5.) Now add a new method called attack, which when invoked, should attack another Human object that is passed as a parameter. The damage done should be 5 * strength (5 points of damage to the attacked, for each 1 point of strength of the attacker).
        // method signature
        // (access modifier) (return type) (method name) (code block)
        public void Attack(Human human)
        {
            // this is the human that is invoking the methods ie human1.Attack(human2)
            // human health to go down 5* the strenght of this
            human.Health -= this.Strength * 5;
        }
    }
}