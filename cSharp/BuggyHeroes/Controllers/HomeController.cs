using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;

namespace Superheroes.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            return View();
        }

        [HttpGet]
        [Route("signin")]
        public IActionResult SignIn(string username)
        {
            HttpContext.Session.SetString("username", username);
            return RedirectToAction("Index", "Team");
        }
    }
}