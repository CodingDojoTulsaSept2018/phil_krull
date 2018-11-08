using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using BooksAndAuthors.Models;
using Microsoft.EntityFrameworkCore;

namespace BooksAndAuthors.Controllers
{
    public class HomeController : Controller
    {
        private Context _context;

        public HomeController(Context contextModel)
        {
            _context = contextModel;
        }
        public IActionResult Index()
        {
            // LINQ query for get all
            List<Author> AllAuthors = _context.Authors.ToList();

            foreach(Author author in AllAuthors)
            {
                Console.WriteLine($"The authors name is: {author.Name}");
            }

            return View();
        }

        public IActionResult About()
        {
            ViewData["Message"] = "Your application description page.";
            // for delete
            Author AuthorToChange = _context.Authors.FirstOrDefault(author => author.Name.Contains("Dave"));

            _context.Authors.Remove(AuthorToChange);

            // could replace from a form submission
            Author NewAuthor = new Author();
            NewAuthor.Name = "Dr. Seuss";

            _context.Authors.Add(NewAuthor);
            _context.SaveChanges();

            return View();
        }

        public IActionResult Contact()
        {
            ViewData["Message"] = "Your contact page.";

            // for update
            Author AuthorToChange = _context.Authors.FirstOrDefault(author => author.Name.Contains("Dr."));
            AuthorToChange.Name = "Dave";
            _context.SaveChanges();

            return View();
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
