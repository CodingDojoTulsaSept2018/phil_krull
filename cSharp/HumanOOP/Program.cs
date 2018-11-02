using System;

namespace HumanOOP
{
    public class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("------------------------------------------------------");
            Human human1 = new Human("Melanie");
            // declare then initialize
            // something on the right = something on the left
            Console.WriteLine($"The name of human1 is: { human1.Name }");
            Console.WriteLine($"The health of human1 is: { human1.Health }");
            Console.WriteLine($"The Strength of human1 is: { human1.Strength }");
            Console.WriteLine($"The Dexterity of human1 is: { human1.Dexterity }");
            Console.WriteLine($"The Intelligence of human1 is: { human1.Intelligence }");
            Console.WriteLine("------------------------------------------------------");
            Human human2 = new Human("Don", 200, 4, 1, 3);
            Console.WriteLine($"The name of human2 is: { human2.Name }");
            Console.WriteLine($"The health of human2 is: { human2.Health }");
            Console.WriteLine($"The Strength of human2 is: { human2.Strength }");
            Console.WriteLine($"The Dexterity of human1 is: { human2.Dexterity }");
            Console.WriteLine($"The Intelligence of human1 is: { human2.Intelligence }");
            Console.WriteLine("------------------------------------------------------");
            Human human3 = new Human(3);
            human1.Attack(human2);
            Console.WriteLine($"The health of human2 after the attack is: { human2.Health }");
        }
    }
}
