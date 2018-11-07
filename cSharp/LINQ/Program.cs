using System;
using System.Collections.Generic;
using System.Linq;

namespace LINQ
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> Food = new List<string> {
                              "apple",
                              "banana",
                              "carrot",
                              "cake",
                              "cucumber",
                              "fudge",
                              "tomato",
                              "tacos"
                          };

            IEnumerable<string> result = from food in Food where food[0] == 'z' select food;
            foreach(string food in result)
            {
                Console.WriteLine(food);
            }

            List<string> result2 = Food.Where(food => food[0] == 'c').ToList();
            foreach(string food in result2)
            {
                Console.WriteLine(food);
            }


            List<string> Adjective = new List<string> {
                                        "tasty",
                                        "capital",
                                        "best",
                                        "typical",
                                        "flavorful",
                                        "toothsome"
                                    };
            
            // each string in the Food list will be combined with each adjective from the Adjective list where their first characters match
            //METHOD SYNTAX
            IEnumerable<string> Combo1 = Food.Join(Adjective, 
                                            foodItem => foodItem[0],
                                            adjective => adjective[0],
                                            (foodItem, adjective) =>
                                            {
                                                return adjective + " " + foodItem;
                                            });
            
            //QUERY SYNTAX
            IEnumerable<string> Combo2 = from foodItem in Food
                                    join adjective in Adjective on foodItem[0] equals adjective[0]
                                    select adjective + " " + foodItem;
            //Combo:   "best banana",
            //         "capital carrot",
            //         "flavorful fudge",
            //         "tasty tomato",
            //         "typical tomato",
            //         "toothsome tomato"
            
            // Notice that apple is not in the combination collection because it does not match an adjective, but tomato occurs three times because it matched three different adjectives

        }
    }
}
